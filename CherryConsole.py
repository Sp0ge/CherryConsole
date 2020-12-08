from jinja2 import Template
from gen_bot import render_bot
import time

print("████████████████████████████████████         __.--~~.,-.__     ")
print("█    ██ ██ ██   ██    ██    ██  █  █         `~-._.-(`-.__`-.  ")
print("█ ██ ██ ██ ██ ████ ██ ██ ██ ███   ██                 \    `~~` ")
print("█ █████    ██   ██    ██    ████ ███             .--./ \       ")
print("█ ██ ██ ██ ██ ████ █ ███ █ █████ ███            /#   \  \.--.  ")
print("█    ██ ██ ██   ██ ██ ██ ██ ████ ███            \    /  /#   \ ")
print("████████████████████████████████████             '--'   \    / ")
print("███████████████████████████████████████                  '--'  ")
print("█    █    ██    ██    █    █ ████    ██")
print("█ ██ █ ██ ██ ██ ██ ████ ██ █ ████ █████")
print("█ ████ ██ ██ ██ ██    █ ██ █ ████    ██")
print("█ ██ █ ██ ██ ██ █████ █ ██ █ ████ █████")
print("█    █    ██ ██ ██    █    █    █    ██")
print("███████████████████████████████████████")
print('Powered by Sp0ge and MaBoiexit in 2017')

time.sleep(1)
while True:
    bot = False
    a = 'stop'
    print('print "help" to get command list')
    while bot == False:
        print('')
        a = input('$CherryConsole$->').replace(" ","")
        print('')

        if a == 'help':
            print('bc - start bot editor')
            print('exit - stop program')

        if a == 'exit':
            print('Powered by Sp0ge and MaBoiexit in 2017')
            time.sleep(1)
            break
            

        if a == 'bot editor' or a == 'bc':
            bot = True

    if bot == True:
            
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
        
    
