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


@app.route('/list_prof/<list_type>')
def list_professions(list_type):
    professions = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                   'инженер по терраформированию', 'климатолог', 'специалист по радиационной защите',
                   'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения', 'метеоролог',
                   'оператор марсохода', 'киберинженер', 'штурман', 'пилот дронов']
    return render_template('professions.html', list_type=list_type, professions=professions)


def get_answers():
    answers = {
        "title": "Анкета",
        "surname": "Watny",
        "name": "Mark",
        "education": "выше среднего",
        "profession": "штурман марсохода",
        "sex": "male",
        "motivation": "Всегда мечтал застрять на Марсе!",
        "ready": "True",
    }
    questions_to_display = {
        "surname": "Фамилия",
        "name": "Имя",
        "education": "Образование",
        "profession": "Профессия",
        "sex": "Пол",
        "motivation": "Мотивация",
        "ready": "Готовы остаться на марсе",
    }
    answers_display = {}
    for k, v in answers.items():
        k = questions_to_display.get(k, k)
        answers_display[k] = v
    return answers_display


@app.route('/auto_answer')
@app.route('/answer')
def answer():
    answers = get_answers()
    title = answers.pop('title')
    return render_template('auto_answer.html', title=title, answers=answers)


if __name__ == '__main__':
    app.run("", 8080)
