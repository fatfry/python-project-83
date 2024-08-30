import os
from dotenv import load_dotenv
from flask import Flask, render_template

try:
    from dotenv import load_dotenv

    load_dotenv('.env.dev')
except ModuleNotFoundError:
    pass

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')


@app.route('/')
def index():
    return render_template('index.html')


@app.get_urls('/urls')
def show_urls_page():
    return render_template('urls.html')

@app.route('/url')
def show_urls_page():
    return render_template('url.html')

@app.route('/404')
def show_urls_page():
    return render_template('404.html')

@app.route('/urls')
def show_urls_page():
    return render_template('500.html')
