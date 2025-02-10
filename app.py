from git import Repo
from datetime import datetime
from collections import Counter


def analyze_git_repo(repo_path):
    try:
        # Open the repository
        repo = Repo(repo_path)

        # Get all commits
        commits = list(repo.iter_commits())
        author_commits = Counter()
        author_emails = {}  # Store email for each author

        for commit in commits:
            author_name = commit.author.name
            author_commits[author_name] += 1
            author_emails[author_name] = commit.author.email

        print(f"\n📁 Repository: {repo_path}")
        print(f"📊 Total commits: {len(commits)}\n")

        # Print author statistics
        print("👥 Author Statistics:")
        print("-" * 80)
        print(f"{'Author':<30} {'Email':<30} {'Commits':<10} {'Percentage':>10}")
        print("-" * 80)

        for author, commit_count in sorted(author_commits.items(), key=lambda x: x[1], reverse=True):
            percentage = (commit_count / len(commits)) * 100
            email = author_emails[author]
            print(f"{author:<30} {email:<30} {commit_count:<10} {percentage:>9.1f}%")

        print("-" * 80 + "\n")

        # Print commit details
        print("📝 Commit Details:")
        print("-" * 80 + "\n")

        print(f"\n📁 Repository: {repo_path}")
        print(f"📊 Total commits: {len(commits)}\n")

        # # Iterate through each commit
        # for commit in commits:
        #     # Format timestamp
        #     commit_date = datetime.fromtimestamp(commit.committed_date)
        #     formatted_date = commit_date.strftime("%Y-%m-%d %H:%M:%S")
        #
        #     print(f"Commit: {commit.hexsha}")
        #     print(f"Author: {commit.author.name} <{commit.author.email}>")
        #     print(f"Date: {formatted_date}")
        #     print(f"Message: {commit.message.strip()}")
        #
        #     # Get statistics for the commit
        #     stats = commit.stats.total
        #     print(f"Changes: {stats['files']} files changed, "
        #           f"{stats['insertions']} insertions(+), "
        #           f"{stats['deletions']} deletions(-)")
        #     print("-" * 80 + "\n")

    except Exception as e:
        print(f"Error analyzing repository: {str(e)}")


if __name__ == "__main__":
    # Replace with your repository path
    repository_path = input("path to repository: ")
    analyze_git_repo(repository_path)