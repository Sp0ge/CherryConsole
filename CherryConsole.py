from jinja2 import Template
from gen_bot import render_bot

print('████████████████████████████████████')
print('█    ██ ██ ██   ██    ██    ██  █  █')
print('█ ██ ██ ██ ██ ████ ██ ██ ██ ███   ██')
print('█ █████    ██   ██    ██    ████ ███')
print('█ ██ ██ ██ ██ ████ █ ███ █ █████ ███')
print('█    ██ ██ ██   ██ ██ ██ ██ ████ ███')
print('████████████████████████████████████')
print('███████████████████████████████████████')
print('█    █    ██    ██    █    █ ████    ██')
print('█ ██ █ ██ ██ ██ ██ ████ ██ █ ████ █████')
print('█ ████ ██ ██ ██ ██    █ ██ █ ████    ██')
print('█ ██ █ ██ ██ ██ █████ █ ██ █ ████ █████')
print('█    █    ██ ██ ██    █    █    █    ██')
print('███████████████████████████████████████')

print('')
print('')
print('')


bot = False
a = 'stop'
print('print "help" to get command list')
while bot == False:
    print('')
    a = input('CherryConsole->')
    print('')

    if a == 'help':
        print('sb - start bot_editor')
        print('exit - stop program')

    if a == 'exit':
        break


                    
        
    if a == 'sb':
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
    print (' ')

    print(args["q"])
    render_bot(NAME, args)
    print("DONE!")
