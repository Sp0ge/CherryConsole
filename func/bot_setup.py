from jinja2 import Template
from func.gen_bot import render_bot
def bot_setup():
    print("  ___BOT_EDIT______________________________________")
    print('') 
    NAME = input("  bot name >>")
    print('  [',NAME,']')
            
    print('')
    token = input('  TOKEN-API access key >>')
    print('  [',token,']')

    print('')
    print('')

    args = {
        "token": token,
        "q": []
    }
        
    n = int(input("  number of message >> "))          
            
    args["n"] = n

    for i in range(n):
        question = str(input("question >> "))
        answer = str(input("answer >> "))
        args["q"].append([question, answer])
    print(args["q"])            
    render_bot(NAME, args)
    print("DONE!")
    print(" ")
    bot = False