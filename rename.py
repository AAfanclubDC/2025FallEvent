import os
import re

def extract_number(filename):
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else 0

def rename_files(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    files.sort(key=extract_number)

    temp_names = []
    # 第一步：先改成暫存名稱
    for i, filename in enumerate(files, start=1):
        old_path = os.path.join(folder_path, filename)
        temp_name = f"__tmp_{i:03d}.tmp"
        temp_path = os.path.join(folder_path, temp_name)
        os.rename(old_path, temp_path)
        temp_names.append((temp_path, filename))  # 保留對應關係

    # 第二步：再改成最終名稱
    for i, (temp_path, old_name) in enumerate(temp_names, start=1):
        _, ext = os.path.splitext(old_name)
        new_name = f"{i:03d}{ext}"
        new_path = os.path.join(folder_path, new_name)
        os.rename(temp_path, new_path)
        print(f"Renamed: {old_name} -> {new_name}")

if __name__ == "__main__":
    target_folder = r"pieces\傳說新聞社-終幕"
    rename_files(target_folder)
