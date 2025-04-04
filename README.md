# 🎫 搶票機器人 Ticket Bot

本專案是一個使用 Python 與 tkinter 製作的搶票機器人，支援自動登入、定時搶票、以及多種票種與區域選擇。  
This project is a Python ticket bot built with tkinter. It supports auto-login, scheduled ticket booking, and multiple ticket/zone options.

---

## 📦 安裝與執行 / Installation & Running

1. **下載專案**  
   Download and unzip the project archive.

2. **執行安裝腳本**  
   Open Terminal, navigate to the project folder, and run:
   ```bash
   chmod +x run_ticket_bot.sh
   ./run_ticket_bot.sh

---
🖥️ 使用說明 / Usage
啟動 GUI 後，你將看到以下介面：

顯示模式：選擇「淺色」、「深色」或「自動」(預設深色模式)
(Theme selection: Light, Dark, or Auto)

自動登入：勾選後將自動填入登入資訊
(Auto-login option)

目標網站：輸入搶票的購票網址
(Enter the ticketing website URL)

帳號 / 密碼：輸入你的登入憑證
(Enter your account credentials)

搶票時間：格式 YYYY-MM-DD HH:MM:SS
(Enter the target ticket booking time)

選擇價格類型：選擇你想要的票價類型（1~4）
(Select ticket price types)

選擇區域：選擇你想要的票務區域（A, B, C）
(Select desired zones)

開始搶票：點擊此按鈕後，輸入的資料將保存並啟動搶票流程
(Press "Start Ticket Bot" to begin the booking process)

---

📄 檔案結構
檔案	| 說明	| Description
ticket_bot_gui.py	| GUI 主程式	| Main GUI application
ticket_bot.py	| 搶票邏輯 (使用 Selenium)	| Ticket booking logic using Selenium
ticket_bot_launcher.py	| 從 bot_args.json 啟動搶票流程	| Launcher reading input and starting bot
bot_args.json	| 儲存 GUI 輸入資料	| JSON file with user input data
ticket_log.txt	| 執行過程記錄	| Log file for recording execution steps
run_ticket_bot.sh	| 一鍵安裝與執行腳本	| Shell script for installation and launch

---

🔧 常見問題 / FAQ
Q: 為什麼介面顏色不正確？
A: 請確認已切換至「深色」或「淺色」模式。若仍有問題，可試著重啟程式。
(If the theme colors are not as expected, try switching the theme mode or restarting the application.)

Q: 沒有顯示目標網站、帳號、密碼或搶票時間？
A: 請確認你正在使用最新的 ticket_bot_gui.py，並未使用舊版本。
(Ensure you're using the latest version of ticket_bot_gui.py.)

Q: 如何處理驗證碼？
A: 目前系統僅提示使用者手動輸入驗證碼。未來版本可整合 OCR 自動識別功能。
(Currently, the bot requires manual captcha input. Future versions may integrate OCR for automatic recognition.)

