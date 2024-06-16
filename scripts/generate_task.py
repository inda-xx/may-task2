import openai
import subprocess
import os
import sys
import json
from datetime import datetime

# Set your OpenAI API key here
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_task(template, requirements):
    try:
        # Generate the task using the new OpenAI API
        prompt = f"Create a new programming task based on this template: {template}. Requirements: {requirements}"
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error generating task: {e}")
        sys.exit(1)

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
        # Save the generated task to a markdown file and commit the changes
        with open("tasks/new_task.md", "w") as file:
            file.write(task_content)

        subprocess.run(["git", "add", "tasks/new_task.md"], check=True)
        subprocess.run(["git", "commit", "-m", f"Add new task: {branch_name}"], check=True)
        subprocess.run(["git", "push", "origin", branch_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error committing and pushing changes: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Get the template and requirements from the command line arguments
    try:
        template = sys.argv[1]
        requirements = sys.argv[2]
    except IndexError:
        print("Error: Missing required command line arguments 'template' and 'requirements'")
        sys.exit(1)
    
    task_content = generate_task(template, requirements)

    # Create a new branch with a unique name
    branch_name = f"task-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    create_branch(branch_name)
    commit_and_push_changes(branch_name, task_content)
