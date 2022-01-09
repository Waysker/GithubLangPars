import requests.exceptions
from flask import Flask, jsonify
from GithubAPI.functions import *


app = Flask(__name__)


@app.errorhandler(requests.exceptions.HTTPError)
def handle_HTTP_error(e):
    if e.response.status_code == 401:
        return 'Bad credentials!', 401
    elif e.response.status_code == 403:
        return f'API rate limit exceeded!. Authorize requests to raise the limit.', 403
    elif e.response.status_code == 404:
        return f'<p>Wrong address, make sure user exists</p> {e}'
    else:
        return f'HTTP error!: {e.response.status_code}'


@app.route("/repos/<name>")
def user(name):
    repos = list_repos_languages(name)
    payload = {
        'repos': [repo.toJson() for repo in repos]
    }

    return payload


@app.route("/lang/<name>")
def lang(name):
    languages = list_languages_percentage(name)
    payload = {
        'languages': [language.toJson() for language in languages]
    }

    return payload


@app.route("/")
def welcome():
    return f"<p>Hello, you stumbled on github language parser API! Here's what it can do:</p>  " \
           "<p>Get list of user repositories with information which languages are used: /repos/{user}</p> " \
           "<p>Get percentage usage of language in all repositories: /lang/{user}</p>"


if __name__ == '__main__':

    app.run(debug=True)
