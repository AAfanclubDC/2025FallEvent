import json
from collections import defaultdict
import os

# 輸入原始資料
with open("繳交情況2.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 分組暫存
groups = defaultdict(list)

for item in data:
    group = item.get("你的組別是?")
    title = item.get("Title")
    order = item.get("作品在組內順位(1最先)")
    id_num = item.get("ID")

    # src: 用 ID 來決定圖片名稱 (補零到兩位數)
    src = f"images/players/{id_num:02d}.png"

    # url: 直接用 Title 當檔名
    url = f"pieces/{title}.html"

    groups[group].append({
        "src": src,
        "title": title,
        "url": url,
        "order": order
    })

# 依組別輸出，並依照 order 排序
for group, items in groups.items():
    items_sorted = sorted(items, key=lambda x: (x["order"] if x["order"] is not None else float("inf")))

    filename = f"data/output{group}.json"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(items_sorted, f, ensure_ascii=False, indent=4)

    print(f"✅ {filename} 已產生，共 {len(items_sorted)} 筆資料，已依照 order 排序")

