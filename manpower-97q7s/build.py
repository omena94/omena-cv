"""Build the job-specific public CV and application letter from cv.json."""
import json
from html import escape as e
from pathlib import Path

ROOT = Path(__file__).resolve().parent
cv = json.loads((ROOT / 'cv.json').read_text(encoding='utf-8'))


def bullets(items):
    return '<ul>' + ''.join(f'<li>{e(item)}</li>' for item in items) + '</ul>' if items else ''


def heading(title, period):
    return f'<div class="entry-heading"><h3>{e(title)}</h3><span class="period">{e(period)}</span></div>'


def entries(items):
    return ''.join(f'<article class="entry">{heading(x["title"], x["period"])}<p class="organization">{e(x["organization"])}</p>{bullets(x["bullets"])}</article>' for x in items)


def labeled(items):
    return '<ul class="competencies">' + ''.join(f'<li><strong>{e(x["label"])}：</strong>{e(x["text"])}</li>' for x in items) + '</ul>'


project = cv['project']
education = ''.join(f'<article class="education-entry">{heading(x["school"], x["period"])}<p>{e(x["degree"])}</p></article>' for x in cv['education'])
html = f'''<!doctype html>
<html lang="zh-Hant">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="余孟庭 Omena 的廠護履歷：勞工健康服務、健檢追蹤、臨床護理與緊急應變經驗。提供兩頁 PDF。">
  <meta name="theme-color" content="#245b85">
  <meta property="og:title" content="余孟庭 Omena｜外商廠護應徵履歷">
  <meta property="og:description" content="勞工健康服務・健檢追蹤・緊急應變">
  <meta property="og:type" content="profile">
  <meta property="og:url" content="https://omena94.github.io/omena-cv/manpower-97q7s/">
  <title>余孟庭 Omena｜外商廠護應徵履歷</title>
  <link rel="icon" href="../favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="../styles.css">
</head>
<body>
  <a class="skip-link" href="#cv">跳至履歷內容</a>
  <nav class="toolbar" aria-label="履歷導覽">
    <a class="wordmark" href="#cv">Omena 的廠護履歷</a>
    <div class="nav-links"><a href="#experience">工作經驗</a><a href="#qualifications">專業資格</a><a class="download" href="Omena-Occupational-Nurse-CV.pdf" download>下載 PDF<span class="download-detail"> · 2 頁</span></a></div>
  </nav>
  <main id="cv">
    <div class="sheet sheet-one">
      <header class="identity">
        <h1>{e(cv['name'])} <span>{e(cv['alias'])}</span></h1>
        <p class="romanized">{e(cv['romanized'])}</p>
        <p class="headline">{e(cv['headline'])}</p>
        <p class="target">{e(cv['target'])}</p>
        <div class="contacts"><span>{e(cv['location'])}</span><a href="mailto:{e(cv['email'])}">{e(cv['email'])}</a><a href="{e(cv['github'])}">github.com/omena94</a></div>
        <p class="availability">{e(cv['availability'])}</p>
      </header>
      <section class="profile" aria-label="個人摘要"><p>{e(cv['summary'])}</p></section>
      <section aria-labelledby="qualifications"><h2 id="qualifications">專業資格</h2>{labeled(cv['qualifications'])}</section>
      <section aria-labelledby="skills"><h2 id="skills">核心能力</h2>{labeled(cv['competencies'])}</section>
      <section aria-labelledby="experience"><h2 id="experience">相關工作經驗</h2>{entries(cv['experience'])}</section>
      <footer class="page-footer"><span>余孟庭 · 廠護應徵履歷</span><span>1 / 2</span></footer>
    </div>
    <div class="sheet sheet-two">
      <header class="continuation"><span>余孟庭 Omena</span><span>臨床經歷・職護工具・學歷</span></header>
      <section aria-labelledby="clinical"><h2 id="clinical">臨床護理經歷</h2>{entries(cv['clinical'])}</section>
      <section aria-labelledby="project"><h2 id="project">職護實務工具</h2><article class="entry project">{heading(project['title'], project['period'])}<p class="organization">{e(project['role'])}</p>{bullets(project['bullets'])}<a class="project-link" href="{e(project['url'])}">{e(project['link_label'])}</a></article></section>
      <section aria-labelledby="education"><h2 id="education">學歷</h2>{education}</section>
      <section class="qualifications" aria-labelledby="tools"><h2 id="tools">文書與語言</h2><p><strong>文書與資料：</strong>{e(cv['tools'])}</p><p><strong>語言能力：</strong>{e(cv['languages'])}</p></section>
      <footer class="page-footer"><span>余孟庭 · 廠護應徵履歷</span><span>2 / 2</span></footer>
    </div>
  </main>
  <footer class="site-footer"><span>更新於 {e(cv['updated'])}</span><a href="{e(cv['job_url'])}">104 職缺</a><a href="https://github.com/omena94/omena-cv/tree/main/manpower-97q7s">履歷原始檔</a><a href="mailto:{e(cv['email'])}">Email 聯絡</a></footer>
</body>
</html>
'''
(ROOT / 'index.html').write_text(html, encoding='utf-8')
(ROOT / 'cover-letter.txt').write_text('\n\n'.join(cv['letter']) + '\n', encoding='utf-8')
print('Rendered manpower-97q7s/index.html and cover-letter.txt')
