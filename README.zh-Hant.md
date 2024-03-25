[English](README.md) | [简体中文](README.zh-Hans.md) | **繁體中文**

> [!WARNING]
>
> 隨更新本文檔可能過時，最終請以 [英文文檔](README.md) 為準。

# bookstw
由 [selenium](https://selenium-python.readthedocs.io/) 驅動，`bookstw` 是一個用於與[博客來網路書店](https://books.com.tw/)進行交互的 Python 庫。

## 安裝
```bash
pip install bookstw
```

## 快速開始
以下示例演示了登錄並進行每日簽到的過程：

> [!NOTE]
>
> 目前，這是 `bookstw` 提供的唯一功能。

```python
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from bookstw import BooksTWRunner
from bookstw.ocr.baidu import BaiduHandwritingOCR

if __name__ == "__main__":
    baidu_ocr = BaiduHandwritingOCR(
        proxy={"http": "", "https": ""},
        api_key="<YOUR_API_KEY>",
        secret_key="<YOUR_SECRET>"
    )
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")
    options.add_argument("--headless")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome = Chrome(options)

    runner = BooksTWRunner(ocr=baidu_ocr, webdriver=chrome)
    runner.login("<YOUR_USERNAME>", "<YOUR_PASSWORD>")
    runner.daily_sign_in()
```

上述代碼片段演示了如何使用 `bookstw` 進行每日簽到。

`BaiduHandwritingOCR` 用於解決驗證碼。它在內部調用 [百度手寫文字識別 API](https://cloud.baidu.com/product/ocr_others/handwriting) 來識別驗證碼圖片。

目前，它是 `bookstw` 支持的唯一 OCR 提供商。然而，你可以通過繼承 [`BaseOCR` 類](./src/bookstw/ocr/__init__.py) 來實現你自己的 OCR 提供商。

## Github Actions
### [auto-signin.yml](.github/workflows/auto-signin.yml)
Fork 這個倉庫並在你的倉庫中創建以下 Secrets：
- `BAIDU_API_KEY`
- `BAIDU_SECRET_KEY`
- `BOOKS_TW_USERNAME`
- `BOOKS_TW_PASSWORD`

將 .yml 文件中的 `INSTALL_FROM` 環境變量更改為 `PyPI` 以從 PyPI 安裝發布版，或者保持為 `Poetry` 以從源碼安裝。

## API 參考
### `bookstw.BooksTWRunner`
#### `bookstw.BooksTWRunner.__init__(ocr: BaseOCR, webdriver: WebDriver)`
創建一個新的 `BooksTWRunner` 實例。

- `ocr`：用於解決驗證碼的 OCR 提供商。
- `webdriver`：用於與博客來網路書店進行交互的 WebDriver。

#### `bookstw.BooksTWRunner.login(self, username: str, password: str, allow_manual_retry: bool = True, ocr_retry: int = 3, retry_delay: int = 5) -> None`
登錄博客來網路書店。

驗證碼通過 OCR 解決。

- `username`：用戶名。
- `password`：密碼。
- `allow_manual_retry`：如果 OCR 失敗，是否允許手動重試。
- `ocr_retry`：OCR 的重試次數。
- `retry_delay`：重試之間的延遲（以秒為單位）。

#### `bookstw.BooksTWRunner.daily_sign_in(self) -> None`
每日簽到以獲取閱讀里程。

如果已經簽到，它將拋出一個異常。