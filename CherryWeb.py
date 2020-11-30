from flask import Flask, request, render_template, send_file

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    name = request.form['name']
    token = request.form['token']
    qnum = request.form['qnum']
    q = request.form['q']


if __name__ == "__main__":
    app.run()