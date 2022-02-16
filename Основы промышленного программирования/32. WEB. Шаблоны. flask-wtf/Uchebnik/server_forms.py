from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'sugondeeznuts'


class LoginForm(FlaskForm):
    username = StringField("Логин", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    is_remember = BooleanField("Запомнить меня")
    submit = SubmitField("Войти")


@app.route("/")
@app.route('/login')
def index():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect("/success")
    params = {"form": form, "title": "Авторизация"}
    return render_template("login.html", **params)


@app.route('/success')
def success():
    return render_template('index.html', username='Норм гений')


if __name__ == '__main__':
    app.run(port=8080, host="")
