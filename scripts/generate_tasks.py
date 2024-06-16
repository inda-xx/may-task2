import openai
import subprocess
import os
import sys
import json
from datetime import datetime

# Set your OpenAI API key here
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_task(template, requirements):
    # Generate the task using the OpenAI API
    prompt = f"Create a new programming task based on this template: {template}. Requirements: {requirements}"
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()

def create_branch(branch_name):
    # Create a new git branch
    subprocess.run(["git", "checkout", "-b", branch_name], check=True)
    subprocess.run(["git", "push", "origin", branch_name], check=True)

def commit_and_push_changes(branch_name, task_content):
    # Save the generated task to a markdown file and commit the changes
    with open("new_task.md", "w") as file:
        file.write(task_content)

    subprocess.run(["git", "add", "new_task.md"], check=True)
    subprocess.run(["git", "commit", "-m", f"Add new task: {branch_name}"], check=True)
    subprocess.run(["git", "push", "origin", branch_name], check=True)

if __name__ == "__main__":
    # Get the template and requirements from the command line arguments
    template = sys.argv[1]
    requirements = sys.argv[2]
    task_content = generate_task(template, requirements)

    # Create a new branch with a unique name
    branch_name = f"task-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    create_branch(branch_name)
    commit_and_push_changes(branch_name, task_content)
