import subprocess, os, sys, getpass
import requests
import ssl
from colorama import init, Fore, Back, Style
from bs4 import BeautifulSoup
ssl._create_default_https_context = ssl._create_unverified_context
def clear_screen(): 
    os.system('cls' if os.name == 'nt' else 'clear')
def display_title():
    print(r"""
                              ╭─────────██╗──██╗─█████╗─██╗██████╗──██████╗─────────╮
                              │         ╚██╗██╔╝██╔══██╗██║██╔══██╗██╔═══██╗        │
                              │          ╚███╔╝ ███████║██║██████╔╝██║   ██║        │
                              │          ██╔██╗ ██╔══██║██║██╔══██╗██║   ██║        │
                              │         ██╔╝ ██╗██║  ██║██║██████╔╝╚██████╔╝        │
                              │         ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═════╝  ╚═════╝         │""")
    print(" "*30 + "│" + " "*18 + "DISCORD - xaibone" + " "*18 + "│")
    print(" "*30 + "╰" +"─"*53 + "╯")
def get_download_path():
    username = getpass.getuser()
    download_dir = f"C:\\Users\\{username}\\AppData\\Local\\Google\\Games"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    return download_dir
def download_file(url, file_path):
    try:
        headers = {}
        response = requests.get(url, headers=headers)
        response.raise_for_status()     
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(response.text)
        return True
    except Exception as e:
        print(f"Lỗi khi tải")
        return False
def check_status(url):
    try:
        headers = {}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        status = response.text.strip().upper()
        return status == "OPEN"
    except Exception as e:
        print(f"Lỗi khi check status")
        return False
def get_status_color(status):
    if status == "OPEN":
        return "\033[92mONLINE\033[0m"
    else:
        return "\033[91mOFFLINE\033[0m"
def download_and_execute_tool(tool_url, filename):
    file_path = os.path.join(get_download_path(), filename)
    print("Đang load code...")
    if not download_file(tool_url, file_path):
        print("Không thể load code")
        input("")
        return False
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        print("Load code bị lỗi")
        input("")
        return False
    print("Load code thuận lợi!")
    print("Đang chạy code :D")
    try:
        subprocess.run([sys.executable, file_path], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Lỗi khi chạy tool")
    except Exception as e:
        print(f"Lỗi")
    return False
def show_menu():
    host_status_url = "https://raw.githubusercontent.com/XaiBoYT/Status-Golike-TOOL/refs/heads/master/open_close_host.txt"
    host_open = check_status(host_status_url)
    if not host_open:
        print("XaiBo đã đóng host - Vui lòng đợi thông báo từ hoặc hỏi xaibone nhé!")
        input("")
        return
    threads_status_url = "https://raw.githubusercontent.com/XaiBoYT/Status-Golike-TOOL/refs/heads/master/threads.txt"
    instagram_status_url = "https://raw.githubusercontent.com/XaiBoYT/Status-Golike-TOOL/refs/heads/master/instagram.txt"
    threads_open = check_status(threads_status_url)
    instagram_open = check_status(instagram_status_url)
    threads_status = get_status_color("OPEN" if threads_open else "CLOSE")
    instagram_status = get_status_color("OPEN" if instagram_open else "CLOSE")
    clear_screen()
    display_title()
    print()
    print("[!] LƯU Ý: ĐÂY SẼ LÀ KHÔNG CẦN COOKIE, NẾU BẠN SỢ BAY TÀI KHOẢN THÌ HÃY LẬP TÀI KHOẢN PHỤ TEST TRƯỚC!")
    print()
    print(f"|1] Threads   [{threads_status}]")
    print(f"|2] Instagram [{instagram_status}]")
    print("|0] Thoát")
    print()
    while True:
        choice = input("> ").strip()
        
        if choice == "0":
            break
        elif choice == "1":
            if threads_open:
                tool_url = "https://raw.githubusercontent.com/XaiBoYT/tool/refs/heads/master/file/threads-obf.py"
                download_and_execute_tool(tool_url, "threads-obf.py")
                break
            else:
                print("[!] XaiBo đã đóng Threads!")
                input("")
                show_menu()
                break
        elif choice == "2":
            if instagram_open:
                tool_url = "https://raw.githubusercontent.com/XaiBoYT/tool/refs/heads/master/file/instagram-obf.py"
                download_and_execute_tool(tool_url, "instagram-obf.py")
                break
            else:
                print("[!] XaiBo đã đóng Instagram!")
                input("")
                show_menu()
                break
        else:
            print("Lựa chọn không hợp lệ!")
def main():
    clear_screen()
    download_path = get_download_path()
    for filename in os.listdir(download_path):
        if filename.endswith(".py"):
            file_path = os.path.join(download_path, filename)
            if os.path.exists(file_path):
                os.remove(file_path)
    show_menu()
if __name__ == "__main__":
    main()
