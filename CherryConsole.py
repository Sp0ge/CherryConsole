﻿from jinja2 import Template
from gen_bot import render_bot
import time
import requests as re

print("  ████████████████████████████████████  __.--~~.,-.__     ")
print("  █    ██ ██ ██   ██    ██    ██  █  █  `~-._.-(`-.__`-.  ")
print("  █ ██ ██ ██ ██ ████ ██ ██ ██ ███   ██          \    `~~` ")
print("  █ █████    ██   ██    ██    ████ ███      .--./ \       ")
print("  █ ██ ██ ██ ██ ████ █ ███ █ █████ ███     /#   \  \.--.  ")
print("  █    ██ ██ ██   ██ ██ ██ ██ ████ ███     \    /  /#   \ ")
print("  ████████████████████████████████████      '--'   \    / ")
print(" ███████████████████████████████████████            '--'  ")
print(" █    █    ██    ██    █    █ ████    ██")
print(" █ ██ █ ██ ██ ██ ██ ████ ██ █ ████ █████")
print(" █ ████ ██ ██ ██ ██    █ ██ █ ████    ██")
print(" █ ██ █ ██ ██ ██ █████ █ ██ █ ████ █████")
print(" █    █    ██ ██ ██    █    █    █    ██")
print(" ███████████████████████████████████████")
print(' Powered by Sp0ge and MaBoi')
print(' https://github.com/Sp0ge/CherryConsole')

time.sleep(1)
while True:
    menu = False
    a = 'stop'
    print(' print "help" to get command list')
    while menu == False:
        print('')
        a = input(' $CherryConsole$ ->').replace(" ","")
        print('')

        if a == 'help':
            print(' bc - start bot editor')
            print(' uc - url check')
            print(' exit - stop program')
            

        if a == 'exit':
            print('Powered by Sp0ge and MaBoiexit in 2017')
            time.sleep(1)
            break
        
        if a == 'bot editor' or a == 'bc' or a == "uc" or a == "urlcheck":
            menu = True
            
    if a == "uc" or a == "urlcheck":
                urls = input("vk short urls -> ").replace("  "," ").replace("#","").replace(",","").split(' ')
                num = len(urls)
                n = 0
                print(' ')
                print("  ___URL_______________________________ANSWER_______")
                while num > n:
                    url = 'https://vk.com/' + urls[n]
                    ans = re.get(url)
                    print("  ",'{} {}'.format(urls[n].ljust(30, ' '), ans),)
                    n += 1
                print('') 
    if a == 'bot editor' or a == 'bc':
            
        print("_________")
            
        print (' print bot name')
        NAME = input()
        print('bot name >>', NAME)
            
        print('')
        print('')

        print('your TOKEN - API')
        token = input()
        print('TOKEN >>', token)

        print('')
        print('')

        args = {
            "token": token,
            "q": []
        }
        
        n = int(input("number of message >> "))          
            
        args["n"] = n

        for i in range(n):
            question = str(input("q >> "))
            answer = str(input("a >> "))
            args["q"].append([question, answer])            

        print ('================')
        print ('YOUR BOT OPTIONS')
        print ('================')

        print(args["q"])
        render_bot(NAME, args)
        print("DONE!")
        
        bot = False
        
    
