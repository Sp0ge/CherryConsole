from func.urlcheck import urlcheck
import time
from func.bot_setup import bot_setup
from func.logo import logo

logo()

print('')
print(' print "help" to get command list')
while True:
    menu = False
    a = 'stop'
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
            quit()
        
        if a == 'bot editor' or a == 'bc' or a == "uc" or a == "urlcheck":
            menu = True
            
    if a == "uc" or a == "urlcheck":
                urlcheck()

    if a == 'bot editor' or a == 'bc':
                bot_setup()
            
        
    
