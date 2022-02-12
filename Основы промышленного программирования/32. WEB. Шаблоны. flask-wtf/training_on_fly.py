from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', defaults={'title': 'MarsOne'})
@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<profession>')
def training(profession):
    if 'инженер' in profession or 'строитель' in profession:
        profession_type = 'инженер'
    else:
        profession_type = 'ученый'
    return render_template('training.html', profession_type=profession_type)


if __name__ == '__main__':
    app.run("", 8080)
