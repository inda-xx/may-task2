import os
import sys
import json
import random
from openai import OpenAI
from datetime import datetime

def main(key, template, requirements):

    client = OpenAI(api_key=key)

    # Parse requirements
    requirements_dict = json.loads(requirements)

    # Template and requirements into a single prompt
    prompt = f"Create a new programming task based on this template: {template}. Requirements: {requirements_dict}"


    response = client.completions.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )

    task_content = response.choices[0].text.strip()

    # Create a new branch 
    branch_name = f"task-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    create_branch(branch_name)
    commit_and_push_changes(branch_name, task_content)

def create_branch(branch_name):
    try:
        # Create a new git branch
        subprocess.run(["git", "checkout", "-b", branch_name], check=True)
        subprocess.run(["git", "push", "origin", branch_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error creating branch: {e}")
        sys.exit(1)

def commit_and_push_changes(branch_name, task_content):
    try:
        # Save generated task to a markdown file and commit
        os.makedirs("tasks", exist_ok=True)
        with open("tasks/new_task.md", "w") as file:
            file.write(task_content)

        subprocess.run(["git", "add", "tasks/new_task.md"], check=True)
        subprocess.run(["git", "commit", "-m", f"Add new task: {branch_name}"], check=True)
        subprocess.run(["git", "push", "origin", branch_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error committing and pushing changes: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Error: Missing required command line arguments 'api_key', 'template', and 'requirements'")
        sys.exit(1)
    
    api_key = sys.argv[1]
    template = sys.argv[2]
    requirements = sys.argv[3]
    
    main(api_key, template, requirements)
