#!/usr/bin/env python3
"""Export observed GitHub counts; never infer adoption or modify portfolio prose.

Optional utility, independent of the website. GITHUB_TOKEN is optional. Uses
only the standard library and paginates the public, owned repository list.
"""
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

USERNAME = 'MartinPdeS'


def get_json(path):
    headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'portfolio-stats'}
    if token := os.environ.get('GITHUB_TOKEN'):
        headers['Authorization'] = f'Bearer {token}'
    request = Request(f'https://api.github.com/{path}', headers=headers)
    with urlopen(request, timeout=30) as response:
        return json.load(response)


def main():
    repos = []
    page = 1
    while True:
        batch = get_json(f'users/{USERNAME}/repos?type=owner&per_page=100&page={page}')
        repos.extend(repo for repo in batch if not repo['fork'])
        if len(batch) < 100:
            break
        page += 1
    stats = {
        'username': USERNAME,
        'observed_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'Public, owned, non-fork repositories; includes archived repositories',
        'repository_count': len(repos),
        'stars': sum(repo['stargazers_count'] for repo in repos),
        'forks': sum(repo['forks_count'] for repo in repos),
    }
    destination = Path(__file__).resolve().parents[1] / 'data/stats/latest_stats.json'
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(stats, indent=2) + '\n')
    print(f'Wrote observed counts to {destination}')


if __name__ == '__main__':
    main()
