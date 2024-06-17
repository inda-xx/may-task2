import sys
import yaml

def load_feedback(feedback_file):
    with open(feedback_file, 'r') as file:
        lines = file.readlines()
        feedback = [line.strip() for line in lines if line.startswith('- ')]
    return feedback

def customize_task(feedback, template_file, output_file):
    with open(template_file, 'r') as file:
        template = yaml.safe_load(file)

    task_customizations = []
    for item in feedback:
        if 'test' in item:
            task_customizations.append("Focus on passing all tests.")
        if 'style' in item:
            task_customizations.append("Improve your coding style.")
        if 'efficiency' in item:
            task_customizations.append("Optimize your code for better efficiency.")
        if 'documentation' in item:
            task_customizations.append("Enhance your code documentation.")

    task_customizations = "\n".join(task_customizations)
    customized_task = template.replace("{customizations}", task_customizations)

    with open(output_file, 'w') as file:
        file.write(customized_task)

if __name__ == "__main__":
    feedback_file = sys.argv[1]
    template_file = sys.argv[2]
    output_file = sys.argv[3]

    feedback = load_feedback(feedback_file)
    customize_task(feedback, template_file, output_file)
