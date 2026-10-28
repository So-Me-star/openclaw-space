import urllib.request
import datetime
import html
import re

URLS = ["https://www.zzu.edu.cn/"]

req = urllib.request.Request(URLS[0], headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=20) as r:
    page = r.read().decode(r.headers.get_content_charset() or "utf-8", errors="replace")

m = re.search(r"<title[^>]*>(.*?)</title>", page, re.I | re.S)
title = html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip() if m else "郑州大学官网"
now = datetime.datetime.now().astimezone().isoformat(timespec="minutes")

with open("official_notices.md", "w", encoding="utf-8") as f:
    f.write("# 郑州大学官方信息更新库\n\n")
    f.write("> 自动抓取记录仅作线索，请以官方原网页为准。\n\n")
    f.write(f"## {title}\n\n- 来源：{URLS[0]}\n- 抓取时间：{now}\n")

print("更新成功")
