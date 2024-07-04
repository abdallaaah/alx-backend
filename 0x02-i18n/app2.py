#!/usr/bin/env python3
"""The first endpoint that flask app will run"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

class Config:
    """Class responsible for Flask app configurations"""
    LANGUAGES = ["en","fr"]
    BABEL_DEFAULT_LOCALE = "fr"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

def get_user(login_as):
    """Retrieve a user by ID."""
    try:
        return users.get(int(login_as))
    except (ValueError, TypeError):
        return None
    
@babel.localeselector
def get_locale():
    """Get the languagh the you will use or best match to user"""
    lang = request.args.get('locale')
    if lang and lang in app.config["LANGUAGES"]:
        return lang
    user = getattr(g, 'user', None)
    if user and user.get('locale') and user.get('locale') in app.config["LANGUAGES"]:
        return user.get('locale')
    lang = request.accept_languages.best_match(app.config['LANGUAGES'])
    if lang:
        return lang
    
    return app.config['BABEL_DEFAULT_LOCALE']

@app.before_request
def before_request():
    id = request.args.get('login_as')
    if id:
        user = get_user(int(id))
        if user:
            g.user = user
            return
    g.user = None

@app.context_processor
def inject_conf_var():
    return dict(get_locale=get_locale)

@app.route('/')
def index():
    """The index of the Flask app"""
    return render_template('2-index.html', username=g.user.get('name'))


@app.route('/index')
def test_index():
    return "test index"

if __name__ == '__main__':
    app.run(debug=True)
