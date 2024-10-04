import requests
from colorama import Fore
import os
import sys
import time

platform = sys.platform
if 'win32' in platform:
    os.system('cls')
elif 'linux' in platform:
    os.system('clear')

print(Fore.RED+'''██████  ██    ██ ██████  ██    ██ ███████ ████████ ███████ ██████  '''+Fore.RESET)
time.sleep(0.50)
print(Fore.RED+'''██   ██  ██  ██  ██   ██ ██    ██ ██         ██    ██      ██   ██ '''+Fore.RESET)
time.sleep(0.50)
print(Fore.RED+'''██████    ████   ██████  ██    ██ ███████    ██    █████   ██████  '''+Fore.RESET)
time.sleep(0.50)
print(Fore.RED+'''██         ██    ██   ██ ██    ██      ██    ██    ██      ██   ██ '''+Fore.RESET)
time.sleep(0.50)
print(Fore.RED+'''██         ██    ██████   ██████  ███████    ██    ███████ ██   ██'''+Fore.RESET)
time.sleep(0.50)
print('create by -> Ta'+''+Fore.RED+'3'+Fore.RESET+'uN'+Fore.RESET)


file_location = input('Input Dork File: ')

try:
    with open(file_location, "r") as a:
        file = [s.rstrip() for s in a.readlines()]
except FileNotFoundError:
    print(f"Error: File at [{file_location}] not found.")
    exit()

req = requests.session()

url = input('Enter URL (https://example.com/): ').rstrip('/')

for word in file:
    full_url = f'{url}/{word}'
    try:
        source = req.get(full_url)
        if source.status_code in [200, 301]:
            content_length = len(source.content)
            print(
                Fore.GREEN + f'Found -> {full_url}\t[Status -> {source.status_code}]\t[Size -> {content_length} bytes]' + Fore.RESET)
        elif source.status_code in [401, 402, 404]:
            print(Fore.RED + f'Error -> {full_url} [Status -> {source.status_code}]' + Fore.RESET)
        elif source.status_code == 403:
            print(Fore.YELLOW + f'Unkoum -> {full_url}\t[Status -> {source.status_code}]' + Fore.RESET)
    except requests.RequestException as e:
        print(Fore.RED + f'Error accessing {full_url}: {e}' + Fore.RESET)
