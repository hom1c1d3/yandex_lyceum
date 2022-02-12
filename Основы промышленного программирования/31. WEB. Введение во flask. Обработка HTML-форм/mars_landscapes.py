from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def mission_name():
    return "Миссия Колонизация Марса"


@app.route('/index')
def mission_deviz():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    promotion_lines = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                       'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
                       'Присоединяйся!']
    return '<br>'.join(promotion_lines)


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}" width="256" height="256">
                    <p>Вот какая она, красная планета!</p>
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet"
                     type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <link
                     href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
                      rel="stylesheet"
                       integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
                        crossorigin="anonymous" />

                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1 class"promotion_header">Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}" width="256" height="256">
                    <div class="alert alert-dark" role="alert">
                        Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                        Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                        Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                        И начнем с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                        Присоединяйся!
                    </div>
                  </body>
                </html>"""


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_astronaut_selection():
    if request.method == 'GET':
        return f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
            rel="stylesheet"
            integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
            crossorigin="anonymous">
    <link href="{url_for('static', filename='css/style.css')}" rel="stylesheet" type="text/css">
    <title>Отбор астронавтов</title>
</head>
<body>
<h1 align="center">Анкета претендента</h1>
<h2 align="center">на участие в миссии</h2>
<div class="container">
    <form class="login_form" method="post">
        <div class="form-group">
            <input type="text" class="form-control" id="surname" placeholder="Введите фамилию"
                   name="surname" required>
            <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name" required>
        </div>
        <div class="form-group">
            <input type="email" class="form-control" id="email" aria-describedby="emailHelp"
                   placeholder="Введите адрес почты" name="email" required>
        </div>
        <div class="form-group">
            <label for="educationSelect">Какое у Вас образование?</label>
            <select class="form-control" id="educationSelect" name="education">
                <option>Начальное</option>
                <option>Основное</option>
                <option>Среднее</option>
                <option>Высшее</option>
            </select>
        </div>
        <div class="form-group">
            <label for="professions">Какие у Вас есть профессии?</label>
            <div class="form-check" id="professions">
                <input type="checkbox" class="form-check-input" id="engineerExplorer"
                       name="profession" value="Инженер-исследователь">
                <label class="form-check-label" for="engineerExplorer">Инженер-исследователь</label>
            </div>
            <div class="form-check">
                <input type="checkbox" class="form-check-input" id="engineerBuilder"
                       name="profession" value="Инженер-строитель">
                <label class="form-check-label" for="engineerBuilder">Инженер-строитель</label>
            </div>
            <div class="form-check">
                <input type="checkbox" class="form-check-input" id="pilot" name="profession" value="Пилот">
                <label class="form-check-label" for="pilot">Пилот</label>
            </div>
            <div class="form-check">
                <input type="checkbox" class="form-check-input" id="meteorologist" name="profession" value="Метеорологист">
                <label class="form-check-label" for="meteorologist">Метеорологист</label>
            </div>
            <div class="form-check">
                <input type="checkbox" class="form-check-input" id="engineerLifeSupport"
                       name="profession" value="Инженер по жизнеобеспечению">
                <label class="form-check-label" for="engineerLifeSupport">Инженер по
                    жизнеобеспечению</label>
            </div>
            <div class="form-check">
                <input type="checkbox" class="form-check-input" id="engineerRadioactivityProtection"
                       name="profession" value="Инженер по защите от радиоактивности">
                <label class="form-check-label" for="engineerRadioactivityProtection">Инженер по
                    защите от радиоактивности</label>
            </div>
            <div class="form-check">
                <input type="checkbox" class="form-check-input" id="doctor" name="profession" value="Врач">
                <label class="form-check-label" for="doctor">Врач</label>
            </div>
            <div class="form-check">
                <input type="checkbox" class="form-check-input" id="exobiologist" name="profession" value="Экзобиолог">
                <label class="form-check-label" for="exobiologist">Экзобиолог</label>
            </div>
        </div>
        <div class="form-group">
            <label for="sex">Укажите пол</label>
            <div class="form-check" id="sex">
                <input class="form-check-input" type="radio" name="sex" id="male" value="male"
                       checked>
                <label class="form-check-label" for="male">
                    Мужской
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                <label class="form-check-label" for="female">
                    Женский
                </label>
            </div>
        </div>
        <div class="form-group">
            <label for="reason">Почему Вы хотите принять участие в миссии</label>
            <textarea class="form-control" id="reason" rows="3" name="reason"></textarea>
        </div>
        <div class="form-group">
            <label for="photo">Приложите фотографию</label>
            <input type="file" class="form-control-file" id="photo" name="file">
        </div>
        <div class="form-group form-check">
            <input type="checkbox" class="form-check-input" id="acceptStay" name="accept">
            <label class="form-check-label" for="acceptStay">Готовы остаться на Марсе?</label>
        </div>
        <button type="submit" class="btn btn-primary">Записаться</button>
    </form>
</div>
</body>
</html>"""
    elif request.method == 'POST':
        print(request.form['name'])
        print(request.form['surname'])
        print(request.form['email'])
        print(request.form['education'])
        print(request.form.getlist('profession'))
        print(request.form['profession'])
        print(request.form['reason'])
        print(request.form['accept'])
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choice(planet_name):
    description = {
        'short_description': 'Эта планета близка к Земле;',
        'description1': 'На ней много необходимых ресурсов;',
        'description2': 'На ней есть вода и атмосфера;',
        'description3': 'На ней есть небольшое магнитное поле;',
        'description4': 'Наконец, она просто красива!'
    }
    return """<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
            rel="stylesheet"
            integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
            crossorigin="anonymous">
    <title>Варианты выбора</title>
</head>
<body>
<div class="container">
<h1 align="center">Мое предложение: {planet_name}</h1>
<h3 align="center">{short_description}</h3>
<div class="alert alert-success" role="alert">
    <h3>{description1}</h3>
</div>
<div class="alert alert-secondary" role="alert">
    <h3>{description2}</h3>
</div>
<div class="alert alert-warning" role="alert">
    <h3>{description3}</h3>
</div>
<div class="alert alert-danger" role="alert">
    <h3>{description4}</h3>
</div>
</div>
</body>
</html>""".format(planet_name=planet_name, **description)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def selection_results(nickname: str, level: int, rating: float):
    return f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
            rel="stylesheet"
            integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
            crossorigin="anonymous">
    <title>Результаты</title>
</head>
<body>
<div class="container">
<h1 align="center">Результаты отбора</h1>
<h2 align="center">Претендетна на участие в миссии {nickname}:</h2>
<div class="alert alert-success" role="alert">
    <h3>Поздравляем! Ваш рейтинг после {level} этапа отбора</h3>
</div>
<div class="alert alert-light" role="alert">
    <h3>составляет {rating}!</h3>
</div>
<div class="alert alert-warning" role="alert">
    <h3>Желаем удачи!</h3>
</div>
</div>
</body>
</html>"""


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    import os
    template = """<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
            rel="stylesheet"
            integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
            crossorigin="anonymous">
    <link href="{}" rel="stylesheet" type="text/css">
    <title>Отбор астронавтов</title>
</head>
<body>
<h1 align="center">Загрузка фотографии</h1>
<h2 align="center">для участие в миссии</h2>
<div class="container">
    <form class="login_form" method="post" enctype="multipart/form-data">
        <div class="form-group">
            <label for="photo">Приложите фотографию</label>
            <input type="file" class="form-control-file" id="photo" name="file">
        </div>
        {}
        <div class="form-group">
            <button type="submit" class="btn btn-primary">Отправить</button>
        </div>
    </form>
</div>
</body>
</html>"""
    if request.method == 'GET':
        """        <div class="text-center">
            <img src="static/img/photo.jpg" class="rounded" alt="Фото">
        </div>"""
        if os.path.exists('static/img/photo.jpg'):
            img = f"""<div class="text-center" style="max-height: 100%; max_width: 100%;">
            <img src="{url_for('static', filename='img/photo.jpg')}" class="rounded" alt="Фото">
        </div>"""
        else:
            img = ""
        page = template.format(url_for("static", filename='css/style.css'), img)
        return page
    elif request.method == 'POST':
        image = request.files['file']
        with open('static/img/photo.jpg', 'wb') as fd:
            fd.write(image.stream.read())
        return "Фото загружено"


@app.route('/carousel')
def carousel():
    return f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
            rel="stylesheet"
            integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
            crossorigin="anonymous">
    <link href="{url_for('static', filename='css/style.css')}" rel="stylesheet" type="text/css">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"
            crossorigin="anonymous"></script>
    <title>Пейзажи Марса</title>
</head>
<body>
<h1 align="center">Пейзажи Марса</h1>

<div class="container"><div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0"
                class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1"
                aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2"
                aria-label="Slide 3"></button>
    </div>
    <div class="carousel-inner">
        <div class="carousel-item active">
            <img src="{url_for('static', filename='img/1.png')}" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
            <img src="{url_for('static', filename='img/2.png')}" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
            <img src="{url_for('static', filename='img/3.png')}" class="d-block w-100" alt="...">
        </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators"
            data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators"
            data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
    </button>
</div></div>
</body>
</html>"""


if __name__ == '__main__':
    app.run(port=8080, host="")
