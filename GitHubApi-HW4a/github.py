import requests
import json

def get_user(user):
    response = requests.get(f"https://api.github.com/users/{user}/repos")
    data = response.json()
    for object in data:
        try:
            name = object['name']
            repos = requests.get(f'https://api.github.com/repos/{user}/{name}/commits')
            count = len(repos.json())
            print(f'Repo: {name} Number of commits: {count}')
        except:
            print("limit exceeded")
    return len(data)

