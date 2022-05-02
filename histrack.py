#Python version by H1rr_Snorre #Respect Bro!
#Require Requests, Colorama
import requests
from colorama import Fore, Back
from platform import system
import json
import os
import time
from hashlib import md5

print(Fore.RESET, Back.RESET)
print(Fore.WHITE, Back.BLACK)

#Set window title if it is on Windows
if system() == 'Windows': os.system('title HisTrack v1.2, Created HackPekka (htr-tech) + H1rr_Snorre')

#Clean the dirty screen
def clear_scr():
    if system() == 'Linux':
        os.system('clear')
    else: os.system('cls')

def banner():
    clear_scr()
    print(f'''
\n{Fore.RED}██╗  ██╗██╗███████╗████████╗██████╗  █████╗  ██████╗██╗  ██╗
██║  ██║██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
███████║██║███████╗   ██║   ██████╔╝███████║██║     █████╔╝
██╔══██║██║╚════██║   ██║   ██╔══██╗██╔══██║██║     ██╔═██╗
██║  ██║██║███████║   ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗
╚═╝  ╚═╝╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝\n
      {Fore.RED}Version : {Fore.WHITE}1.2 Python\n
  {Fore.RED}<{Fore.WHITE}-{Fore.RED}>{Fore.RED} Created HackPekka ({Fore.WHITE}htr-tech{Fore.RED}) + H1rr_Snorre
''')
time.sleep(1)

def menu():
    while True:
        banner()
        print(f'{Fore.RESET}')
        print(f'  {Fore.RED}<{Fore.WHITE}1{Fore.RED}> My IP')
        time.sleep(.1)
        print(f'  {Fore.RED}<{Fore.WHITE}2{Fore.RED}> Track IP')
        time.sleep(.1)
        print(f'  {Fore.RED}<{Fore.WHITE}0{Fore.RED}> Exit')
        time.sleep(.1)
        print()
        option = input(f'  {Fore.RED}<{Fore.WHITE}-{Fore.RED}> {Fore.WHITE}Select {Fore.RED}>>{Fore.LIGHTYELLOW_EX} ')
        if option == '1' or option == '01':
            myipaddr()
        elif option == '2' or option == '02':
            useripaddr()
        elif option == '0' or option == '00':
            time.sleep(1)
            print(Fore.RESET,Back.RESET)
            exit()
        else:
            print(f' {Fore.RED}[{Fore.WHITE}!{Fore.RED}] {Fore.YELLOW}Invalid option {Fore.RED}[{Fore.WHITE}!{Fore.RED}]')
            time.sleep(1)

def myipaddr():
    myipaddripapico = json.loads(requests.get("https://ipapi.co//json").content)
    myipaddripapicom = json.loads(requests.get("http://ip-api.com/json/").content)
    myip = myipaddripapico['ip']
    mycity = myipaddripapico['city']
    myregion = myipaddripapico['region']
    mycountry = myipaddripapico["country_name"]
    mylat = myipaddripapicom["lat"]
    mylon = myipaddripapicom["lon"]
    mytime = myipaddripapicom["timezone"]
    mypostal = myipaddripapicom["zip"]
    myisp = myipaddripapico["org"]
    myasn = myipaddripapico["asn"]
    mycountrycode = myipaddripapico["country_code"]
    mycurrency = myipaddripapico["currency"]
    mylanguage = myipaddripapico["languages"]
    mycalling = myipaddripapico["country_calling_code"]
    banner()
    print('\n')
    print(f'  {Fore.RED}  Ip Address    {Fore.LIGHTCYAN_EX}:{Fore.LIGHTGREEN_EX}   {myip}')
    time.sleep(.1)
    print(f'  {Fore.RED}  City          {Fore.LIGHTCYAN_EX}:{Fore.LIGHTGREEN_EX}   {mycity}')
    time.sleep(.1)
    print(f'  {Fore.RED}  Region        {Fore.LIGHTCYAN_EX}:{Fore.LIGHTGREEN_EX}   {myregion}')
    time.sleep(.1)
    print(f'  {Fore.RED}  Country       {Fore.LIGHTCYAN_EX}:{Fore.LIGHTGREEN_EX}   {mycountry}')
    print()
    print(f'  {Fore.RED}  Latitude     {Fore.LIGHTCYAN_EX}:{Fore.LIGHTGREEN_EX}    {mylat}')
    time.sleep(.1)
    print(f'  {Fore.RED}  Longitude    {Fore.LIGHTCYAN_EX}:{Fore.LIGHTGREEN_EX}    {mylon}')
    time.sleep(.1)
    print(f'  {Fore.RED}  Time Zone    {Fore.LIGHTCYAN_EX}:{Fore.LIGHTGREEN_EX}    {mytime}')
    time.sleep(.1)
    print(f'  {Fore.RED}  Postal Code  {Fore.LIGHTCYAN_EX}:{Fore.LIGHTGREEN_EX}    {mypostal}')
    print()
    time.sleep(.1)
    print(f'  {Fore.RED}  ISP           {Fore.LIGHTCYAN_EX}:{Fore.LIGHTGREEN_EX}   {myisp}')
    time.sleep(.1)
    print(f'  {Fore.RED}  ASN           {Fore.LIGHTCYAN_EX}:{Fore.LIGHTGREEN_EX}   {myasn}')
    print()
    print(f'  {Fore.RED}  Country Code  {Fore.LIGHTCYAN_EX}:{Fore.LIGHTGREEN_EX}   {mycountrycode}')
    time.sleep(.1)
    print(f'  {Fore.RED}  Currency      {Fore.LIGHTCYAN_EX}:{Fore.LIGHTGREEN_EX}   {mycurrency}')
    time.sleep(.1)
    print(f'  {Fore.RED}  Languages     {Fore.LIGHTCYAN_EX}:{Fore.LIGHTGREEN_EX}   {mylanguage}')
    time.sleep(.1)
    print(f'  {Fore.RED}  Calling Code  {Fore.LIGHTCYAN_EX}:{Fore.LIGHTGREEN_EX}   {mycalling}')
    print()
    print(f'  {Fore.RED}  GOOGLE Maps   {Fore.LIGHTCYAN_EX}:{Fore.LIGHTBLUE_EX}  https://maps.google.com/?q={mylat},{mylon}')
    time.sleep(5)
    print()
    print(f'  {Fore.RED}<{Fore.WHITE}1{Fore.RED}> Main Menu', end='')
    print(f'  {Fore.RED}<{Fore.WHITE}2{Fore.RED}> Exit')
    print()

    mainorexit1 = input(f' {Fore.RED}>> {Fore.LIGHTYELLOW_EX}')
    if mainorexit1 == '1' or mainorexit1 == '01':
        menu()
    elif mainorexit1 == '2' or mainorexit1 == '02':
        print(Fore.RESET,Back.RESET,'\n')
        exit()
    else:
        print(f'  {Fore.RED}[{Fore.WHITE}!{Fore.RED}] {Fore.YELLOW}Invalid option {Fore.RED}[{Fore.WHITE}!{Fore.RED}]')
        time.sleep(1)
        menu()

def useripaddr():
    banner()
    ip = input(f'  {Fore.RED}<{Fore.WHITE}-{Fore.RED}> Input IP Address {Fore.WHITE}:')
    myipaddripapico = json.loads(requests.get(f"https://ipapi.co/{ip}/json").content)
    myipaddripapicom = json.loads(requests.get(f"http://ip-api.com/json/{ip}").content)
    myip = myipaddripapico['ip']
    mycity = myipaddripapico['city']
    myregion = myipaddripapico['region']
    mycountry = myipaddripapico["country_name"]
    mylat = myipaddripapicom["lat"]
    mylon = myipaddripapicom["lon"]
    mytime = myipaddripapicom["timezone"]
    mypostal = myipaddripapicom["zip"]
    myisp = myipaddripapico["org"]
    myasn = myipaddripapico["asn"]
    mycountrycode = myipaddripapico["country_code"]
    mycurrency = myipaddripapico["currency"]
    mylanguage = myipaddripapico["languages"]
    mycalling = myipaddripapico["country_calling_code"]
    banner()
    print('\n')
    print(f'  {Fore.RED}  Ip Address    {Fore.LIGHTCYAN_EX}:{Fore.LIGHTGREEN_EX}   {myip}')
    time.sleep(.1)
    print(f'  {Fore.RED}  City          {Fore.LIGHTCYAN_EX}:{Fore.LIGHTGREEN_EX}   {mycity}')
    time.sleep(.1)
    print(f'  {Fore.RED}  Region        {Fore.LIGHTCYAN_EX}:{Fore.LIGHTGREEN_EX}   {myregion}')
    time.sleep(.1)
    print(f'  {Fore.RED}  Country       {Fore.LIGHTCYAN_EX}:{Fore.LIGHTGREEN_EX}   {mycountry}')
    print()
    print(f'  {Fore.RED}  Latitude      {Fore.LIGHTCYAN_EX}:{Fore.LIGHTGREEN_EX}   {mylat}')
    time.sleep(.1)
    print(f'  {Fore.RED}  Longitude     {Fore.LIGHTCYAN_EX}:{Fore.LIGHTGREEN_EX}   {mylon}')
    time.sleep(.1)
    print(f'  {Fore.RED}  Time Zone     {Fore.LIGHTCYAN_EX}:{Fore.LIGHTGREEN_EX}   {mytime}')
    time.sleep(.1)
    print(f'  {Fore.RED}  Postal Code   {Fore.LIGHTCYAN_EX}:{Fore.LIGHTGREEN_EX}   {mypostal}')
    print()
    time.sleep(.1)
    print(f'  {Fore.RED}  ISP           {Fore.LIGHTCYAN_EX}:{Fore.LIGHTGREEN_EX}   {myisp}')
    time.sleep(.1)
    print(f'  {Fore.RED}  ASN           {Fore.LIGHTCYAN_EX}:{Fore.LIGHTGREEN_EX}   {myasn}')
    print()
    print(f'  {Fore.RED}  Country Code  {Fore.LIGHTCYAN_EX}:{Fore.LIGHTGREEN_EX}   {mycountrycode}')
    time.sleep(.1)
    print(f'  {Fore.RED}  Currency      {Fore.LIGHTCYAN_EX}:{Fore.LIGHTGREEN_EX}   {mycurrency}')
    time.sleep(.1)
    print(f'  {Fore.RED}  Languages     {Fore.LIGHTCYAN_EX}:{Fore.LIGHTGREEN_EX}   {mylanguage}')
    time.sleep(.1)
    print(f'  {Fore.RED}  Calling Code  {Fore.LIGHTCYAN_EX}:{Fore.LIGHTGREEN_EX}   {mycalling}')
    print()
    print(f'  {Fore.RED}  GOOGLE Maps   {Fore.LIGHTCYAN_EX}:{Fore.LIGHTBLUE_EX}  https://maps.google.com/?q={mylat},{mylon}')
    time.sleep(5)
    print()
    print(f'  {Fore.RED}<{Fore.WHITE}1{Fore.RED}> Main Menu', end='')
    print(f'  {Fore.RED}<{Fore.WHITE}2{Fore.RED}> Exit')
    print()

    mainorexit1 = input(f'  {Fore.RED}>> {Fore.LIGHTYELLOW_EX}')
    if mainorexit1 == '1' or mainorexit1 == '01':
        menu()
    elif mainorexit1 == '2' or mainorexit1 == '02':
        print(Fore.RESET,Back.RESET,'\n')
        exit()
    else:
        print(f' {Fore.RED}[{Fore.WHITE}!{Fore.RED}] {Fore.YELLOW}Invalid option {Fore.RED}[{Fore.WHITE}!{Fore.RED}]')
        time.sleep(1)
        menu()

def zero():
    clear_scr()
    print()
    time.sleep(.1)
    print('𝙴𝚗𝚝𝚎𝚛 𝙲𝚘𝚍𝚎 𝚝𝚘 𝚄𝚗𝚕𝚘𝚌𝚔 𝚝𝚑𝚒𝚜 𝚃𝚘𝚘𝚕!')
    print(f'{Fore.RED}\n')
    time.sleep(.1)
    print()
    zero = md5(input(f'{Fore.YELLOW}  >>{Fore.BLACK}{Back.BLACK}').encode('ASCII')).hexdigest()
    if zero == 'c9284c718b14a0530f371cd614eaa518' or zero == '7b7e6565449bd824bd31e80a7e3bca8d':
        menu()
    else:
        print(f"{Fore.RED}    [𝚇]𝙸𝚗𝚟𝚊𝚕𝚒𝚍 𝙲𝚘𝚍𝚎[𝚇]\n")
        print(f'''{Fore.YELLOW}    𝙿𝚛𝚘𝚋𝚕𝚎𝚖 𝙷𝚎𝚛𝚎?

{Back.RED}{Fore.WHITE} 𝙸𝚏 𝚢𝚘𝚞 𝚍𝚘𝚗𝚝 𝚔𝚗𝚘𝚠 𝚌𝚘𝚍𝚎 𝚍𝚘 𝚝𝚑𝚒𝚜:${Back.BLACK}

{Fore.YELLOW}𝟷. 𝙹𝚘𝚒𝚗 𝚘𝚞𝚛 𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚖:  ${Fore.RED}https://t.me/+sX0qdcVcbEE1Y2I0

{Fore.YELLOW}𝟸. 𝙵𝚒𝚗𝚍 𝙲𝚘𝚍𝚎 𝚒𝚗 𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚖
''')
        time.sleep(13)
        call0()

def call0():
    zero()

if __name__ == '__main__':
    zero()
    exit()
