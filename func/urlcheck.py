import time
import requests as re
def urlcheck():
    urls = input("vk short urls -> ").replace("  "," ").replace("#","").replace(",","").split(' ')
    num = len(urls)
    n = 0
    print(' ')
    print("  ___URL_______________________________ANSWER_______")
    print('') 
    while num > n:
        url = 'https://vk.com/' + urls[n]
        ans = re.get(url)
        print("  ",'{} {}'.format(urls[n].ljust(30, ' '), ans),)
        n += 1
    print('') 