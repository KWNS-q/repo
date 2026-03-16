import subprocess

# Get total number of commits
total_commits = subprocess.check_output(
    ["git", "rev-list", "--count", "HEAD"], text=True
).strip()

# Get last commit message
last_commit_msg = subprocess.check_output(
    ["git", "log", "-1", "--pretty=%B"], text=True
).strip()

print(f"Total commits in repository: {total_commits}")
print(f"Last commit message: {last_commit_msg}")
