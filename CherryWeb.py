from flask import Flask, request, render_template, send_file
from wtforms import Form, BooleanField, StringField, PasswordField, validators


app = Flask(__name__)

@app.route('/')
@app.route('/index.html', methods=['GET', 'POST'])
def form():
    try:
        a = form.objects.get()
    except form.DoesNotExist:
        a = None

    if request.method == 'POST' and form.validate():
        form = form(request.form)
        user = User(form.name.data, form.token.data, form.qnum.data)
        if form.is_valid():
            form.save()
            flash(user)

    return render_template('index.html', {'form': form})



if __name__ == "__main__":
    app.run()