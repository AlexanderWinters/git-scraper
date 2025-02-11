import shutil

from git import Repo
import os
from datetime import datetime
from collections import Counter


def analyze_git_repo(repo_url):

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

        print(f"\n📁 Repository: {repo_name}")
        print(f"📊 Total commits: {len(commits)}")
        print(f"Total authors: {len(email_commits)}\n")

        with open("data.csv", "a") as csv_file:
            if os.stat("data.csv").st_size == 0:
                csv_file.write("repository,commits,authors\n")
            csv_file.write(f"{repo_name},{len(commits)},{len(email_commits)}\n")
        
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
    repo_url = input("Repository URL: ")
    analyze_git_repo(repo_url)