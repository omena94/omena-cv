# Omena · 余孟庭的 CV

- [線上閱讀](https://omena94.github.io/omena-cv/)
- [下載兩頁 PDF](https://omena94.github.io/omena-cv/Omena-CV.pdf)
- [GitHub](https://github.com/omena94)

繁體中文履歷，聚焦醫療資訊需求分析、跨部門協作與網頁專案。內容及章節依 `ai-job-search` 的候選人資料與 CV 工作流程整理；網頁沿用 moderncv banking 的單欄結構與藍色標題，並提供兩頁 A4 PDF。

## 更新

`cv.json` 是網頁與 PDF 的共同內容來源。修改後執行：

```bash
python build.py
python -m http.server 8794 --bind 127.0.0.1
```

開啟 `http://127.0.0.1:8794`，使用瀏覽器列印功能，紙張選 A4、縮放 100%、不加頁首頁尾，確認預覽恰為兩頁後存成 `Omena-CV.pdf`。

Windows 字型經瀏覽器列印後，部分中文字可能在 PDF 文字層變成同形部首。存檔後執行下列步驟修正文字對應，再確認頁數及複製文字：

```bash
python -m pip install pypdf
python normalize_pdf.py
```

此步驟只修正字型的 Unicode 對應，不變更字形、頁面內容或排版。

`styles.css` 包含手機版與列印樣式。網站為純靜態 HTML/CSS，不使用追蹤器、第三方字型或後端服務。

## 發布範圍

公開內容僅包含履歷、下載檔與建置來源；不包含原始履歷編輯頁、私人聯絡資料、求職紀錄或內部評估。
