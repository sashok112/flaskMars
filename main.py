import os
import threading

from flask import Flask, url_for
from pyngrok import ngrok, conf

os.environ["FLASK_ENV"] = "development"

app = Flask(__name__)
port = 5000

conf.get_default().auth_token = "1TAQMab2CGNEfLxOf5wPDf4UPCn_xQdDqeHaPDEEt96k9tee"
# Open a ngrok tunnel to the HTTP server
public_url = ngrok.connect(port).public_url
print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}\"".format(public_url, port))

# Update any base URLs to use the public ngrok URL
app.config["BASE_URL"] = public_url


# ... Update inbound traffic via APIs to use the public-facing ngrok URL


# Define Flask routes
@app.route("/")
def index():
    return "Привет от приложения Flask"


@app.route('/image_mars')
def image():
    return f'''
    <title>Привет, Марс!</title>
    <h1>Жди нас, Марс!</h1>
    <img src="{url_for('static', filename='img/mars_planet.png')}" 
           alt="здесь должна была быть картинка, но не нашлась">
     <br>Вот она, какая красивая планета!</br>'''


# Start the Flask server in a new thread
threading.Thread(target=app.run, kwargs={"use_reloader": False}).start()
