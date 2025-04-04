#!/bin/bash

set -e

echo "==> 建立虛擬環境 brew reinstall python@3.13 --with-tcl-tk(venv)..."
python3 -m venv venv
source venv/bin/activate

echo "==> 安裝依賴 (selenium, ntplib, pillow, pytesseract)..."
pip install --upgrade pip
pip install selenium ntplib pillow pytesseract

echo "==> 安裝 tesseract OCR（如未安裝）"
if ! command -v tesseract &> /dev/null; then
  brew install tesseract
fi

echo "==> 安裝 ChromeDriver for macOS M1（版本 124）"
CHROME_VERSION="124.0.6367.60"
ZIP_URL="https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/${CHROME_VERSION}/mac-arm64/chromedriver-mac-arm64.zip"
curl -# -L -o chromedriver.zip "$ZIP_URL"
unzip -o chromedriver.zip
mv chromedriver-mac-arm64/chromedriver .
chmod +x chromedriver
rm -rf chromedriver.zip chromedriver-mac-arm64

echo "==> 使用內建 Python 執行 GUI（具有 tkinter）"
export VENV_PATH="$(pwd)/venv/bin/python"
/usr/bin/python3 ticket_bot_gui.py
