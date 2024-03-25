[English](README.md) | **简体中文**

# bookstw
由 [selenium](https://selenium-python.readthedocs.io/) 驱动，`bookstw` 是一个用于与[博客来网络书店](https://books.com.tw/)进行交互的 Python 库。

## 安装
```bash
pip install bookstw
```

## 快速开始
以下示例演示了登录并进行每日签到的过程：

> [!NOTE]
>
> 目前，这是 `bookstw` 提供的唯一功能。

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

上述代码片段演示了如何使用 `bookstw` 进行每日签到。

`BaiduHandwritingOCR` 用于解决验证码。目前，它是 `bookstw` 支持的唯一 OCR 提供商。然而，你可以通过继承 [`BaseOCR` 类](./src/bookstw/ocr/__init__.py) 来实现你自己的 OCR 提供商。

## Github Actions
Fork 这个仓库并在你的仓库中创建以下 Secrets：
- `BAIDU_API_KEY`
- `BAIDU_SECRET_KEY`
- `BOOKS_TW_USERNAME`
- `BOOKS_TW_PASSWORD`

查看 [Workflow 文件](.github/workflows/auto-signin.yml) 以获取更多详情。

## API 参考
### `bookstw.BooksTWRunner`
#### `bookstw.BooksTWRunner.__init__(ocr: BaseOCR, webdriver: WebDriver)`
创建一个新的 `BooksTWRunner` 实例。

- `ocr`：用于解决验证码的 OCR 提供商。
- `webdriver`：用于与博客来网络书店进行交互的 WebDriver。

#### `bookstw.BooksTWRunner.login(self, username: str, password: str, ocr_retry: int = 3, retry_delay: int = 5) -> None`
登录博客来网络书店。

- `username`：用户名。
- `password`：密码。
- `ocr_retry`：OCR 的重试次数。
- `retry_delay`：重试之间的延迟（以秒为单位）。

#### `bookstw.BooksTWRunner.daily_sign_in(self) -> None`
每日签到。