import os
import sys
import json
import subprocess
from datetime import datetime
from openai import OpenAI
import pytz
from pytz import timezone

def main(api_key):
    if not api_key:
        print("Error: OpenAI API key is missing.")
        sys.exit(1)

    client = OpenAI(api_key=api_key)

    # Read the template file
    try:
        with open("task_template.md", "r") as file:
            template = file.read()
    except FileNotFoundError:
        print("Error: task_template.md file not found.")
        sys.exit(1)

    # Read the existing code and tests
    try:
        with open("src/Indamon.java", "r") as file:
            existing_code = file.read()
        with open("src/IndamonTest.java", "r") as file:
            existing_tests = file.read()
    except FileNotFoundError:
        print("Error: Indamon.java or IndamonTest.java file not found.")
        sys.exit(1)

    # Extract requirements JSON and theme from environment variables
    requirements_str = os.getenv("REQUIREMENTS_JSON", '{"difficulty": "medium", "language": "Java"}')
    theme = os.getenv("TASK_THEME", "Create a basic Java application with the following requirements.")

    try:
        requirements_dict = json.loads(requirements_str)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        sys.exit(1)

    # Combine template, theme, requirements, existing code, and existing tests into a single prompt
    prompt = (f"Create a new programming task based on this template: {template}. "
              f"Theme: {theme}. "
              f"Requirements: {requirements_dict}. "
              "Use the following existing code and tests as inspiration. Ensure that the new generated tasks are detailed, aesthetically pleasing, and provide thorough instructions for the students. "
              "The new task must include specific function names where necessary and be compatible with the provided tests. "
              "Provide a set of tests for the task and a suggested solution. The tests must be extremely thorough, robust, and detailed, covering all edge cases, including invalid inputs, boundary conditions, and performance considerations. The tests should be similar to the provided tests and must be of high quality as they will be used for student assessment and grading. "
              "The task description must include the name of the test class and the test methods for the functions in the task. "
              "The code template must be very detailed and coordinated with the task description and tests, ensuring the correct function names and return types are used so that the tests pass. "
              "Format the response as follows:\n\n"
              "### Task\n<task_description>\n\n"
              "### Template\n<template_code>\n\n"
              "### Tests\n<test_cases>\n\n"
              "### Solution\n<solution_code>\n\n"
              f"### Existing Code\n{existing_code}\n\n"
              f"### Existing Tests\n{existing_tests}")

    # Call OpenAI API to generate task, template, tests, and solution
    response_content = generate_with_retries(client, prompt, max_retries=3)
    if response_content is None:
        print("Error: Failed to generate task after multiple retries.")
        sys.exit(1)

    # Extract task, template, tests, and solution from the response
    task, template, tests, solution = extract_task_template_tests_solution(response_content)

    # Create a new branch with a unique name
    stockholm_tz = timezone('Europe/Stockholm')
    branch_name = f"task-{datetime.now(stockholm_tz).strftime('%Y%m%d%H%M%S')}"
    create_branch(branch_name)
    commit_and_push_changes(branch_name, task, template, tests, solution)

def generate_with_retries(client, prompt, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error generating task: {e}")
            if attempt < max_retries - 1:
                print("Retrying...")
    return None

def extract_task_template_tests_solution(content):
    # Split the content based on predefined markers
    task_marker = "### Task"
    template_marker = "### Template"
    tests_marker = "### Tests"
    solution_marker = "### Solution"

    task_start = content.find(task_marker)
    template_start = content.find(template_marker)
    tests_start = content.find(tests_marker)
    solution_start = content.find(solution_marker)

    task = content[task_start + len(task_marker):template_start].strip()
    template = content[template_start + len(template_marker):tests_start].strip()
    tests = content[tests_start + len(tests_marker):solution_start].strip()
    solution = content[solution_start + len(solution_marker):].strip()

    return task, template, tests, solution

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

def commit_and_push_changes(branch_name, task_content, template_content, tests_content, solution_content):
    try:
        # Configure git
        subprocess.run(["git", "config", "--global", "user.email", "actions@github.com"], check=True)
        subprocess.run(["git", "config", "--global", "user.name", "github-actions"], check=True)
        
        # Save the generated task to a markdown file and commit the changes
        os.makedirs("tasks", exist_ok=True)
        os.makedirs("src", exist_ok=True)
        os.makedirs(".hidden_tasks", exist_ok=True)

        task_file_path = os.path.join("tasks", "new_task.md")
        template_file_path = os.path.join("src", "template_code.java")  # Adjust extension based on language
        tests_file_path = os.path.join(".hidden_tasks", "new_task_tests.java")  # Adjust extension based on language
        solution_file_path = os.path.join(".hidden_tasks", "new_task_solution.java")  # Adjust extension based on language

        with open(task_file_path, "w") as file:
            file.write(task_content)
        with open(template_file_path, "w") as file:
            file.write(template_content)
        with open(tests_file_path, "w") as file:
            file.write(tests_content)
        with open(solution_file_path, "w") as file:
            file.write(solution_content)

        subprocess.run(["git", "add", task_file_path, template_file_path, tests_file_path, solution_file_path], check=True)
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

if len(sys.argv) != 2:
    print("Error: Missing required command line argument 'api_key'")
    sys.exit(1)

api_key = sys.argv[1]

main(api_key)
