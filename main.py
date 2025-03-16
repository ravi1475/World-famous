import os
import subprocess

# Use a raw string or double backslashes for Windows paths
REPO_PATH = r"C:\Users\HP\Music\Commit Folder"
BRANCH_NAME = "Main"

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Error running command: {command}")
        print(result.stderr)
        exit(1)

# Change directory to the repository
os.chdir(REPO_PATH)

# Create and switch to a new branch
run_command(f"git checkout -b {BRANCH_NAME}")

# Generate commits
for i in range(2051, 2101):
    filename = f"commit_file_{i}.txt"
    with open(filename, "w") as file:
        file.write(f"Commit number {i}")
    run_command(f"git add {filename}")
    run_command(f'git commit -m "Commit {i}"')
    print(f"✅ Commit {i} created successfully")

# Push the new branch
run_command(f"git push -u origin {BRANCH_NAME}")

# Create a pull request with GitHub CLI (ensure you have gh installed and authenticated)
run_command('gh pr create --title "Automated Commits PR" --body "This Pull Request was created by a script"')

print("🚀 All commits pushed and pull request created successfully!")
