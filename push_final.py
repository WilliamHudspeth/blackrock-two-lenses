import os
import subprocess
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env'))

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
remote_url = f"https://x-access-token:{GITHUB_TOKEN}@github.com/WilliamHudspeth/blackrock-two-lenses.git"

subprocess.run('git add .', shell=True)
subprocess.run('git commit -m "Sync final $906 charts, updated documents, and add MIT License"', shell=True)
result = subprocess.run(f'git push {remote_url} main', shell=True, capture_output=True, text=True)

if result.returncode == 0:
    print("Success")
else:
    print(result.stderr)
