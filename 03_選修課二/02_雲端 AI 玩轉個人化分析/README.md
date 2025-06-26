# The Mirror in Your Words. 雲端 AI 玩轉個人化分析。
為了方便大家進行部署，可直接 copy & paste 下方指令。
另外，也提供大家卸除服務的方法，務必確實執行。

## 常用指令

在 Cloud Shell 環境中，可以使用以下基本指令來進行檔案與目錄的操作。

| 指令 | 描述 |
| :--- | :--- |
| `ls` | 查看目前路徑下的檔案與資料夾。 |
| `pwd` | 顯示目前所在的完整路徑。 |
| `cd <folder>` | 進入指定的資料夾。 |
| `cd ..` | 回到上一層資料夾。 |
| `clear` | 清除畫面上的所有訊息。 |
| `cat <file_name>` | 查看並印出指定檔案的內容。 |

-----

## 部署指令

請依照以下步驟部署前後端應用程式。

### 1\. 獲取程式碼

首先，在 Cloud Shell 中，透過 `git` 下載原始碼並進入專案目錄。

```bash
git clone https://github.com/whyhugo/csie-camp-gcp-mbti.git
cd csie-camp-gcp-mbti
```

### 2\. 部署後端服務

進入後端函式目錄，並使用 `gcloud` 指令進行部署。

```bash
cd function-backend
gcloud functions deploy mbti-analyzer \
  --gen2 \
  --runtime python311 \
  --region=us-central1 \
  --trigger-http \
  --allow-unauthenticated \
  --entry-point mbti_analyzer \
  --memory=1Gi
```

部署成功後，系統會顯示後端服務的網址 (`uri`)，請務必將其複製下來。

### 3\. 部署前端應用

回到上一層，進入前端應用程式目錄。執行部署指令，並記得將 `<貼上後端網址>` 替換為上一步複製的 `uri`。

```bash
cd ../webapp-frontend
gcloud run deploy personal-mbti-app \
  --source . \
  --region=us-central1 \
  --allow-unauthenticated \
  --update-env-vars=FUNCTION_URL=<貼上後端網址>
```

### 4\. 驗證服務

部署完成後，打開前端服務的 `Service URL`，測試網站功能是否正常運作。

-----

## 課程結束後 - 資源卸除

為了避免 Google Cloud Platform 產生非預期的費用，請務必在課程結束後，透過以下任一方法清理所有已建立的資源。

### 方法一：逐一刪除服務

在 Cloud Shell 中，依序執行以下指令，分別刪除前端、後端服務以及 Cloud Storage 儲存桶。

```bash
# 1. 刪除前端 Cloud Run 服務
gcloud run services delete personal-mbti-app --region=us-central1

# 2. 刪除後端 Cloud Functions 服務
gcloud functions delete mbti-analyzer --region=us-central1

# 3. 刪除儲存桶 (注意：這會刪除裡面存放的所有圖片)
gsutil rm -r gs://$(gcloud config get-value project)-mbti-images
```

### 方法二：關閉整個專案 (最保險)

1.  前往 Google Cloud Platform 控制台。
2.  點擊左上角的導覽選單 **(☰)** \> **「IAM 與管理」** \> **「設定」**。
3.  在頁面頂端，點擊\*\*「關閉」\*\*按鈕。
4.  依照畫面指示，輸入該專案 ID 以確認操作。專案將會進入待刪除狀態，並在 30 天後被永久移除。