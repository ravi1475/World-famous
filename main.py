import os

# Set your repo path here
REPO_PATH = "path/to/your/repository"



# Loop to create 150 commits
for i in range(1751, 1901):
    filename = f"commit_file_{i}.txt"
    
    # Create/modify a file to ensure changes for each commit
    with open(filename, "w") as file:
        file.write(f"Commit number {i}")
    
    # Git commands to add, commit, and push
    os.system(f"git add {filename}")
    os.system(f'git commit -m "Commit {i}"')
    print(f"✅ Commit {i} created successfully")

print("🚀 All commits created successfully. Now push them manually:")
print("git push origin main")
