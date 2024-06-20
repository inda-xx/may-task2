import os
import sys
import json
import subprocess
from datetime import datetime
from openai import OpenAI

def main(api_key, template, requirements):
    if not api_key:
        print("Error: OpenAI API key is missing.")
        sys.exit(1)

    client = OpenAI(api_key=api_key)
    
    # Parse requirements 
    try:
        requirements_dict = json.loads(requirements)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        sys.exit(1)

    # Combine template and requirements 
    prompt = f"Create a new programming task based on this template: {template}. Requirements: {requirements_dict}"

    
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        task_content = response.choices[0].message["content"].strip()
    except Exception as e:
        print(f"Error generating task: {e}")
        sys.exit(1)

    # Create a new branch
    branch_name = f"task-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    create_branch(branch_name)
    commit_and_push_changes(branch_name, task_content)

def create_branch(branch_name):
    try:
        # Create new git branch
        subprocess.run(["git", "checkout", "-b", branch_name], check=True)
        subprocess.run(["git", "push", "origin", branch_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error creating branch: {e}")
        sys.exit(1)

def commit_and_push_changes(branch_name, task_content):
    try:
        # Save the generated task to a markdown file and commit changes
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
