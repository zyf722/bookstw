import os

from bookstw import BooksTWRunner
from bookstw.ocr.baidu import BaiduHandwritingOCR
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

if __name__ == "__main__":
    baidu_ocr = BaiduHandwritingOCR(
        proxy={"http": "", "https": ""},
        api_key=os.environ["BAIDU_API_KEY"],
        secret_key=os.environ["BAIDU_SECRET_KEY"],
    )
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")
    options.add_argument("--headless")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome = Chrome(options)

    runner = BooksTWRunner(ocr=baidu_ocr, webdriver=chrome)
    runner.login(
        username=os.environ["BOOKS_TW_USERNAME"],
        password=os.environ["BOOKS_TW_PASSWORD"],
        allow_manual_retry=False,
    )
    runner.daily_sign_in()
