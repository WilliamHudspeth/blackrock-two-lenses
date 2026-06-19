import os
import subprocess
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env'))

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
if not GITHUB_TOKEN:
    print("Error: GITHUB_TOKEN not found in .env")
    exit(1)

def run_cmd(cmd):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error executing {cmd}:")
        print(result.stderr)
    else:
        print(result.stdout)
    return result.returncode == 0

# Remove create_repo.py
if os.path.exists('create_repo.py'):
    os.remove('create_repo.py')

# Initialize git
run_cmd('git init')

# Configure git if not configured
run_cmd('git config user.email "wshb@example.com"')
run_cmd('git config user.name "WilliamHudspeth"')

# Add all files
run_cmd('git add .')

# Commit
run_cmd('git commit -m "Initial commit: BlackRock Two Lenses project framework"')

# Add remote
remote_url = f"https://x-access-token:{GITHUB_TOKEN}@github.com/WilliamHudspeth/blackrock-two-lenses.git"
run_cmd('git branch -M main')
run_cmd(f'git remote add origin {remote_url}')

# Push
print("Pushing to remote...")
result = subprocess.run('git push -u origin main', shell=True, capture_output=True, text=True)
if result.returncode != 0:
    print("Error pushing:")
    print(result.stderr)
else:
    print(result.stdout)

# Remove remote with token to be safe
run_cmd('git remote remove origin')
run_cmd('git remote add origin https://github.com/WilliamHudspeth/blackrock-two-lenses.git')
