from flask import Flask, url_for

app = Flask(__name__)


@app.route('/image_mars')
def image():
    return f'''
    <title>Привет, Марс!</title>
    <h1>Жди нас, Марс!</h1>
    <img src="{url_for('static', filename='img/mars_planet.png')}" 
           alt="здесь должна была быть картинка, но не нашлась">
     <br>Вот она, какая красивая планета</br>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')