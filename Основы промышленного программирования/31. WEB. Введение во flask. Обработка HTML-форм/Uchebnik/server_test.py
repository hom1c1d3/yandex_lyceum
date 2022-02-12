from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
@app.route('/index')
def index():
    return "Привет, Yandex!"


@app.route('/countdown')
def countdown():
    countdown_list = [str(i) for i in range(10, 0, -1)]
    countdown_list.append("Пуск!")
    return '<br>'.join(countdown_list)


@app.route('/image_sample')
def image():
    return f"""<img src="{url_for('static', filename='img/webserver-1-7.jpeg')}" alt="Сова">"""


@app.route('/sample_page')
def sample_page():
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
        <title>Привет Yandex</title>
    </head>
    <body>

        <h1>Пример страницы</h1>

    </body>
    </html>
    """


@app.route('/bootstrap_sample')
def bootstrap_sample():
    return f"""
<!doctype html>
<html lang="en">
<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

  <title>Hello, world!</title>
</head>
<body>
  <h1>Hello, world!</h1>
  <div class="alert alert-danger" role="danger">
    Я люблю когда волостатые мужики обмазываются маслом
  </div>
</body>
</html>
    """


if __name__ == '__main__':
    app.run(port=8080, host="")
