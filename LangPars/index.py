from flask import Flask, jsonify
from GithubAPI.functions import *

# TODO
# if more requests maybe create storage for urls
# showing current API requests limit
# authorization for less request limits
# Handle API exceeded and Wrong Message (wrong user)
# 'API rate limit exceeded for 5.173.41.179. (But here\'s the good news: Authenticated requests get a higher rate limit. Check out the documentation for more details.)'
# wrong message handler
# In case the JSON decoding fails, r.json() raises an exception. For example, if the response gets a 204 (No Content), or if the response contains invalid JSON, attempting r.json() raises requests.exceptions.JSONDecodeError. This wrapper exception provides interoperability for multiple exceptions that may be thrown by different python versions and json serialization libraries.
# constant counter of requests, maybe in header ?
# cache for requests as to not repeat for example request for list of repos, it is needed in both endpoints
# BIG add oauth authorization from github through redirect

# TODO
# Cel zadania czy procenty są
# Stwórz oprogramowanie pozwalające na:
#  listowanie repozytoriów (nazwa i lista użytych języków programowania),
#  uzyskanie procentowego udziału użytych języków pośród wszystkich repozytoriów,
# dla dowolnego użytkownika serwisu GitHub.


app = Flask(__name__)


@app.route("/repos/<name>")
def user(name):
    repos = list_repos_languages(name)
    payload = {
        'limits': '',
        'repos': repos
    }

    return jsonify(payload)


@app.route("/lang/<name>")
def lang(name):
    languages = list_languages_percentage(name)
    payload = {
        'limits': '',
        'languages': languages
    }

    return jsonify(payload)


@app.route("/")
def welcome():
    # TODO
    # new line ?
    return f"Hello, you stumbled on github language parser API! Here's what it can do:  " \
           "Get list of user repositories with information which languages are used: /repos/{user} " \
           "Get percentage usage of language in all repositories"


if __name__ == '__main__':

    app.run(debug=True)
