**English** | [简体中文](README.zh-CN.md)

# bookstw
Powered by [selenium](https://selenium-python.readthedocs.io/), `bookstw` is a simple library to interact with Books.com.tw.

## Installation
```bash
pip install bookstw
```

## Quick Start
Let's get started with a simple example that logs in to Books.com.tw and signs in daily.

> [!NOTE]
>
> For now it is the only feature provided by `bookstw`.

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

The above code snippet demonstrates how to sign in daily with `bookstw`.

The `BaiduHandwritingOCR` is used to solve the captcha.  Currently, it is the only OCR provider supported by `bookstw`. However, you can implement your own OCR provider by inheriting the [`BaseOCR` class](./src/bookstw/ocr/__init__.py).

## Github Actions
Fork this repository and create the following secrets in your repository:
- `BAIDU_API_KEY`
- `BAIDU_SECRET_KEY`
- `BOOKS_TW_USERNAME`
- `BOOKS_TW_PASSWORD`

Check the [workflow file](.github/workflows/auto-signin.yml) for more details.

## API Reference
### `bookstw.BooksTWRunner`
#### `bookstw.BooksTWRunner.__init__(ocr: BaseOCR, webdriver: WebDriver)`
Creates a new `BooksTWRunner` instance.

- `ocr`: The OCR provider used to solve the captcha.
- `webdriver`: The WebDriver used to interact with Books.com.tw.

#### `bookstw.BooksTWRunner.login(self, username: str, password: str, ocr_retry: int = 3, retry_delay: int = 5) -> None`
Login to books.com.tw.

- `username`: Username.
- `password`: Password.
- `ocr_retry`: Number of retries for OCR.
- `retry_delay`: Delay between retries in seconds.

#### `bookstw.BooksTWRunner.daily_sign_in(self) -> None`
Sign in daily.
