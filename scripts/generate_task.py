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
    
    # Parse requirements JSON
    try:
        requirements_dict = json.loads(requirements)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        sys.exit(1)

    # Combine template and requirements into a single prompt
    prompt = (f"Create a new programming task based on this template: {template}. "
              f"Requirements: {requirements_dict}. "
              "Also, provide a set of tests for the task and a suggested solution. "
              "Format the response as follows:\n\n"
              "### Task\n<task_description>\n\n"
              "### Tests\n<test_cases>\n\n"
              "### Solution\n<solution_code>")

    # Call OpenAI API to generate task, tests, and solution
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        response_content = response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating task: {e}")
        sys.exit(1)

    # Extract task, tests, and solution from the response
    task, tests, solution = extract_task_tests_solution(response_content)

    # Create a new branch with a unique name
    branch_name = f"task-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    create_branch(branch_name)
    commit_and_push_changes(branch_name, task, tests, solution)

def extract_task_tests_solution(content):
    # Split the content based on predefined markers
    task_marker = "### Task"
    tests_marker = "### Tests"
    solution_marker = "### Solution"

    task_start = content.find(task_marker)
    tests_start = content.find(tests_marker)
    solution_start = content.find(solution_marker)

    task = content[task_start + len(task_marker):tests_start].strip()
    tests = content[tests_start + len(tests_marker):solution_start].strip()
    solution = content[solution_start + len(solution_marker):].strip()

    return task, tests, solution

def create_branch(branch_name):
    try:
        # Create a new git branch
        subprocess.run(["git", "checkout", "-b", branch_name], check=True)
        # Use the GITHUB_TOKEN for authentication
        subprocess.run(
            ["git", "push", "-u", "origin", branch_name],
            check=True,
            env=dict(os.environ, GIT_ASKPASS='echo', GIT_USERNAME='x-access-token', GIT_PASSWORD=os.getenv('GITHUB_TOKEN'))
        )
    except subprocess.CalledProcessError as e:
        print(f"Error creating branch: {e}")
        sys.exit(1)

def commit_and_push_changes(branch_name, task_content, tests_content, solution_content):
    try:
        # Configure git
        subprocess.run(["git", "config", "--global", "user.email", "actions@github.com"], check=True)
        subprocess.run(["git", "config", "--global", "user.name", "github-actions"], check=True)
        
        # Save the generated task to a markdown file and commit the changes
        os.makedirs("tasks", exist_ok=True)
        os.makedirs(".hidden_tasks", exist_ok=True)

        task_file_path = os.path.join("tasks", "new_task.md")
        tests_file_path = os.path.join(".hidden_tasks", "new_task_tests.md")
        solution_file_path = os.path.join(".hidden_tasks", "new_task_solution.md")

        with open(task_file_path, "w") as file:
            file.write(task_content)
        with open(tests_file_path, "w") as file:
            file.write(tests_content)
        with open(solution_file_path, "w") as file:
            file.write(solution_content)

        subprocess.run(["git", "add", task_file_path, tests_file_path, solution_file_path], check=True)
        subprocess.run(["git", "commit", "-m", f"Add new task and hidden files: {branch_name}"], check=True)
        # Use the GITHUB_TOKEN for authentication
        subprocess.run(
            ["git", "push", "origin", branch_name],
            check=True,
            env=dict(os.environ, GIT_ASKPASS='echo', GIT_USERNAME='x-access-token', GIT_PASSWORD=os.getenv('GITHUB_TOKEN'))
        )
    except subprocess.CalledProcessError as e:
        print(f"Error committing and pushing changes: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if len(sys.argv) != 4:
    print("Error: Missing required command line arguments 'api_key', 'template', and 'requirements'")
    sys.exit(1)

api_key = sys.argv[1]
template = sys.argv[2]
requirements = sys.argv[3]

main(api_key, template, requirements)
