import requests
from .auth import header_dict


def github_request(url):
    response = requests.get(url, headers=header_dict)
    response.raise_for_status()
    return response.json()
