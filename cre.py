import json
import os,sys

# 讀取 JSON 文件
with open('繳交情況2.json', 'r', encoding='utf-8') as file:
    datas = json.load(file)

with open('template.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# 初始化輸出列表

for data in datas:
    tmp_Html = html_content.replace("123標題預留位321", data["Title"]) 
    image_folder = f"pieces/{data['Title']}"
    print(image_folder)
    print(data['Title'])
    try:
        image_files = os.listdir(image_folder)
    except:
        print(image_folder)
        input()
        continue
    
    image_tags = ''
    folder = f"pieces/{data['Title']}"
    if os.path.exists(folder):
        files = sorted(os.listdir(folder))  # 取得實際檔案清單
        for idx, fname in enumerate(files, start=1):  # 001 從 1 開始
            ext = os.path.splitext(fname)[1]  # 取得副檔名 (包含 .)
            image_path = f"{data['Title']}/{idx:03}{ext}"
            image_tags += f'<img src="{image_path}" alt=""><br>\n'
    else:
        print(f"⚠ 資料夾 {folder} 不存在")
    
    # 替換圖片預留位
    tmp_Html = tmp_Html.replace("456圖片預留位654", image_tags)
    print(data['Title'])
    # 將結果寫入新的 HTML 文件
    with open(f'作品/{data["Title"]}.html', 'w', encoding='utf-8') as file:
        file.write(tmp_Html)