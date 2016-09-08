import requests

TOP_COUNT = 20
API_URL = 'https://api.github.com/search/repositories?q=created:>2016-08-25&sort=stars&order=desc'


def get_trending_repositories(top_size):
    responce = requests.get(API_URL)
    data = responce.json()
    result = data['items'][:top_size]
    return result


def print_trending_repositories(repositories):
    output = '''    Name: {name}
    Stars: {stars}
    Issues: {issues}
    Url: {url}
    '''
    output += '*' * 75

    for repo in repositories:
        print(output.format(
            name=repo['name'],
            stars=repo['stargazers_count'],
            issues=repo['open_issues_count'],
            url=repo['html_url'],
        ))


if __name__ == '__main__':
    repositories = get_trending_repositories(TOP_COUNT)
    print_trending_repositories(repositories)
