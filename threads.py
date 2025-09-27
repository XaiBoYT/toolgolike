from curl_cffi import requests
from urllib.parse import urljoin
import os
import platform
import sys
import time
import json
import pyautogui
import webbrowser
import pyperclip
from colorama import init, Fore, Back, Style
import traceback
import threading
from datetime import datetime, timedelta
import random
import subprocess

# Khởi tạo colorama
init(autoreset=True)

# Màu sắc gradient
COLOR_TITLE = (255, 255, 0)        # Vàng
COLOR_MENU = (255, 255, 0)         # Vàng
COLOR_SUCCESS = (0, 255, 0)        # Xanh lá
COLOR_ERROR = (255, 0, 0)          # Đỏ
COLOR_WARNING = (255, 0, 255)      # Magenta
COLOR_INFO = (0, 0, 255)           # Xanh dương
COLOR_COIN = (255, 255, 0)         # Vàng
COLOR_LINK = (0, 255, 255)         # Cyan
COLOR_INPUT = (255, 255, 255)      # Trắng
COLOR_COORD = (255, 0, 255)        # Magenta
COLOR_ACCOUNT = (0, 255, 255)      # Cyan
COLOR_JOB = (0, 255, 0)            # Xanh lá
COLOR_TIMER = (255, 255, 0)        # Vàng
COLOR_ACTION = (255, 0, 255)       # Magenta
COLOR_STATS = (0, 255, 255)        # Cyan
COLOR_COMMENT = (0, 0, 255)        # Xanh dương

CONFIG_FILE = "threads.cfg"

# User agent cố định cho iPhone
USER_AGENT = "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"

def get_user_agent():
    """Trả về user agent cố định"""
    return USER_AGENT

def clear_screen():
    """Xóa màn hình console"""
    os.system('cls' if platform.system() == "Windows" else 'clear')

def gradient_text(text, start_color, end_color=None):
    """Tạo hiệu ứng gradient màu cho text từ trái sang phải"""
    # Nếu end_color không được cung cấp, sử dụng màu trắng làm end_color
    if end_color is None:
        end_color = (255, 255, 255)  # Màu trắng
    
    # Đảm bảo start_color và end_color là tuple RGB
    if isinstance(start_color, str) and start_color.startswith('#'):
        start_color = tuple(int(start_color[i:i+2], 16) for i in (1, 3, 5))
    elif isinstance(start_color, str):
        # Xử lý các màu được định nghĩa bằng tên
        color_map = {
            'COLOR_TITLE': (255, 255, 0),
            'COLOR_MENU': (255, 255, 0),
            'COLOR_SUCCESS': (0, 255, 0),
            'COLOR_ERROR': (255, 0, 0),
            'COLOR_WARNING': (255, 0, 255),
            'COLOR_INFO': (0, 0, 255),
            'COLOR_COIN': (255, 255, 0),
            'COLOR_LINK': (0, 255, 255),
            'COLOR_INPUT': (255, 255, 255),
            'COLOR_COORD': (255, 0, 255),
            'COLOR_ACCOUNT': (0, 255, 255),
            'COLOR_JOB': (0, 255, 0),
            'COLOR_TIMER': (255, 255, 0),
            'COLOR_ACTION': (255, 0, 255),
            'COLOR_STATS': (0, 255, 255),
            'COLOR_COMMENT': (0, 0, 255)
        }
        start_color = color_map.get(start_color, (255, 255, 255))
    
    if isinstance(end_color, str) and end_color.startswith('#'):
        end_color = tuple(int(end_color[i:i+2], 16) for i in (1, 3, 5))
    elif isinstance(end_color, str):
        color_map = {
            'COLOR_TITLE': (255, 255, 0),
            'COLOR_MENU': (255, 255, 0),
            'COLOR_SUCCESS': (0, 255, 0),
            'COLOR_ERROR': (255, 0, 0),
            'COLOR_WARNING': (255, 0, 255),
            'COLOR_INFO': (0, 0, 255),
            'COLOR_COIN': (255, 255, 0),
            'COLOR_LINK': (0, 255, 255),
            'COLOR_INPUT': (255, 255, 255),
            'COLOR_COORD': (255, 0, 255),
            'COLOR_ACCOUNT': (0, 255, 255),
            'COLOR_JOB': (0, 255, 0),
            'COLOR_TIMER': (255, 255, 0),
            'COLOR_ACTION': (255, 0, 255),
            'COLOR_STATS': (0, 255, 255),
            'COLOR_COMMENT': (0, 0, 255)
        }
        end_color = color_map.get(end_color, (255, 255, 255))
    
    result = ""
    steps = len(text)
    r1, g1, b1 = start_color
    r2, g2, b2 = end_color
    
    for i, char in enumerate(text):
        ratio = i / (steps - 1) if steps > 1 else 0
        r = int(r1 + (r2 - r1) * ratio)
        g = int(g1 + (g2 - g1) * ratio)
        b = int(b1 + (b2 - b1) * ratio)
        result += f"\033[38;2;{r};{g};{b}m{char}"
    
    return result + "\033[0m"  # Reset color


# Sửa các lỗi gọi hàm gradient_text trong display_title()
def display_title():
    """Hiển thị tiêu đề với ASCII art"""
    title = r"""
                                        ██╗  ██╗ █████╗ ██╗██████╗  ██████╗
                                        ╚██╗██╔╝██╔══██╗██║██╔══██╗██╔═══██╗
                                         ╚███╔╝ ███████║██║██████╔╝██║   ██║
                                         ██╔██╗ ██╔══██║██║██╔══██╗██║   ██║
                                        ██╔╝ ██╗██║  ██║██║██████╔╝╚██████╔╝
                                        ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═════╝  ╚═════╝
   """
    # Sửa các dòng này - thêm end_color
    print(gradient_text(title, COLOR_LINK, COLOR_MENU))
    print(gradient_text("│", COLOR_MENU) +
          gradient_text(" "*48 + " DISCORD -", COLOR_INFO, COLOR_INPUT) + 
          gradient_text(" xaibone", COLOR_INPUT, COLOR_INFO)+
          gradient_text(" "*52 +"│", COLOR_MENU, COLOR_ERROR))
    print(gradient_text("│" + " "*44 + " Tool ", COLOR_MENU, COLOR_ERROR) +
          gradient_text("GOLIKE ", COLOR_ERROR, COLOR_MENU) +
          gradient_text("Threads", COLOR_MENU) +
          gradient_text(" [PC]", COLOR_INPUT, COLOR_ERROR)+
          gradient_text(" "*49 +"│", COLOR_MENU, COLOR_ERROR))
    print(gradient_text("│", COLOR_MENU)+
          gradient_text(" "*118 +"│", COLOR_MENU, COLOR_ERROR))
    print(gradient_text("╰" + "─"*118 + "╯", COLOR_MENU, COLOR_ERROR))
    print("")

def load_config():
    """Đọc cấu hình từ file"""
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_config(config):
    """Lưu cấu hình vào file"""
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=4)

def get_raw_api_data(auth_token, t_param):
    """Lấy thông tin tài khoản"""
    base_url = "https://gateway.golike.net/"
    endpoint = "api/users/me"
    url = urljoin(base_url, endpoint)

    headers = {
        "Authorization": f"Bearer {auth_token.replace('Bearer ', '')}",
        "T": t_param,
        "User-Agent": get_user_agent(),
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            impersonate="chrome110",
            timeout=10
        )
        
        if response.status_code == 200:
            return response.json()
        print(gradient_text(f"❌ Lỗi API: {response.status_code} - {response.text}", COLOR_ERROR))
        return None
        
    except Exception as e:
        print(gradient_text(f"❌ Lỗi kết nối: {str(e)}", COLOR_ERROR))
        return None

def get_threads_accounts(auth_token, t_param):
    """Lấy danh sách tài khoản threads"""
    base_url = "https://gateway.golike.net/"
    endpoint = "api/threads-account"
    url = urljoin(base_url, endpoint)
    
    headers = {
        "Authorization": f"Bearer {auth_token.replace('Bearer ', '')}",
        "T": t_param,
        "User-Agent": get_user_agent(),
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            impersonate="chrome110",
            timeout=10
        )
        
        if response.status_code == 200:
            return response.json()
        print(gradient_text(f"❌ Lỗi API: {response.status_code} - {response.text}", COLOR_ERROR))
        return None
        
    except Exception as e:
        print(gradient_text(f"❌ Lỗi kết nối: {str(e)}", COLOR_ERROR))
        return None

def display_threads_accounts(accounts_data):
    """Hiển thị danh sách tài khoản threads"""
    if not accounts_data or 'data' not in accounts_data or not accounts_data['data']:
        print(gradient_text("⚠️ Không có tài khoản threads nào được tìm thấy", COLOR_WARNING))
        return None
    
    print(gradient_text("╭────────────────────────────────────╮", COLOR_INFO, COLOR_LINK))
    print(gradient_text("│" + " "*2 + "STT" + " "*2 + "│" + " "*8 + "TÊN THREADS" + " "*9 + "│", COLOR_INFO, COLOR_LINK))
    print(gradient_text("│───────│────────────────────────────│", COLOR_INFO, COLOR_LINK))
    
    for index, account in enumerate(accounts_data['data'], start=1):
         print(gradient_text("│ " + " "*2, COLOR_INFO, COLOR_LINK)+
               gradient_text(f"{str(index).ljust(4)}", COLOR_MENU)+
               gradient_text("│" + " "*8, COLOR_INFO, COLOR_LINK )+
               gradient_text(f"{str(account.get('threads_username', '')).ljust(24)}" + " ", COLOR_MENU, COLOR_ERROR))
    
    print(gradient_text("╰" + "─"*7 + "─" + "─"*28 + "╯", COLOR_INFO, COLOR_LINK))
    
    return accounts_data['data']

def select_threads_account(accounts):
    """Chọn một hoặc nhiều tài khoản threads và hỏi có ẩn tên không"""
    while True:
        try:
            print(gradient_text("\n            CHỌN TÀI KHOẢN", COLOR_SUCCESS, COLOR_COIN))
            choice = input(gradient_text("[ c> ] NHẬP SỐ THỨ TỰ TÀI KHOẢN: ", COLOR_SUCCESS)).strip().lower()
            time.sleep(0.5)
            
            if choice == 'q':
                return None
                
            # Xử lý nhiều lựa chọn
            selected_indexes = []
            choices = choice.split(',')
            
            for c in choices:
                c = c.strip()
                if not c:
                    continue
                    
                index = int(c)
                if 1 <= index <= len(accounts):
                    selected_indexes.append(index-1)
                else:
                    print(gradient_text(f"[ :< ] SỐ {index} KHÔNG HỢP LỆ!", COLOR_ERROR))
            
            if selected_indexes:
                # Loại bỏ trùng lặp và giữ nguyên thứ tự
                selected_indexes = list(dict.fromkeys(selected_indexes))
                selected_accounts = [accounts[i] for i in selected_indexes]
                
                # Hỏi có muốn ẩn tên tài khoản không
                print("")
                hide_option = input(gradient_text("[ c> ] ẨN TÊN? (NHẬP 'Y'): ", COLOR_SUCCESS)).strip().lower()
                
                # Thêm thuộc tính ẩn tên vào mỗi tài khoản được chọn
                for account in selected_accounts:
                    account['hide_name'] = (hide_option == 'y')
                
                return selected_accounts
                
            print(gradient_text(f"[ :< ] VUI LÒNG NHẬP TỪ 1 -> {len(accounts)} (HOẶC 'Q' ĐỂ THOÁT)", COLOR_WARNING))
            
        except ValueError:
            print("")
            print(gradient_text("[ :< ] SỐ BẠN VỪA NHẬP KHÔNG HỢP LỆ!", COLOR_WARNING))

def get_job_delay():
    """Nhập thời gian delay cho mỗi job, hỗ trợ random với định dạng min,max"""
    while True:
        delay_input = input(gradient_text(f"\n[ :> ] NHẬP DELAY (ENTER để mặc định 10s) => ", COLOR_INFO, COLOR_LINK)).strip()
        
        # Xử lý trường hợp Enter (mặc định)
        if not delay_input:
            delay = 10
            is_random = False
            break
        
        # Xử lý trường hợp random với định dạng min,max
        if ',' in delay_input:
            try:
                parts = delay_input.split(',')
                if len(parts) != 2:
                    raise ValueError
                
                min_delay = int(parts[0].strip())
                max_delay = int(parts[1].strip())
                
                if min_delay <= 0 or max_delay <= 0:
                    print(gradient_text("[ :< ] THỜI GIAN PHẢI LỚN HƠN 0!", COLOR_WARNING))
                    continue
                
                if min_delay > max_delay:
                    min_delay, max_delay = max_delay, min_delay
                
                delay = f"{min_delay},{max_delay}"
                is_random = True
                break
                
            except ValueError:
                print(gradient_text("[ :< ] ĐỊNH DẠNG KHÔNG HỢP LỆ!", COLOR_WARNING))
                continue
        
        # Xử lý trường hợp số cố định
        else:
            try:
                delay = int(delay_input)
                if delay <= 0:
                    print(gradient_text("[ :< ] THỜI GIAN PHẢI LỚN HƠN 0!", COLOR_WARNING))
                    continue
                is_random = False
                break
            except ValueError:
                print(gradient_text("[ :< ] VUI LÒNG NHẬP SỐ NGUYÊN DƯƠNG HOẶC MIN,MAX!", COLOR_WARNING))
                continue
    
    # Hiển thị thông báo xác nhận
    time.sleep(1.5)
    if is_random:
        min_d, max_d = map(int, delay.split(','))
        print(gradient_text(f"\n[ :> ] ĐÃ ĐẶT THỜI GIAN DELAY RANDOM: {min_d}s - {max_d}s", COLOR_SUCCESS))
    else:
        print(gradient_text(f"\n[ :> ] ĐÃ ĐẶT THỜI GIAN DELAY LÀ {delay}s", COLOR_SUCCESS))
    
    time.sleep(1.5)
    print("")
    print(gradient_text("[ ! ] ĐANG CHUẨN BỊ BẮT ĐẦU TRONG 3s NỮA...", COLOR_SUCCESS, COLOR_MENU))
    time.sleep(3.5)
    
    return delay


def get_threads_jobs(auth_token, t_param, account_id):
    """Lấy job threads hiện tại"""
    base_url = "https://gateway.golike.net/"
    endpoint = "api/advertising/publishers/threads/jobs"
    url = urljoin(base_url, endpoint)
    
    headers = {
        "Authorization": f"Bearer {auth_token.replace('Bearer ', '')}",
        "T": t_param,
        "User-Agent": get_user_agent(),
        "Content-Type": "application/json;charset=utf-8",
        "Accept": "application/json, text/plain, */*",
        "sec-ch-ua": '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "Referer": ""
    }

    params = {
        "account_id": account_id,
        "data": "null",
        "_": int(time.time() * 1000)
    }
    
    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            impersonate="chrome110",
            timeout=10
        )
        
        if response.status_code == 200:
            job_data = response.json()
            if isinstance(job_data, dict) and job_data.get('data'):
                data = job_data['data']
                return {
                    'id': str(data.get('id', '')),
                    'type': data.get('type', ''),
                    'coin': int(data.get('coin', 0)),
                    'price_per_after_cost': int(data.get('price_per_after_cost', 0)),
                    'link': data.get('link', ''),
                    'created_at': data.get('created_at', ''),
                    'object_id': data.get('object_id', ''),
                    'comment_text': data.get('comment_text', '') if data.get('type') == 'comment' else None
                }
            else:
                print(gradient_text("⚠️ Không có job khả dụng hoặc định dạng dữ liệu không đúng", COLOR_WARNING))
                return None
        
        if response.status_code == 400:
            error_data = response.json()
            if error_data.get('message'):
                print(gradient_text(f"⚠️ {error_data['message']}", COLOR_WARNING))
                return "no_jobs"
        
        print(gradient_text(f"❌ [Lỗi {response.status_code}] {response.text}", COLOR_ERROR))
        return None
        
    except Exception as e:
        print(gradient_text(f"⚠️ Lỗi kết nối: {str(e)}", COLOR_ERROR))
        return None

def enhanced_complete_job(auth_token, t_param, job_id, account_id):
    """Hoàn thành job threads"""
    base_url = "https://gateway.golike.net/"
    endpoint = "api/advertising/publishers/threads/complete-jobs"
    url = urljoin(base_url, endpoint)
    
    headers = {
        "Authorization": f"Bearer {auth_token.replace('Bearer ', '')}",
        "T": t_param,
        "User-Agent": get_user_agent(),
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json, text/plain, */*",
        "sec-ch-ua": '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "Referer": ""
    }

    json_data = {
        "ads_id": int(job_id),
        "account_id": int(account_id),
        "async": True,
        "data": None
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=json_data,
            impersonate="chrome110",
            timeout=10
        )
        
        if response.status_code == 200:
            result = response.json()
            if result.get('success'):
                coin_earned = result.get('coin', 0)
                if 'data' in result and 'prices' in result['data']:
                    coin_earned = result['data']['prices']
                return True, coin_earned
            else:
                error_msg = result.get('message', 'Không có thông báo lỗi')
                print(gradient_text(f"⚠️ Lỗi từ server: {error_msg}", COLOR_WARNING))
                return False, 0
        
        print(gradient_text(f"❌ Lỗi {response.status_code}: {response.text}", COLOR_ERROR))
        return False, 0
        
    except Exception as e:
        print(gradient_text(f"⚠️ Lỗi kết nối: {str(e)}", COLOR_ERROR))

def skip_threads_job(auth_token, t_param, job_id, account_id, job_type, object_id=None):
    """Bỏ qua job hiện tại"""
    base_url = "https://gateway.golike.net/"
    endpoint = "api/advertising/publishers/threads/skip-jobs"
    url = urljoin(base_url, endpoint)
    
    headers = {
        "Authorization": f"Bearer {auth_token.replace('Bearer ', '')}",
        "T": t_param,
        "User-Agent": get_user_agent(),
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json, text/plain, */*",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "Referer": ""
    }

    json_data = {
        "ads_id": int(job_id),
        "account_id": int(account_id),
        "type": job_type
    }
    
    if object_id and job_type in ['follow', 'like', 'comment', 'share']:
        json_data["object_id"] = object_id

    try:
        response = requests.post(
            url,
            headers=headers,
            json=json_data,
            impersonate="chrome110",
            timeout=8
        )
        
        if response.status_code == 200:
            result = response.json()
            if result.get('success'):
                print(gradient_text("✅ SKIP JOB THÀNH CÔNG!", COLOR_SUCCESS))
                return True
            else:
                print(gradient_text(f"⚠️ Không thể bỏ qua job: {result.get('message', 'Không rõ lý do')}", COLOR_WARNING))
                return False
        
        print(gradient_text(f"❌ Lỗi khi bỏ qua job {response.status_code}: {response.text}", COLOR_ERROR))
        return False
        
    except Exception as e:
        print(gradient_text(f"⚠️ Lỗi kết nối: {str(e)}", COLOR_ERROR))
        return False

def perform_job_action(job, job_delay):
    """Thực hiện job với hiển thị countdown liên tục - chỉ cần chờ delay"""
    try:
        if not job or not isinstance(job, dict) or 'type' not in job:
            return False
            
        total_time = job_delay
        start_time = time.time()
        job_type = job.get('type', 'unknown')
        remaining_time = total_time
        
        # Chờ thời gian còn lại
        while remaining_time > 0:
            time.sleep(1)
            remaining_time -= 1
        
        return True
        
    except Exception as e:
        return False

def process_jobs(auth_token, t_param, account, initial_coin, job_delay):
    """Xử lý jobs cho một tài khoản với giao diện tương tự multi-account"""
    account_id = account.get('id', '')
    account_name = account.get('threads_username', '')
    account_number = ''.join(filter(str.isdigit, account_name)) or "01"
    
    # Xác định tên hiển thị
    display_name = "[ĐÃ ẨN]" if account.get('hide_name') else account_name
    
    # Biến để theo dõi trạng thái
    current_coin = initial_coin
    total_earned = 0
    consecutive_errors = 0
    consecutive_job_errors = 0  # Đếm số lần get job lỗi liên tiếp
    job_count = 0
    running = True
    
    # Kiểm tra nếu job_delay là random (chuỗi "min,max")
    is_random_delay = isinstance(job_delay, str) and ',' in job_delay
    
    # Thread kiểm tra phím Enter
    def check_for_stop():
        nonlocal running
        input()
        running = False
    
    stop_thread = threading.Thread(target=check_for_stop)
    stop_thread.daemon = True
    stop_thread.start()
    
    # Hiển thị thông báo bắt đầu
    print(gradient_text("╭" + "─"*60 + "╮", COLOR_SUCCESS, COLOR_COIN))
    print(gradient_text("│" + " "*24 + "BẮT ĐẦU XỬ LÝ" + " "*23 + "│", COLOR_SUCCESS, COLOR_COIN))
    print(gradient_text("│" + f" TÀI KHOẢN: {display_name} - DELAY: {job_delay}s ".center(60) + "│", COLOR_SUCCESS, COLOR_COIN))
    print(gradient_text("╰" + "─"*60 + "╯", COLOR_SUCCESS, COLOR_COIN))
    
    while running and consecutive_job_errors < 9:
        try:
            # Tìm job mới
            delay_time = random.randint(5, 10)
            print(gradient_text(f"[ {account_number} ] {display_name} | ĐANG TÌM JOB MỚI - CHỜ {delay_time}s", COLOR_ACTION, COLOR_LINK), end='\r')
            time.sleep(delay_time)
            print(' ' * 80, end='\r')
            
            job = get_threads_jobs(auth_token, t_param, account_id)
            
            # Kiểm tra nếu không có job
            if job == "no_jobs":
                consecutive_job_errors += 1
                print(gradient_text(f"[ {account_number} ] {display_name} | KHÔNG CÓ JOB ({consecutive_job_errors}/9)", COLOR_WARNING))
                
                # Kiểm tra nếu đạt 9 lỗi liên tiếp
                if consecutive_job_errors >= 9:
                    print(gradient_text(f"[ {account_number} ] {display_name} | ĐẠT 9 LẦN LỖI LIÊN TIẾP, TỰ ĐỘNG DỪNG", COLOR_ERROR))
                    break
                
                # Nếu 3 lỗi liên tiếp, ngủ 1 phút
                if consecutive_job_errors % 3 == 0:
                    sleep_time = 60  # 1 phút
                    print(gradient_text(f"[ {account_number} ] {display_name} | 3 LẦN LỖI LIÊN TIẾP, NGỦ {sleep_time}s", COLOR_ERROR))
                    for i in range(sleep_time, 0, -1):
                        if not running:
                            break
                        print(gradient_text(f"[ {account_number} ] {display_name} | ĐANG NGỦ {i}s ", COLOR_ERROR, COLOR_MENU), end='\r')
                        time.sleep(1)
                    print(' ' * 50, end='\r')
                else:
                    # Chờ 10s như bình thường
                    for i in range(10, 0, -1):
                        if not running:
                            break
                        print(gradient_text(f"[ {account_number} ] {display_name} | CHỜ {i}s...", COLOR_ERROR), end='\r')
                        time.sleep(1)
                    print(' ' * 80, end='\r')
                continue
            
            # Kiểm tra job hợp lệ
            if not job or not isinstance(job, dict) or 'type' not in job:
                print(gradient_text(f"[ {account_number} ] {display_name} | JOB KHÔNG HỢP LỆ", COLOR_ERROR))
                consecutive_errors += 1
                consecutive_job_errors += 1
                
                if consecutive_errors >= 5:
                    print(gradient_text(f"[ {account_number} ] {display_name} | 5 LỖI LIÊN TIẾP, TỰ ĐỘNG DỪNG", COLOR_ERROR))
                    running = False
                
                if consecutive_job_errors >= 9:
                    print(gradient_text(f"[ {account_number} ] {display_name} | ĐẠT 9 LẦN LỖI LIÊN TIẾP, TỰ ĐỘNG DỪNG", COLOR_ERROR))
                    break
                    
                continue
            
            # Reset biến đếm lỗi nếu có job hợp lệ
            consecutive_errors = 0
            consecutive_job_errors = 0
            
            # Tính toán thời gian delay cho job này
            if is_random_delay:
                min_d, max_d = map(int, job_delay.split(','))
                current_delay = random.randint(min_d, max_d)
            else:
                current_delay = job_delay
            
            # Hiển thị job
            job_count += 1
            job_type = job.get('type', 'unknown')
            job_reward = job.get('price_per_after_cost', 0)
            
            # Hiển thị thông tin job (đã bỏ link)
            print(gradient_text(f"[ {job_count:02d} ] ", COLOR_MENU, COLOR_ERROR)+
                  gradient_text(f"{display_name} ", COLOR_ACTION, COLOR_ERROR)+
                  gradient_text(f"| ", COLOR_INPUT)+
                  gradient_text(f"+{job_reward}đ ", COLOR_COIN)+
                  gradient_text(f"| ", COLOR_INPUT)+
                  gradient_text(f"{job_type.upper()}", COLOR_LINK, COLOR_INFO))
            
            # Chờ thời gian delay
            for remaining in range(current_delay, 0, -1):
                print(gradient_text(f"[ {job_count:02d} ] CHỜ {remaining:2d}s! ", COLOR_ACTION, COLOR_LINK), end='\r')
                time.sleep(1)
            print(' ' * 50, end='\r')  # Xóa dòng đếm ngược
            
            # Hoàn thành job
            max_attempts = 2
            attempts = 0
            success = False
            earned = 0
            
            while attempts < max_attempts and not success and running:
                attempts += 1
                success, earned = enhanced_complete_job(auth_token, t_param, job['id'], account_id)
                
                if success:
                    total_earned += earned
                    current_coin += earned
                    print(gradient_text(f"[ {job_count:02d} ] ", COLOR_SUCCESS)+
                          gradient_text(f"{display_name} ", COLOR_SUCCESS, COLOR_MENU)+
                          gradient_text(f"| ", COLOR_INPUT)+
                          gradient_text(f"SUCCESS ", COLOR_SUCCESS)+
                          gradient_text(f"| ", COLOR_INPUT)+
                          gradient_text(f"+{earned}đ ", COLOR_COIN)+
                          gradient_text(f"| ", COLOR_INPUT)+
                          gradient_text(f"TỔNG TIỀN: {total_earned}đ ", COLOR_MENU, COLOR_SUCCESS))
                    time.sleep(1.5)
                elif attempts < max_attempts:
                    print(gradient_text(f"[ {job_count:02d} ] {display_name} | LỖI, THỬ LẠI SAU 2s...", COLOR_ERROR))
                    time.sleep(2)
            
            if not success:
                print(gradient_text(f"[ {job_count:02d} ] {display_name} | KHÔNG THỂ HOÀN THÀNH, ĐANG SKIP...", COLOR_ERROR))
                skip_threads_job(auth_token, t_param, job['id'], account_id, job['type'], job.get('object_id'))
            
            # Chờ trước khi lấy job tiếp theo
            for i in range(4, 0, -1):
                print(gradient_text(f"[ {job_count:02d} ] {display_name} | CHỜ {i}s ĐỂ LẤY JOB MỚI", COLOR_ACTION, COLOR_INFO), end='\r')
                time.sleep(1)
            print(' ' * 80, end='\r')
            
        except KeyboardInterrupt:
            print(gradient_text(f"[ {job_count:02d} ] {display_name} | ĐÃ DỪNG TOOL", COLOR_ERROR, COLOR_INFO))
            running = False
        except Exception as e:
            print(gradient_text(f"[ {job_count:02d} ] {display_name} | LỖI: {str(e)}", COLOR_ERROR))
            consecutive_errors += 1
            consecutive_job_errors += 1
            
            if consecutive_errors >= 5:
                print(gradient_text(f"[ {job_count:02d} ] {display_name} | 5 LỖI LIÊN TIẾP, TỰ ĐỘNG DỪNG", COLOR_ERROR))
                running = False
            
            if consecutive_job_errors >= 9:
                print(gradient_text(f"[ {job_count:02d} ] {display_name} | ĐẠT 9 LẦN LỖI LIÊN TIẾP, TỰ ĐỘNG DỪNG", COLOR_ERROR))
                break
                
            time.sleep(3)
    
    if consecutive_job_errors >= 9:
        print(gradient_text(f"[ {job_count:02d} ] {display_name} | ĐÃ DỪNG DO 9 LẦN GET JOB LỖI LIÊN TIẾP", COLOR_ERROR))
    else:
        print(gradient_text(f"[ {job_count:02d} ] {display_name} | ĐÃ DỪNG TOOL", COLOR_ERROR))
    
    print(gradient_text("NHẤN ENTER ĐỂ THOÁT...", COLOR_ERROR))

def process_jobs_multiple_accounts(auth_token, t_param, accounts, initial_coins, job_delay):
    """Xử lý jobs cho nhiều tài khoản với độ trễ 1.7s giữa các tài khoản"""
    
    # Biến để theo dõi trạng thái
    running = True
    account_status = {}
    total_earned_all_accounts = 0
    global_job_count = 0  # Biến đếm số job chung cho tất cả tài khoản
    
    # Khởi tạo trạng thái cho từng tài khoản
    for account in accounts:
        account_id = account.get('id', '')
        account_name = account.get('threads_username', '')
        display_name = "[ĐÃ ẨN]" if account.get('hide_name') else account_name
        
        account_status[account_id] = {
            'current_coin': initial_coins.get(account_id, 0),
            'total_earned': 0,
            'consecutive_errors': 0,
            'consecutive_job_errors': 0,  # Đếm số lần get job lỗi liên tiếp
            'job_count': 0,
            'name': account_name,
            'display_name': display_name,  # Thêm display_name
            'active': True,  # Trạng thái hoạt động của tài khoản
            'current_job_number': 0  # Số thứ tự job hiện tại của tài khoản
        }
    
    # Thread kiểm tra phím Enter để dừng
    def check_for_stop():
        nonlocal running
        input()
        running = False
    
    stop_thread = threading.Thread(target=check_for_stop)
    stop_thread.daemon = True
    stop_thread.start()
    
    # Hiển thị thông báo bắt đầu
    print(gradient_text("╭" + "─"*60 + "╮", COLOR_SUCCESS, COLOR_COIN))
    print(gradient_text("│" + " "*24 + "BẮT ĐẦU XỬ LÝ" + " "*23 + "│", COLOR_SUCCESS, COLOR_COIN))
    print(gradient_text("│" + f" SỐ TÀI KHOẢN: {len(accounts)} - DELAY: {job_delay}s ".center(60) + "│", COLOR_SUCCESS, COLOR_COIN))
    print(gradient_text("╰" + "─"*60 + "╯", COLOR_SUCCESS, COLOR_COIN))

    
    # Hàm xử lý job cho một tài khoản
    def process_single_job(account):
        nonlocal global_job_count, total_earned_all_accounts
        account_id = account.get('id', '')
        status = account_status[account_id]
        account_name = status['name']
        display_name = status['display_name']  # Sử dụng display_name
        
        try:
            # Lấy job
            job = get_threads_jobs(auth_token, t_param, account_id)
            
            # Kiểm tra nếu không có job
            if job == "no_jobs":
                return False, "no_jobs"
            
            # Kiểm tra job hợp lệ
            if not job or not isinstance(job, dict) or 'type' not in job:
                return False, "invalid_job"
            
            # Kiểm tra nếu job type là comment thì skip ngay
            if job.get('type') == 'comment':
                print(gradient_text(f"[ {global_job_count + 1:02d} ] {display_name} | ĐANG SKIP COMMENT JOB...", COLOR_ERROR, COLOR_WARNING))
                skip_threads_job(auth_token, t_param, job['id'], account_id, job['type'], job.get('object_id'))
                return False, "skip_comment"
            
            # Reset bộ đếm lỗi get job nếu thành công
            status['consecutive_job_errors'] = 0
            
            # Tính toán thời gian delay
            is_random_delay = isinstance(job_delay, str) and ',' in job_delay
            if is_random_delay:
                min_d, max_d = map(int, job_delay.split(','))
                current_delay = random.randint(min_d, max_d)
            else:
                current_delay = job_delay
            
            # Tăng số job
            global_job_count += 1
            status['job_count'] += 1
            
            # Hiển thị job
            job_type = job.get('type', 'unknown')
            job_reward = job.get('price_per_after_cost', 0)
            
            # Hiển thị thông tin job (đã bỏ link)
            print(gradient_text(f"[ {global_job_count:02d} ] ", COLOR_MENU, COLOR_ERROR)+
                  gradient_text(f"{display_name} ", COLOR_ACTION, COLOR_ERROR)+
                  gradient_text(f"| ", COLOR_INPUT)+
                  gradient_text(f"+{job_reward}đ ", COLOR_COIN)+
                  gradient_text(f"| ", COLOR_INPUT)+
                  gradient_text(f"{job_type.upper()}", COLOR_LINK, COLOR_INFO))
            
            # Chờ thời gian delay
            for remaining in range(current_delay, 0, -1):
                print(gradient_text(f"[ {global_job_count:02d} ] CHỜ {remaining:2d}s! ", COLOR_ACTION, COLOR_LINK), end='\r')
                time.sleep(1)
            print(' ' * 50, end='\r')  # Xóa dòng đếm ngược
            
            # Hoàn thành job
            max_attempts = 2
            attempts = 0
            success = False
            earned = 0
            
            while attempts < max_attempts and not success:
                attempts += 1
                success, earned = enhanced_complete_job(auth_token, t_param, job['id'], account_id)
                
                if success:
                    status['total_earned'] += earned
                    total_earned_all_accounts += earned
                    status['current_coin'] += earned
                    print(gradient_text(f"[ {global_job_count:02d} ] ", COLOR_SUCCESS)+
                          gradient_text(f"{display_name} ", COLOR_SUCCESS, COLOR_MENU)+
                          gradient_text(f"| ", COLOR_INPUT)+
                          gradient_text(f"SUCCESS ", COLOR_SUCCESS)+
                          gradient_text(f"| ", COLOR_INPUT)+
                          gradient_text(f"+{earned}đ ", COLOR_COIN)+
                          gradient_text(f"| ", COLOR_INPUT)+
                          gradient_text(f"TỔNG TIỀN: {total_earned_all_accounts}đ ", COLOR_MENU, COLOR_SUCCESS))
                    
                    time.sleep(1.5)
                elif attempts < max_attempts:
                    print(gradient_text(f"[ {global_job_count:02d} ] {display_name} | LỖI, THỬ LẠI SAU 2s...", COLOR_ERROR))
                    time.sleep(2)
            
            if not success:
                print(gradient_text(f"[ {global_job_count:02d} ] {display_name} | KHÔNG THỂ HOÀN THÀNH, ĐANG SKIP...", COLOR_ERROR))
                skip_threads_job(auth_token, t_param, job['id'], account_id, job['type'], job.get('object_id'))
                return False, "skip_failed"
            
            return True, "success"
            
        except Exception as e:
            return False, f"error: {str(e)}"
    
    # Vòng lặp chính cho nhiều tài khoản
    while running:
        # Kiểm tra xem còn tài khoản nào hoạt động không
        active_accounts = [acc for acc in accounts if account_status[acc['id']]['active']]
        if not active_accounts:
            print(gradient_text("TẤT CẢ TÀI KHOẢN ĐÃ DỪNG HOẠT ĐỘNG", COLOR_ERROR, COLOR_INFO))
            break
        
        # Xử lý từng tài khoản với độ trễ 1.7s
        for account in active_accounts:
            if not running:
                break
                
            account_id = account.get('id', '')
            status = account_status[account_id]
            account_name = status['name']
            display_name = status['display_name']  # Sử dụng display_name
            
            # Kiểm tra nếu tài khoản đã đạt 9 lỗi get job liên tiếp
            if status['consecutive_job_errors'] >= 9:
                print(gradient_text(f"[ {global_job_count + 1:02d} ] {display_name} | ĐẠT 9 LẦN LỖI LIÊN TIẾP, TỰ ĐỘNG DỪNG", COLOR_ERROR))
                status['active'] = False
                continue
            
            # Tìm job mới
            delay_time = random.randint(5, 10)
            print(gradient_text(f"[ {global_job_count + 1:02d} ] {display_name} | ĐANG TÌM JOB MỚI - CHỜ {delay_time}s", COLOR_ACTION, COLOR_LINK), end='\r')
            time.sleep(delay_time)
            print(' ' * 80, end='\r')
            
            # Xử lý job
            success, result = process_single_job(account)
            
            # Xử lý kết quả
            if success:
                status['consecutive_errors'] = 0
            else:
                if result == "no_jobs":
                    status['consecutive_job_errors'] += 1
                    print(gradient_text(f"[ {global_job_count + 1:02d} ] {display_name} | KHÔNG CÓ JOB ({status['consecutive_job_errors']}/9)", COLOR_ERROR, COLOR_MENU))
                    
                    # Kiểm tra nếu đạt 9 lỗi liên tiếp
                    if status['consecutive_job_errors'] >= 9:
                        print(gradient_text(f"[ {global_job_count + 1:02d} ] {display_name} | ĐẠT 9 LẦN LỖI LIÊN TIẾP, TỰ ĐỘNG DỪNG", COLOR_ERROR))
                        status['active'] = False
                        continue
                    
                    # Nếu 3 lỗi liên tiếp, ngủ 1 phút
                    if status['consecutive_job_errors'] % 3 == 0:
                        sleep_time = 60  # 1 phút
                        print(gradient_text(f"[ {global_job_count + 1:02d} ] {display_name} | 3 LẦN LỖI LIÊN TIẾP, NGỦ {sleep_time}s", COLOR_ERROR, COLOR_SUCCESS))
                        for i in range(sleep_time, 0, -1):
                            if not running:
                                break
                            print(gradient_text(f"[ {global_job_count + 1:02d} ] {display_name} | ĐANG NGỦ {i}s ", COLOR_ERROR), end='\r')
                            time.sleep(1)
                        print(' ' * 50, end='\r')
                    else:
                        # Chờ 10s như bình thường
                        for i in range(10, 0, -1):
                            if not running:
                                break
                            print(gradient_text(f"[ {global_job_count + 1:02d} ] {display_name} | CHỜ {i}s...", COLOR_ACTION, COLOR_INFO), end='\r')
                            time.sleep(1)
                        print(' ' * 80, end='\r')
                
                elif result == "skip_comment":
                    # Job comment đã được skip, không tính là lỗi
                    pass
                
                else:
                    status['consecutive_errors'] += 1
                    status['consecutive_job_errors'] += 1
                    
                    if status['consecutive_errors'] >= 5:
                        print(gradient_text(f"[ {global_job_count + 1:02d} ] {display_name} | 5 LỖI LIÊN TIẾP, TỰ ĐỘNG DỪNG", COLOR_ERROR))
                        status['active'] = False
                    
                    if status['consecutive_job_errors'] >= 9:
                        print(gradient_text(f"[ {global_job_count + 1:02d} ] {display_name} | ĐẠT 9 LẦN LỖI LIÊN TIẾP, TỰ ĐỘNG DỪNG", COLOR_ERROR))
                        status['active'] = False
            
            # Chờ 1.7s trước khi xử lý tài khoản tiếp theo
            if running:
                time.sleep(1.7)

def main():
    """Hàm chính của chương trình"""
    config = load_config()
    
    while True:
        try:
            clear_screen()
            display_title()
            
            # Kiểm tra và yêu cầu nhập auth_token nếu chưa có
            auth_token = config.get('auth_token', '').strip()
            if not auth_token:
                print(gradient_text("[ :> ] NHẬP AUTH TOKEN CỦA BẠN: ", COLOR_ACTION, COLOR_INFO))
                auth_token = input().strip()
                if not auth_token:
                    print(gradient_text("[ :< ] AUTH TOKEN KHÔNG ĐƯỢC ĐỂ TRỐNG!", COLOR_ERROR))
                    time.sleep(2)
                    continue
                config['auth_token'] = auth_token
                save_config(config)
            
            # Kiểm tra và yêu cầu nhập T parameter nếu chưa có
            t_param = config.get('t_param', '').strip()
            if not t_param:
                print(gradient_text("[ :> ] NHẬP T PARAM CỦA BẠN: ", COLOR_ACTION, COLOR_INFO))
                t_param = input().strip()
                if not t_param:
                    print(gradient_text("[ :< ] T PARAM KHÔNG ĐƯỢC ĐỂ TRỐNG!", COLOR_ERROR))
                    time.sleep(2)
                    continue
                config['t_param'] = t_param
                save_config(config)
            
            # Lấy thông tin tài khoản
            print(gradient_text("\n[ :> ] ĐANG LẤY THÔNG TIN TÀI KHOẢN...", COLOR_MENU, COLOR_ERROR))
            account_data = get_raw_api_data(auth_token, t_param)
            
            if not account_data or 'data' not in account_data:
                print(gradient_text("[ :< ] KHÔNG THỂ LẤY THÔNG TIN TÀI KHOẢN!", COLOR_ERROR))
                time.sleep(2)
                continue
            
            user_data = account_data['data']
            user_name = user_data.get('name', '')
            user_email = user_data.get('email', '')
            user_coin = user_data.get('coin', 0)
            
            # Hiển thị thông tin tài khoản (SỬA LỖI Ở ĐÂY)
            print(gradient_text("╭────────────────────────────────────╮", COLOR_INFO, COLOR_LINK))
            print(gradient_text("│" + " "*14 + "TÀI KHOẢN" + " "*13 + "│", COLOR_INFO, COLOR_LINK))
            print(gradient_text("│─────────────────────────────────────", COLOR_INFO, COLOR_LINK))
            print("")
            print(gradient_text("          TÀI KHOẢN: ", COLOR_INFO, COLOR_LINK)+
                  gradient_text(f"{user_name}", COLOR_MENU, COLOR_ERROR))
            print(gradient_text("          SỐ DƯ: ", COLOR_INFO, COLOR_LINK)+
                  gradient_text(f"{user_coin} VNĐ", COLOR_COIN, COLOR_SUCCESS))
            print("")
            print(gradient_text("╰────────────────────────────────────╯", COLOR_INFO, COLOR_LINK))
            
            # Lấy danh sách tài khoản threads
            print(gradient_text("\n[ :> ] ĐANG LẤY DANH SÁCH TÀI KHOẢN THREADS...", COLOR_MENU, COLOR_ERROR))
            accounts_data = get_threads_accounts(auth_token, t_param)
            
            if not accounts_data:
                print(gradient_text("[ :< ] KHÔNG THỂ LẤY DANH SÁCH TÀI KHOẢN THREADS!", COLOR_ERROR))
                time.sleep(2)
                continue
            
            # Hiển thị danh sách tài khoản threads
            accounts = display_threads_accounts(accounts_data)
            if not accounts:
                print(gradient_text("[ :< ] KHÔNG CÓ TÀI KHOẢN THREADS NÀO ĐỂ LÀM VIỆC!", COLOR_ERROR))
                time.sleep(2)
                continue
            
            # Chọn tài khoản threads
            selected_accounts = select_threads_account(accounts)
            if not selected_accounts:
                continue
            
            # Nhập thời gian delay
            job_delay = get_job_delay()
            
            # Lấy số dư ban đầu cho từng tài khoản
            initial_coins = {}
            for account in selected_accounts:
                initial_coins[account['id']] = user_coin  # Sử dụng số dư chung cho tất cả tài khoản
            
            # Xử lý jobs cho các tài khoản đã chọn
            clear_screen()
            display_title()
            if len(selected_accounts) == 1:
                process_jobs(auth_token, t_param, selected_accounts[0], user_coin, job_delay)
            else:
                process_jobs_multiple_accounts(auth_token, t_param, selected_accounts, initial_coins, job_delay)
            
            break
            
        except KeyboardInterrupt:
            print(gradient_text("\n[ :< ] ĐÃ DỪNG CHƯƠNG TRÌNH!", COLOR_WARNING))
            break
        except Exception as e:
            print(gradient_text(f"[ :< ] LỖI: {str(e)}", COLOR_ERROR))
            traceback.print_exc()
            time.sleep(3)

if __name__ == "__main__":
    main()
