import os
import zipfile
import rarfile
import py7zr
rarfile.UNRAR_TOOL = r"C:\Program Files\WinRAR\UnRAR.exe"
def extract_file(file_path, target_path):
    os.makedirs(target_path, exist_ok=True)

    if file_path.lower().endswith(".zip"):
        with zipfile.ZipFile(file_path, 'r') as zf:
            zf.extractall(target_path)
    elif file_path.lower().endswith(".rar"):
        with rarfile.RarFile(file_path, 'r') as rf:
            rf.extractall(target_path)
    elif file_path.lower().endswith(".7z"):
        with py7zr.SevenZipFile(file_path, mode='r') as sz:
            sz.extractall(path=target_path)
def extract_archives(src_folder: str, dst_folder: str):
    os.makedirs(dst_folder, exist_ok=True)
    extensions = (".zip", ".rar", ".7z")

    for root, dirs, files in os.walk(src_folder):
        for file in files:
            if file.lower().endswith(extensions):
                archive_path = os.path.join(root, file)
                rel_path = os.path.relpath(root, src_folder)
                target_path = os.path.join(dst_folder, rel_path)  # 🚀 不再加壓縮檔名

                print(f"解壓縮 {archive_path} -> {target_path}")
                try:
                    extract_file(archive_path, target_path)
                except Exception as e:
                    print(f"解壓縮失敗: {archive_path}, 錯誤: {e}")

if __name__ == "__main__":
    source = r"D:\coding\ownDCio\2025FallEvent\請上傳你的作品_所有檔案以壓縮後打包為主，圖片需要以001,002...形式為檔名，其餘的繳交形式以一個檔案為限 (File responses)-20250920T022815Z-1-001\File responses"
    dest   = r"D:\coding\ownDCio\2025FallEvent\pieces"
    extract_archives(source, dest)
