import os
import subprocess
import random
from datetime import datetime, timedelta

# Configuration
REPO_PATH = r'C:\DjnagoProjects\Projects\blog'
FILE_NAME = 'README.md'
DAYS = 5
MAX_COMMITS_PER_DAY = 17

def run_command(command):
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        raise Exception(f"Command failed with error: {result.stderr}")
    return result.stdout

def create_commits_for_day(date, num_commits):
    for _ in range(num_commits):
        file_path = os.path.join(REPO_PATH, FILE_NAME)
        with open(file_path, 'a') as file:
            file.write(f"Commit on {date} - {datetime.now()}\n")
        run_command(f'git add {FILE_NAME}')
        run_command(f'git commit -m "Commit for {date}" --date="{date}"')

def main():
    os.chdir(REPO_PATH)
    # Make sure the repo is clean
    if run_command('git status --porcelain').strip():
        raise Exception('Repository is not clean. Please commit or stash your changes.')
    
    # Create commits for the past 20 days
    start_date = datetime.now() - timedelta(days=DAYS)
    for i in range(DAYS):
        date = (start_date + timedelta(days=i)).strftime('%Y-%m-%d %H:%M:%S')
        num_commits = random.randint(0, MAX_COMMITS_PER_DAY)
        create_commits_for_day(date, num_commits)
    
    # Push changes
    run_command('git push origin main')

if __name__ == "__main__":
    main()
