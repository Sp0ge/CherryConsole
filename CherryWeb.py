from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
@app.route('/index.html', methods=['post', 'get'])
def login():
    message = ''
    if request.method == 'POST':
        url = request.form.get('url')
        n = 0
        rew = ''
        urls = url.replace("  "," ").replace("#","").replace(",","").split(' ')
        num = len(urls)
        while num > n:
            url = 'https://vk.com/' + urls[n]
            ans = request.get(url)
            answer = ("  ",'{} {}'.format(urls[n].ljust(30, ' '), ans),)
            rew = rew + ' ' + answer
            n += 1
        message = rew
    return render_template('index.html', message=message)

if __name__ == "__main__":
    app.run()