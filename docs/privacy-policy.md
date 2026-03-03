---
layout: default
title: 隱私權政策
parent: 說明
nav_order: 5
description: "ThTxGNN SMART on FHIR 應用程式隱私權政策，說明資料收集、使用、儲存與安全措施。"
permalink: /privacy-policy/
---

# 隱私權政策

**最後更新日期**：2026 年 2 月 27 日

---

## 概述

<p class="key-answer" data-question="ThTxGNN 如何處理我的資料？">
ThTxGNN SMART App 是一個<strong>純前端應用程式</strong>，所有資料處理都在您的瀏覽器中進行。我們<strong>不收集、不儲存、不傳輸</strong>任何病患的個人健康資訊 (PHI) 到我們的伺服器。
</p>

---

## 資料收集與使用

### 我們不收集的資料

| 資料類型 | 收集情形 |
|----------|----------|
| 病患姓名、生日、聯絡資訊 | **不收集** |
| 病患用藥記錄 | **不收集** |
| 診斷紀錄 | **不收集** |
| 任何個人健康資訊 (PHI) | **不收集** |

### 應用程式如何運作

<ol class="actionable-steps">
<li><strong>EHR 授權</strong>：您從電子病歷系統 (EHR) 啟動 ThTxGNN SMART App</li>
<li><strong>本地處理</strong>：應用程式在您的瀏覽器中讀取用藥資料</li>
<li><strong>本地查詢</strong>：藥物映射和老藥新用查詢完全在瀏覽器中完成</li>
<li><strong>無資料外傳</strong>：病患資料不會離開您的瀏覽器</li>
</ol>

---

## 技術架構與安全措施

### 純前端架構

<p class="key-answer" data-question="ThTxGNN 的技術架構是什麼？">
ThTxGNN SMART App 採用<strong>純前端（Client-Side Only）</strong>架構：所有程式碼都在使用者的瀏覽器中執行，不需要後端伺服器處理病患資料。
</p>

| 項目 | 說明 |
|------|------|
| 伺服器端處理 | 無 |
| 資料庫 | 無（使用靜態 JSON 檔案） |
| 病患資料儲存 | 無 |
| Session 儲存 | 僅在瀏覽器記憶體中，關閉即清除 |

### OAuth 2.0 安全授權

本應用程式使用 **OAuth 2.0 with PKCE**（Proof Key for Code Exchange）進行授權：

- **PKCE 保護**：防止授權碼攔截攻擊
- **最小權限原則**：只請求必要的讀取權限
- **無長期憑證**：不儲存 refresh token

### 請求的權限範圍

```
launch                          - EHR 啟動上下文
patient/MedicationRequest.read  - 讀取用藥處方
patient/MedicationStatement.read - 讀取用藥陳述
openid                          - OpenID Connect 身份驗證
fhirUser                        - 使用者資訊
```

---

## 第三方服務

### 使用的外部服務

| 服務 | 用途 | 資料傳輸 |
|------|------|----------|
| **RxNorm API** | 藥物名稱查詢 | 僅傳送 RxCUI 代碼（非病患資料） |
| **CDN (jsDelivr)** | JavaScript 函式庫載入 | 無病患資料 |

### 靜態資源

藥物預測資料庫（`search-index.json`）是靜態檔案，不包含任何使用者或病患資訊。

---

## 網站分析

### 我們的網站

ThTxGNN 網站（thtxgnn.yao.care）可能使用以下分析工具：

- **匿名流量統計**：頁面瀏覽數、訪客來源等
- **無個人識別**：不追蹤個別使用者行為

### SMART App

SMART App 本身**不包含任何分析追蹤程式碼**，確保病患資料的完全隱私。

---

## 資料儲存

### 本地儲存

| 儲存位置 | 內容 | 存續時間 |
|----------|------|----------|
| 瀏覽器記憶體 | OAuth token、用藥資料 | 關閉分頁即清除 |
| Local Storage | 無 | 不使用 |
| Session Storage | 無 | 不使用 |
| Cookies | 無 | 不使用 |

### 伺服器端儲存

**無**。我們沒有後端伺服器，不儲存任何使用者或病患資料。

---

## HIPAA 合規聲明

雖然 ThTxGNN 主要針對泰國健保藥品，本應用程式的設計符合 HIPAA 隱私規則的精神：

<div class="key-takeaway">
<strong>隱私保護措施</strong>
<ul>
<li>無 PHI 傳輸至外部伺服器</li>
<li>純前端處理，資料不離開瀏覽器</li>
<li>使用加密連線 (HTTPS)</li>
<li>OAuth 2.0 + PKCE 安全授權</li>
<li>最小權限原則</li>
</ul>
</div>

---

## 開源透明

ThTxGNN 是開源專案，您可以檢視完整的程式碼：

- **GitHub**: [https://github.com/yao-care/ThTxGNN](https://github.com/yao-care/ThTxGNN)
- **SMART App 程式碼**: `docs/smart/` 目錄

<blockquote class="expert-quote">
「透明度是建立信任的基礎。開源程式碼允許任何人驗證我們的隱私聲明。」
</blockquote>

---

## 兒童隱私

本應用程式不特別針對 13 歲以下兒童設計，但作為醫療輔助工具，可能用於顯示兒科病患的用藥資訊。無論使用者年齡，我們都不收集任何個人資料。

---

## 政策變更

如果本隱私權政策有重大變更，我們將：

1. 更新本頁面的「最後更新日期」
2. 在 GitHub 專案中記錄變更
3. 保持變更的透明度

---

## 聯絡我們

如有隱私相關問題，請透過以下方式聯繫：

- **GitHub Issues**: [https://github.com/yao-care/ThTxGNN/issues](https://github.com/yao-care/ThTxGNN/issues)
- **專案首頁**: [https://thtxgnn.yao.care/](https://thtxgnn.yao.care/)

---

## 相關連結

- [SMART on FHIR 技術文件](/smart/)
- [關於專案](/about/)
- [資料來源](/sources/)

---

<div class="disclaimer">
<strong>免責聲明</strong><br>
本隱私權政策僅適用於 ThTxGNN SMART App 和 thtxgnn.yao.care 網站。當您使用第三方 EHR 系統時，該系統的隱私政策可能另有規定。
<br><br>
<small>最後審核：2026-02-27 | 審核者：ThTxGNN Team</small>
</div>
