
# ticket_bot_launcher.py

import json
from datetime import datetime
from ticket_bot import TicketBot

with open("bot_args.json", "r", encoding="utf-8") as f:
    args = json.load(f)

summary = [
    "🎫 Ticket Bot 啟動參數如下：",
    f"📍 目標網址：{args.get('book_url')}",
    f"👤 帳號：{args.get('username')}",
    f"🕒 搶票時間：{args.get('target_time_str')}",
    f"💰 類型選擇：{args.get('price_types')}",
    f"🏟️ 區域選擇：{args.get('zone_names')}",
    f"🔐 登入方式：{'自動' if args.get('login_mode') else '手動'}",
    "-" * 40
]

print("\n".join(summary))

with open("ticket_log.txt", "a", encoding="utf-8") as log:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log.write(f"[{now}] 啟動 TicketBot\n")
    for line in summary:
        log.write(line + "\n")
    log.write("\n")

bot = TicketBot(**args)
bot.run()
