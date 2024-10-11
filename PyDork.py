# disclaimer
# this tool for pentesting use I'm not responsible how to you use
import os
import sys
import webbrowser
from colorama import Fore

platform = sys.platform
if 'win32' in platform:
    os.system('cls')
elif 'linux' in platform:
    os.system('clear')


def all_domain():
    banner = Fore.RED + '''
     ██▓███ ▓██   ██▓▓█████▄  ▒█████   ██▀███   ██ ▄█▀
    ▓██░  ██▒▒██  ██▒▒██▀ ██▌▒██▒  ██▒▓██ ▒ ██▒ ██▄█▒ 
    ▓██░ ██▓▒ ▒██ ██░░██   █▌▒██░  ██▒▓██ ░▄█ ▒▓███▄░ 
    ▒██▄█▓▒ ▒ ░ ▐██▓░░▓█▄   ▌▒██   ██░▒██▀▀█▄  ▓██ █▄ 
    ▒██▒ ░  ░ ░ ██▒▓░░▒████▓ ░ ████▓▒░░██▓ ▒██▒▒██▒ █▄
    ▒▓▒░ ░  ░  ██▒▒▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░▒ ▒▒ ▓▒
    ░▒ ░     ▓██ ░▒░  ░ ▒  ▒   ░ ▒ ▒░   ░▒ ░ ▒░░ ░▒ ▒░
    ░░       ▒ ▒ ░░   ░ ░  ░ ░ ░ ░ ▒    ░░   ░ ░ ░░ ░ 
             ░ ░        ░        ░ ░     ░     ░  ░   
             ░ ░      ░  

    Pydork V1     By -> Ta3uN                              
    ''' + Fore.RESET
    print(banner)
    print(Fore.YELLOW + 'Publicly -> Publicly exposed documents                      php -> phpinfo()')
    print(
        Fore.BLUE + 'Directory -> Directory listing vulnerabilities               pastebin -> Search pastebin.com / pasting sites')
    print(
        Fore.MAGENTA + 'Configuration -> Configuration files exposed                     flow -> Search stackoverflow.com')
    print(Fore.LIGHTMAGENTA_EX + 'Database -> Database files exposed                          Signup -> Signup pages')
    print(Fore.LIGHTBLACK_EX + 'Log -> Log files exposed                               domains -> Find Subdomains')
    print(Fore.CYAN + 'Backup -> Backup and old files                            SubDomains -> Find Sub-Subdomains')
    print(
        Fore.LIGHTGREEN_EX + 'login -> Login pages                                     IP -> Show only IP addresses (opens multiple tabs)')
    print(Fore.YELLOW + 'SQL -> SQL errors')
    print(Fore.LIGHTCYAN_EX + 'PHP -> PHP errors' + Fore.RESET)

    while True:
        choice_one = input('Choose One With Number ' + Fore.MAGENTA + '>>> ' + Fore.RESET)

        url_Ppublic = input(
            'Enter Target [look like (http OR https://exampl.com/)] ' + Fore.MAGENTA + ' >>> ' + Fore.RESET)
        if 'Publicly' in choice_one:
            public_dork = f'site:{url_Ppublic} ext:doc | ext:docx | ext:odt | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv'
            webbrowser.open('https://www.google.com/search?q=' + public_dork)

        elif 'Directory' in choice_one:
            dicrectory_dork = f'site:{url_Ppublic} intitle:index.of'
            webbrowser.open('https://www.google.com/search?q=' + dicrectory_dork)

        elif 'Configuration' in choice_one:
            Configuration_dork = f'site:{url_Ppublic} ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini | ext:env'
            webbrowser.open('https://www.google.com/search?q=' + Configuration_dork)

        elif 'Database' in choice_one:
            Database_dork = f'site:{url_Ppublic} ext:sql | ext:dbf | ext:mdb'
            webbrowser.open('https://www.google.com/search?q=' + Database_dork)

        elif 'Log' in choice_one:
            Log_dork = f'site:{url_Ppublic} ext:log'
            webbrowser.open('https://www.google.com/search?q=' + Log_dork)

        elif 'Backup' in choice_one:
            Backup_dork = f'site:{url_Ppublic} ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup'
            webbrowser.open('https://www.google.com/search?q=' + Backup_dork)


        elif 'login' in choice_one:
            login_dork = f'site:{url_Ppublic} inurl:login | inurl:signin | intitle:Login | intitle:"sign in" | inurl:auth'
            webbrowser.open_new_tab('https://www.google.com/search?q=' + login_dork)


        elif 'SQL' in choice_one:
            SQL_dork = f'site:{url_Ppublic} intext:"sql syntax near" | intext:"syntax error has occurred" | intext:"incorrect syntax near" | intext:"unexpected end of SQL command" | intext:"Warning: mysql_connect()" | intext:"Warning: mysql_query()" | intext:"Warning: pg_connect()"'
            webbrowser.open('https://www.google.com/search?q=' + SQL_dork)

        elif 'PHP' in choice_one:
            PHP_dork = f'site:{url_Ppublic} "PHP Parse error" | "PHP Warning" | "PHP Error"'
            webbrowser.open('https://www.google.com/search?q=' + PHP_dork)

        elif 'php' in choice_one:
            phpinfo_dork = f'site:{url_Ppublic} ext:php intitle:phpinfo "published by the PHP Group"'
            webbrowser.open('https://www.google.com/search?q=' + phpinfo_dork)

        elif 'pastebin' in choice_one:
            Search_dork = f'site:pastebin.com | site:paste2.org | site:pastehtml.com | site:slexy.org | site:snipplr.com | site:snipt.net | site:textsnip.com | site:bitpaste.app | site:justpaste.it | site:heypasteit.com | site:hastebin.com | site:dpaste.org | site:dpaste.com | site:codepad.org | site:jsitor.com | site:codepen.io | site:jsfiddle.net | site:dotnetfiddle.net | site:phpfiddle.org | site:ide.geeksforgeeks.org | site:repl.it | site:ideone.com | site:paste.debian.net | site:paste.org | site:paste.org.ru | site:codebeautify.org  | site:codeshare.io | site:trello.com "{url_Ppublic}"'
            webbrowser.open('https://www.google.com/search?q=' + Search_dork)

        elif 'flow' in choice_one:
            stackoverflow_dork = f'site:stackoverflow.com "{url_Ppublic}"'
            webbrowser.open('https://www.google.com/search?q=' + stackoverflow_dork)

        elif 'Signup' in choice_one:
            Signup_dork = f'site:{url_Ppublic} inurl:signup | inurl:register | intitle:Signup'
            webbrowser.open('https://www.google.com/search?q=' + Signup_dork)

        elif 'domains' in choice_one:
            Find_dork = f'site:*.{url_Ppublic}'
            webbrowser.open('https://www.google.com/search?q=' + Find_dork)

        elif 'SubDomains' in choice_one:
            Subdomains_dork = f'site:*.*.{url_Ppublic}'
            webbrowser.open('https://www.google.com/search?q=' + Subdomains_dork)

        elif 'IP' in choice_one:
            IP_dork = f'({url_Ppublic}) (site:*.*.29.* |site:*.*.28.* |site:*.*.27.* |site:*.*.26.* |site:*.*.25.* |site:*.*.24.* |site:*.*.23.* |site:*.*.22.* |site:*.*.21.* |site:*.*.20.* |site:*.*.19.* |site:*.*.18.* |site:*.*.17.* |site:*.*.16.* |site:*.*.15.* |site:*.*.14.* |site:*.*.13.* |site:*.*.12.* |site:*.*.11.* |site:*.*.10.* |site:*.*.9.* |site:*.*.8.* |site:*.*.7.* |site:*.*.6.* |site:*.*.5.* |site:*.*.4.* |site:*.*.3.* |site:*.*.2.* |site:*.*.1.* |site:*.*.0.*)'
            webbrowser.open('https://www.google.com/search?q=' + IP_dork)

        replay = input('do you want use again (y,n) >>> ')
        if replay != 'y':
            print('Thank You For Use')
            break
        else:
            platform = sys.platform
            if 'win32' in platform:
                os.system('cls')
            elif 'linux' in platform:
                os.system('clear')
            banner = Fore.RED + '''
             ██▓███ ▓██   ██▓▓█████▄  ▒█████   ██▀███   ██ ▄█▀
            ▓██░  ██▒▒██  ██▒▒██▀ ██▌▒██▒  ██▒▓██ ▒ ██▒ ██▄█▒ 
            ▓██░ ██▓▒ ▒██ ██░░██   █▌▒██░  ██▒▓██ ░▄█ ▒▓███▄░ 
            ▒██▄█▓▒ ▒ ░ ▐██▓░░▓█▄   ▌▒██   ██░▒██▀▀█▄  ▓██ █▄ 
            ▒██▒ ░  ░ ░ ██▒▓░░▒████▓ ░ ████▓▒░░██▓ ▒██▒▒██▒ █▄
            ▒▓▒░ ░  ░  ██▒▒▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░▒ ▒▒ ▓▒
            ░▒ ░     ▓██ ░▒░  ░ ▒  ▒   ░ ▒ ▒░   ░▒ ░ ▒░░ ░▒ ▒░
            ░░       ▒ ▒ ░░   ░ ░  ░ ░ ░ ░ ▒    ░░   ░ ░ ░░ ░ 
                     ░ ░        ░        ░ ░     ░     ░  ░   
                     ░ ░      ░     
            Pydork V1     By -> Ta3uN                          
            ''' + Fore.RESET
            print(banner)
            print(Fore.YELLOW + 'Publicly -> Publicly exposed documents                      php -> phpinfo()')
            print(
                Fore.BLUE + 'Directory -> Directory listing vulnerabilities               pastebin -> Search pastebin.com / pasting sites')
            print(
                Fore.MAGENTA + 'Configuration -> Configuration files exposed                     flow -> Search stackoverflow.com')
            print(
                Fore.LIGHTMAGENTA_EX + 'Database -> Database files exposed                          Signup -> Signup pages')
            print(
                Fore.LIGHTBLACK_EX + 'Log -> Log files exposed                               domains -> Find Subdomains')
            print(
                Fore.CYAN + 'Backup -> Backup and old files                            SubDomains -> Find Sub-Subdomains')
            print(
                Fore.LIGHTGREEN_EX + 'login -> Login pages                                     IP -> Show only IP addresses (opens multiple tabs)')
            print(Fore.YELLOW + 'SQL -> SQL errors')
            print(Fore.LIGHTCYAN_EX + 'PHP -> PHP errors' + Fore.RESET)


all_domain()
