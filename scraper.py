import shutil

from git import Repo
import os
from datetime import datetime
from collections import Counter
import csv


def analyze_git_repo(repo_url):

    if not repo_url.endswith('.git'):
        repo_url = repo_url + '.git'
        print(f"Added .git extension. New URL: {repo_url}")

    repo_path = "./temp"
    repo_name = repo_url.rstrip(".git").split("/")[-1]
    try:
        # CLONE REPO FROM URL
        if not os.path.exists(repo_path):
            print(f"Cloning repository from {repo_url}...")
            Repo.clone_from(repo_url, repo_path)
            print("Repository cloned successfully!")

        repo = Repo(repo_path)

        # Get all commits
        commits = list(repo.iter_commits())
        email_commits = Counter()
        email_authors = {}  # Store email for each author


        for commit in commits:
            author_email = commit.author.email
            email_commits[author_email] += 1
            email_authors[author_email] = commit.author.email

        last_commit = commits[0]  # First commit in the list is the most recent
        last_commit_date = datetime.fromtimestamp(last_commit.committed_date)

        print(f"\n📁 Repository: {repo_name}")
        print(f"📊 Total commits: {len(commits)}")
        print(f"Total authors: {len(email_commits)}")
        print(f"Last commit: {last_commit_date.strftime('%Y-%m-%d %H:%M:%S')}\n")

        with open("data.csv", "a", newline='') as csv_file:
            fieldnames = ["repository", "commits", "authors", "last_commit"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            if os.stat("data.csv").st_size == 0:
                writer.writeheader()
            writer.writerow({
                "repository": repo_name,
                "commits": len(commits),
                "authors": len(email_commits) - 1,
                "last_commit": last_commit_date.strftime('%Y-%m-%d')
            })

        #PASS THESE THREE ITEMS TO THE CSV

        # Print author statistics
        print("👥 Author Statistics:")
        print("-" * 80)
        print(f"{'Author':<30} {'Email':<30} {'Commits':<10} {'Percentage':>10}")
        print("-" * 80)

        for email, commit_count in sorted(email_commits.items(), key=lambda x: x[1], reverse=True):
            percentage = (commit_count / len(commits)) * 100
            author_name=email_authors[email].split("@")[0]
            print(f"{email:<30} {author_name:<30} {commit_count:<10} {percentage:>9.1f}%")

        print("-" * 80 + "\n")

        # Print commit details
        print("📝 Commit Details:")

        print(f"\nCleaning up: Removing local repository at {repo_path}")
        shutil.rmtree(repo_path)




    except Exception as e:
        print(f"Error analyzing repository: {str(e)}")
        if os.path.exists(repo_path):
            print(f"\nCleaning up after error...")
            shutil.rmtree(repo_path)
            print("Cleanup completed!")



if __name__ == "__main__":
    repo_urls = [





    ]

    # Create or clear the data.csv file
    with open("data.csv", "w", newline='') as csv_file:
        fieldnames = ["repository", "commits", "authors", "last_commit"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

    # Process each repository
    for repo_url in repo_urls:
        print(f"\nProcessing repository: {repo_url}")
        try:
            analyze_git_repo(repo_url)
        except Exception as e:
            print(f"Failed to process repository {repo_url}: {str(e)}")
            continue