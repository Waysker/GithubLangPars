import requests
from .auth import header_dict


def github_request(url):
    response = requests.get(url, headers=header_dict)
    response.raise_for_status()
    # limits['used'] = response.headers["X-RateLimit-Used"]
    # limits['limit'] = response.headers["X-RateLimit-Limit"]
    return response.json()
#     # I want this
#     # if repo_list.status_code == 403:
#     #     limit = repo_list.headers["X-RateLimit-Limit"]
#     #     used = repo_list.headers["X-RateLimit-Used"]
#     #     return f"API rate limit exceeded! Limit: {limit} Used: {used}"
