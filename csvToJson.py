import pandas as pd
import os
# 定義一個函數來計算資料夾中檔案的數量
def count_files_in_folder(folder_name):
    folder_path = os.path.join('2025FallEvent\pieces', folder_name)
    try:
        return len([name for name in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, name))])+1
    except FileNotFoundError:
        return 0  # 如果找不到資料夾，返回 0
df = pd.read_csv (r'2025 秋活 (回覆) - 表單回應 1.csv',encoding="utf-8")
print(len(df))
# 確保 Time 欄位是 datetime 格式
df['Time'] = df['Time'].str.replace('下午', 'PM').str.replace('上午', 'AM')
df['Time'] = pd.to_datetime(df['Time'], format=r'%Y/%m/%d %p %I:%M:%S', errors='coerce')

# df_filtered = df.sort_values('Time').drop_duplicates(subset=['ID'], keep='last')
# df_filtered['Time'] = df_filtered['Time'].dt.strftime('%Y-%m-%d %H:%M:%S')
# df_filtered['Page'] = 0
# df_filtered = df_filtered.sort_values(by='ID')
# 將篩選後的 DataFrame 轉換為 JSON
# df_filtered.to_json(r'繳交情況2.json', orient='records', force_ascii=False)
print(len(df))
df.to_json (r'繳交情況2.json',orient='records',force_ascii=False)