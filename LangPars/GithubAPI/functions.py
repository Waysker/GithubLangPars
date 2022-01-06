from collections import defaultdict
from .request import github_request


def list_languages_percentage(user):
    # async ?
    repo_list = github_request(f"https://api.github.com/users/{user}/repos")

    user_languages_usage = defaultdict(int)

    for repo in repo_list:
        language_dict = github_request(repo['languages_url'])
        for key, value in language_dict.items():
            user_languages_usage[key] += value

    code_sum = sum(user_languages_usage.values())
    user_languages_percentage = {key: round(value / code_sum * 100, 2) for key, value in user_languages_usage.items()}

    return user_languages_percentage


def list_repos_languages(user):
    repos_languages = defaultdict(list)
    repo_list = github_request(f"https://api.github.com/users/{user}/repos")
    for repo in repo_list:
        language_dict = github_request(repo['languages_url'])
        for key in language_dict.keys():
            repos_languages[repo['name']].append(key)

    return repos_languages
