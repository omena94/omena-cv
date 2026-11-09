"""Repair Chromium's CJK radical aliases without changing rendered glyphs.

Some Windows fonts map both an ideograph and its Kangxi radical to one glyph.
Chromium can choose the radical for the PDF ToUnicode table. Normalize only
those CJK radical destinations so copy/paste and ATS text use the original
ideographs. Glyph identifiers, page contents, and visual layout stay intact.
Requires pypdf. Run after printing index.html to Omena-CV.pdf.
"""
from pathlib import Path
import re
import sys
import unicodedata
from pypdf import PdfReader, PdfWriter
from pypdf.generic import DecodedStreamObject, NameObject


def normalize_destination(value):
    text = bytes.fromhex(value).decode('utf-16-be')
    normalized = ''.join(
        unicodedata.normalize('NFKC', char) if 0x2E80 <= ord(char) <= 0x2FDF else char
        for char in text
    )
    return normalized.encode('utf-16-be').hex().upper()


def normalize_cmap(cmap):
    def chars(match):
        pairs = re.findall(r'<([0-9a-fA-F]+)>\s*<([0-9a-fA-F]+)>', match.group(1))
        return f'{len(pairs)} beginbfchar\n' + '\n'.join(
            f'<{source}> <{normalize_destination(target)}>' for source, target in pairs
        ) + '\nendbfchar'

    def ranges(match):
        pairs = []
        for item in re.finditer(r'<([0-9a-fA-F]+)>\s*<([0-9a-fA-F]+)>\s*(?:<([0-9a-fA-F]+)>|\[([^]]*)\])', match.group(1)):
            first, last, start, array = item.groups()
            count = int(last, 16) - int(first, 16) + 1
            if start:
                targets = [f'{int(start,16)+i:0{len(start)}X}' for i in range(count)]
            else:
                targets = re.findall(r'<([0-9a-fA-F]+)>', array)
                assert len(targets) == count
            pairs.extend((f'{int(first,16)+i:0{len(first)}X}', normalize_destination(target)) for i,target in enumerate(targets))
        chunks = []
        for offset in range(0, len(pairs), 100):
            chunk = pairs[offset:offset+100]
            chunks.append(f'{len(chunk)} beginbfchar\n' + '\n'.join(f'<{a}> <{b}>' for a,b in chunk) + '\nendbfchar')
        return '\n'.join(chunks)

    cmap = re.sub(r'\d+\s+beginbfchar\s*(.*?)\s*endbfchar', chars, cmap, flags=re.S)
    return re.sub(r'\d+\s+beginbfrange\s*(.*?)\s*endbfrange', ranges, cmap, flags=re.S)


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name('Omena-CV.pdf')
    reader = PdfReader(path)
    writer = PdfWriter()
    writer.clone_document_from_reader(reader)
    seen = set()
    repaired = 0
    for page in writer.pages:
        for reference in page['/Resources'].get('/Font', {}).values():
            font = reference.get_object()
            if id(font) in seen or '/ToUnicode' not in font:
                continue
            seen.add(id(font))
            original = font['/ToUnicode'].get_object().get_data().decode('ascii')
            updated = normalize_cmap(original)
            if original != updated:
                stream = DecodedStreamObject()
                stream.set_data(updated.encode('ascii'))
                font[NameObject('/ToUnicode')] = writer._add_object(stream)
                repaired += 1
    temporary = path.with_suffix('.normalized.pdf')
    with temporary.open('wb') as output:
        writer.write(output)
    temporary.replace(path)
    print(f'Normalized Unicode maps in {repaired} font resources: {path.name}')


if __name__ == '__main__':
    main()
