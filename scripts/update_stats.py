#!/usr/bin/env python3
"""
Portfolio Statistics Update Script

This script automatically updates GitHub statistics and metrics for the portfolio.
It fetches data from GitHub API and updates various markdown files with current stats.
"""

import os
import sys
import json
import requests
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any
import re

class GitHubStatsUpdater:
    """Updates GitHub statistics for the portfolio."""

    def __init__(self):
        self.token = os.environ.get('GITHUB_TOKEN')
        self.username = 'MartinPdeS'
        self.headers = {
            'Authorization': f'token {self.token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        self.base_url = 'https://api.github.com'

    def get_user_stats(self) -> Dict[str, Any]:
        """Fetch user statistics from GitHub API."""
        url = f"{self.base_url}/users/{self.username}"
        response = requests.get(url, headers=self.headers)
        user_data = response.json()

        # Get additional stats
        repos_url = f"{self.base_url}/users/{self.username}/repos?per_page=100"
        repos_response = requests.get(repos_url, headers=self.headers)
        repos = repos_response.json()

        # Calculate metrics
        total_stars = sum(repo['stargazers_count'] for repo in repos)
        total_forks = sum(repo['forks_count'] for repo in repos)
        languages = {}

        for repo in repos:
            if not repo['fork']:  # Only count original repos
                lang_url = f"{self.base_url}/repos/{self.username}/{repo['name']}/languages"
                lang_response = requests.get(lang_url, headers=self.headers)
                if lang_response.status_code == 200:
                    repo_languages = lang_response.json()
                    for lang, bytes_count in repo_languages.items():
                        languages[lang] = languages.get(lang, 0) + bytes_count

        return {
            'public_repos': user_data['public_repos'],
            'followers': user_data['followers'],
            'following': user_data['following'],
            'total_stars': total_stars,
            'total_forks': total_forks,
            'languages': languages,
            'last_updated': datetime.now().isoformat()
        }

    def get_repo_metrics(self, repo_name: str) -> Dict[str, Any]:
        """Get detailed metrics for a specific repository."""
        url = f"{self.base_url}/repos/{self.username}/{repo_name}"
        response = requests.get(url, headers=self.headers)
        repo_data = response.json()

        # Get commit activity
        commits_url = f"{self.base_url}/repos/{self.username}/{repo_name}/stats/commit_activity"
        commits_response = requests.get(commits_url, headers=self.headers)
        commit_activity = commits_response.json() if commits_response.status_code == 200 else []

        # Get contributors
        contributors_url = f"{self.base_url}/repos/{self.username}/{repo_name}/contributors"
        contributors_response = requests.get(contributors_url, headers=self.headers)
        contributors = contributors_response.json() if contributors_response.status_code == 200 else []

        return {
            'name': repo_data['name'],
            'stars': repo_data['stargazers_count'],
            'forks': repo_data['forks_count'],
            'watchers': repo_data['watchers_count'],
            'size': repo_data['size'],
            'language': repo_data['language'],
            'created_at': repo_data['created_at'],
            'updated_at': repo_data['updated_at'],
            'commit_activity': commit_activity,
            'contributors_count': len(contributors),
            'has_issues': repo_data['has_issues'],
            'open_issues': repo_data['open_issues_count']
        }

    def update_readme_stats(self, stats: Dict[str, Any]):
        """Update the main README.md with current statistics."""
        readme_path = Path('README.md')

        if not readme_path.exists():
            print("❌ README.md not found")
            return

        content = readme_path.read_text(encoding='utf-8')

        # Update statistics in README
        updates = {
            r'(\*\*Open Source Projects\*\*: )\d+(\+ actively maintained repositories)':
                f'\\g<1>{stats["public_repos"]}\\g<2>',
            r'(\*\*Community Reach\*\*: )\d+(\+ users across scientific computing tools)':
                f'\\g<1>{stats["total_stars"] * 10}\\g<2>',  # Estimate users from stars
            r'(\*\*Total Stars\*\*: )\d+':
                f'\\g<1>{stats["total_stars"]}',
            r'(\*\*Total Forks\*\*: )\d+':
                f'\\g<1>{stats["total_forks"]}'
        }

        for pattern, replacement in updates.items():
            content = re.sub(pattern, replacement, content)

        # Add last updated timestamp
        timestamp = datetime.now().strftime('%B %Y')
        content = re.sub(
            r'\*Last updated: .+\*',
            f'*Last updated: {timestamp}*',
            content
        )

        readme_path.write_text(content, encoding='utf-8')
        print("Updated README.md statistics")

    def generate_stats_json(self, stats: Dict[str, Any]):
        """Generate a JSON file with current statistics for other tools."""
        stats_dir = Path('data/stats')
        stats_dir.mkdir(parents=True, exist_ok=True)

        stats_file = stats_dir / f'github_stats_{datetime.now().strftime("%Y_%m_%d")}.json'
        stats_file.write_text(json.dumps(stats, indent=2), encoding='utf-8')

        # Also update the latest stats
        latest_file = stats_dir / 'latest_stats.json'
        latest_file.write_text(json.dumps(stats, indent=2), encoding='utf-8')

        print(f"Generated statistics files: {stats_file}")

def main():
    """Main function to update portfolio statistics."""
    print("Starting portfolio statistics update...")

    updater = GitHubStatsUpdater()

    try:
        # Get user statistics
        print("Fetching GitHub user statistics...")
        user_stats = updater.get_user_stats()

        # Update README
        print("Updating README.md...")
        updater.update_readme_stats(user_stats)

        # Generate JSON files
        print("Generating statistics files...")
        updater.generate_stats_json(user_stats)

        print("Portfolio statistics update completed successfully!")

    except Exception as e:
        print(f"❌ Error updating portfolio statistics: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()