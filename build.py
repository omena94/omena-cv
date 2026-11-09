"""Render the public CV from one content source. No network access required."""
import json
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent
cv = json.loads((ROOT / 'cv.json').read_text(encoding='utf-8'))
e = escape

def bullets(items):
    return '<ul>' + ''.join(f'<li>{e(item)}</li>' for item in items) + '</ul>'

def heading(title, period):
    return f'<div class="entry-heading"><h3>{e(title)}</h3><span class="period">{e(period)}</span></div>'

competencies = '<ul class="competencies">' + ''.join(f'<li><strong>{e(x["label"])}：</strong>{e(x["text"])}</li>' for x in cv['competencies']) + '</ul>'
experience = ''.join(f'<article class="entry">{heading(x["title"],x["period"])}<p class="organization">{e(x["organization"])}</p>{bullets(x["bullets"])}</article>' for x in cv['experience'])
clinical = f'<article class="entry clinical">{heading(cv["clinical"]["title"],cv["clinical"]["period"])}<p>{e(cv["clinical"]["text"])}</p></article>'
projects = ''.join(f'<article class="entry project">{heading(x["title"],x["period"])}<p class="organization">{e(x["role"])}</p><p class="technology">{e(x["technology"])}</p>{bullets(x["bullets"])}<a class="project-link" href="{e(x["url"])}">{e(x["linkLabel"])}</a></article>' for x in cv['projects'])
education = ''.join(f'<article class="education-entry">{heading(x["school"],x["period"])}<p>{e(x["degree"])}</p></article>' for x in cv['education'])

html = f'''<!doctype html>
<html lang="zh-Hant">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="余孟庭 Omena 的履歷：資訊護理師、醫療需求分析、產品協作與 AI 輔助開發。查看工作經驗、專案及下載兩頁 PDF。">
  <meta name="theme-color" content="#245b85">
  <meta property="og:title" content="Omena 余孟庭｜個人履歷">
  <meta property="og:description" content="資訊護理師・需求分析・產品協作・AI 輔助開發">
  <meta property="og:type" content="profile">
  <meta property="og:url" content="https://omena94.github.io/omena-cv/">
  <title>Omena 余孟庭｜個人履歷</title>
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <a class="skip-link" href="#cv">跳至履歷內容</a>
  <nav class="toolbar" aria-label="履歷導覽">
    <a class="wordmark" href="#cv">Omena 的履歷</a>
    <div class="nav-links"><a href="#experience">工作經驗</a><a href="#projects">專案</a><a class="download" href="Omena-CV.pdf" download>下載 PDF<span class="download-detail"> · 2 頁</span></a></div>
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
      <section aria-labelledby="skills"><h2 id="skills">核心能力</h2>{competencies}</section>
      <section aria-labelledby="experience"><h2 id="experience">工作經驗</h2>{experience}{clinical}</section>
      <footer class="page-footer"><span>Omena · 余孟庭</span><span>1 / 2</span></footer>
    </div>
    <div class="sheet sheet-two">
      <header class="continuation"><span>余孟庭 Omena</span><span>專案・學歷・資格</span></header>
      <section aria-labelledby="projects"><h2 id="projects">精選專案</h2>{projects}</section>
      <section aria-labelledby="education"><h2 id="education">學歷</h2>{education}</section>
      <section class="qualifications" aria-labelledby="qualifications"><h2 id="qualifications">資格與語言</h2><p><strong>專業資格：</strong>{e(cv['certifications'])}</p><p><strong>語言能力：</strong>{e(cv['languages'])}</p></section>
      <footer class="page-footer"><span>Omena · 余孟庭</span><span>2 / 2</span></footer>
    </div>
  </main>
  <footer class="site-footer"><span>更新於 {e(cv['updated'])}</span><a href="https://github.com/omena94/omena-cv">查看履歷原始檔</a><a href="mailto:{e(cv['email'])}">Email 聯絡</a></footer>
</body>
</html>
'''
(ROOT / 'index.html').write_text(html, encoding='utf-8')
print('Rendered index.html from cv.json')
