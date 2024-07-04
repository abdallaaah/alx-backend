#!/usr/bin/env python3
"""The first endpoint that flask app will run"""
from flask import Flask, render_template, request
from flask_babel import Babel

class Config:
    """Class responsible for language settings"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

@app.route('/')
def index():
    """The index of the Flask app"""
    print(app.config)
    return render_template('index.html')

@app.route('/index')
def test_index():
    return "test index"

if __name__ == '__main__':
    app.run(debug=True)
