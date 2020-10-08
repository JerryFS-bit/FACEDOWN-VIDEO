
#ORIGINAL AUTHOR OF THE CODE; AnonymousFromGeorgia
#MODIFIED BY: JerryFS-bit

import os
import re
import requests
import pyfiglet 

from colorama import Fore, Back, init
from datetime import datetime
from signal import signal, SIGINT
from tqdm import tqdm
from os import system, name

def Cscreen():
    if name == "posix":
        system("clear")
    else:
        system("cls")

def information_author():
    print(Fore.WHITE + "YouTube   : https://youtube.com/AnonymousFromGeorgia" + Fore.RESET)
    print(Fore.LIGHTBLUE_EX + "Github    : https://github.com/AnonymousFromGeorgia" + Fore.RESET)
    print(Fore.WHITE + "Facebook  : https://facebook.com/anonimaluri" + Fore.RESET)
    print(Fore.LIGHTBLUE_EX + "Twitter   : https://twitter.com/anonimaluri" + Fore.RESET)

def keyboardInterruptHandler(signal, frame):
    print(Fore.YELLOW + "\nThe program has been shut down !!".format(signal))
    exit(0)

signal(SIGINT, keyboardInterruptHandler)  
fb = pyfiglet.figlet_format("FaceDownVideo") 

Cscreen()
print(Fore.BLUE + fb + Fore.RESET)
print(Fore.LIGHTYELLOW_EX + "ORIGINAL CREATOR: AnonymousFromGeorgia " + Fore.RESET)
print("--------------------------------------------------------------------")
information_author()
print("--------------------------------------------------------------------")

print(Fore.YELLOW + "\nMODIFIED BY: JerryFS-bit" + Fore.RESET)
print("--------------------------------------------------------------------")
print(Fore.LIGHTBLUE_EX + "Github    : https://github.com/JerryFS-bit" + Fore.RESET)
print("--------------------------------------------------------------------")


url = input(Fore.CYAN + "\n\nENTER THE [URL] OF THE VIDEO: " + Fore.RESET)
x = re.match(r'^(https:|)[/][/]www.([^/]+[.])*facebook.com', url)


if x:
    html = requests.get(url).content.decode('utf-8')
else:
    information()
    exit()

_qualityhd = re.search('hd_src:"https', html)
_qualitysd = re.search('sd_src:"https', html)
_hd = re.search('hd_src:null', html)
_sd = re.search('sd_src:null', html)

list = []
_thelist = [_qualityhd, _qualitysd, _hd, _sd]
for id,val in enumerate(_thelist):
    if val != None:
        list.append(id)

try:
    if len(list) == 2:
        if 0 in list and 1 in list:
            _input_1 = str(input(Fore.LIGHTBLUE_EX + "SELECT OPTION A FOR HD RESOLUTION, OTHERWISE SELECT OPTION B FOR STANDARD QUALITY: " + Fore.RESET)).upper()
            if _input_1 == 'A':
                print(Fore.LIGHTYELLOW_EX + "\nDOWNLOADING VIDEO IN HD QUALITY" + Fore.RESET)
                video_url = re.search(r'hd_src:"(.+?)"', html).group(1)
                file_size_request = requests.get(video_url, stream=True)
                file_size = int(file_size_request.headers['Content-Length'])
                block_size = 1024 

                sel = str(input("If you want to add a name to your file, type 'Y' otherwise press 'N' and the system will assign one: ")).upper()
                if (sel == 'Y'):
                    filename_favorite = str(input("Enter the file name (omit the extension): "))
                    t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename_favorite, ascii=True)
                    with open(filename_favorite + '.mp4', 'wb') as f:
                        for data in file_size_request.iter_content(block_size):
                            t.update(len(data))
                            f.write(data)
                elif (sel == 'N'):
                    filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                    t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
                    with open(filename + '.mp4', 'wb') as f:
                        for data in file_size_request.iter_content(block_size):
                            t.update(len(data))
                            f.write(data)
                t.close()

            if _input_1 == 'B':
                print(Fore.LIGHTYELLOW_EX + "\nDOWNLOADING VIDEO IN SD QUALITY" + Fore.RESET)
                video_url = re.search(r'sd_src:"(.+?)"', html).group(1)
                file_size_request = requests.get(video_url, stream=True)
                file_size = int(file_size_request.headers['Content-Length'])
                block_size = 1024 

                sel = str(input("If you want to add a name to your file, type 'Y' otherwise press 'N' and the system will assign one: ")).upper()

                if (sel == 'Y'):
                    filename_favorite = str(input("Enter the file name (omit the extension): "))
                    t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename_favorite, ascii=True)

                    with open(filename_favorite + '.mp4', 'wb') as f:
                        for data in file_size_request.iter_content(block_size):
                            t.update(len(data))
                            f.write(data)
                elif (sel == 'N'):
                    filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                    t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
                    with open(filename + '.mp4', 'wb') as f:
                        for data in file_size_request.iter_content(block_size):
                            t.update(len(data))
                            f.write(data)                    
                t.close()

    if len(list) == 2:
        if 1 in list and 2 in list:
            _input_2 = str(input("Sorry! Unfortunately the video is not available in HD quality. Do you want to download anyway? ('Y' or 'N'): ")).upper()
            if _input_2 == 'Y':
                print(Fore.LIGHTYELLOW_EX + "\nDOWNLOADING VIDEO IN SD QUALITY" + Fore.RESET)
                video_url = re.search(r'sd_src:"(.+?)"', html).group(1)
                file_size_request = requests.get(video_url, stream=True)
                file_size = int(file_size_request.headers['Content-Length'])
                block_size = 1024 
                filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
                with open(filename + '.mp4', 'wb') as f:
                    for data in file_size_request.iter_content(block_size):
                        t.update(len(data))
                        f.write(data)
                t.close()

            if _input_2 == 'N':
                exit()

    if len(list) == 2:
        if 0 in list and 3 in list:
            _input_2 = str(input("Sorry! Unfortunately the video is not available in HD quality. Do you want to download anyway? ('Y' or 'N'): \n")).upper()
            if _input_2 == 'Y':
                print(Fore.LIGHTYELLOW_EX + "\nDOWNLOADING VIDEO IN HD QUALITY" + Fore.RESET)
                video_url = re.search(r'hd_src:"(.+?)"', html).group(1)
                file_size_request = requests.get(video_url, stream=True)
                file_size = int(file_size_request.headers['Content-Length'])
                block_size = 1024 
                filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
                with open(filename + '.mp4', 'wb') as f:
                    for data in file_size_request.iter_content(block_size):
                        t.update(len(data))
                        f.write(data)
                t.close()

            if _input_2 == 'N':
                exit()
except(KeyboardInterrupt):
    print("\nThe program has been shut down")
