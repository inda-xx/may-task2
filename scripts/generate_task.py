import os
import sys
import json
from openai import OpenAI
from datetime import datetime

def main(api_key, template, requirements):

    client = OpenAI(api_key=api_key)

    # Parse requirements JSON
    requirements_dict = json.loads(requirements)

    # Combine template and requirements into a single prompt
    prompt = f"Create a new programming task based on this template: {template}. Requirements: {requirements_dict}"

    # Call OpenAI API to generate task
    response = client.completions.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )

    task_content = response.choices[0].text.strip()

    # Save the generated task to a markdown file
    os.makedirs("tasks", exist_ok=True)
    with open("tasks/new_task.md", "w") as file:
        file.write(task_content)
    
    # Set output variables for the workflow
    print(f"::set-output name=task_content::{task_content}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Error: Missing required command line arguments 'api_key', 'template', and 'requirements'")
        sys.exit(1)
    
    api_key = sys.argv[1]
    template = sys.argv[2]
    requirements = sys.argv[3]
    
    main(api_key, template, requirements)
