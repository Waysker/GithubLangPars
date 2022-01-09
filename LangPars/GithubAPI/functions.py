from collections import defaultdict
from .request import github_request
from .objects import *


def to_language_percentage(language, value, sum):
    percentage = round(value / sum * 100, 2)
    return LanguagePercentage(language, percentage)


def list_languages_percentage(user):
    repo_list = github_request(f"https://api.github.com/users/{user}/repos")

    user_languages_usage = defaultdict(int)

    for repo in repo_list:
        language_dict = github_request(repo['languages_url'])
        for language, value in language_dict.items():
            user_languages_usage[language] += value

    code_sum = sum(user_languages_usage.values())
    user_languages_percentage = [to_language_percentage(language, value, code_sum) for language, value in
                                 user_languages_usage.items()]

    return user_languages_percentage


def list_repos_languages(user):
    repos_languages = []
    repo_list = github_request(f"https://api.github.com/users/{user}/repos")
    for repo in repo_list:
        language_dict = github_request(repo['languages_url'])
        language_list = [language for language in language_dict.keys()]
        repos_languages.append(RepoLanguages(repo['name'], language_list))

    return repos_languages
