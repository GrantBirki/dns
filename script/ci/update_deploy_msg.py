import jinja2
import os

results = os.environ.get('MSG', False)

# Set up the Jinja2 environment and change variable syntax to [[ ]]
environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader('.'),
    variable_start_string='[[',
    variable_end_string=']]',
)

# Load the template from a file
template = environment.get_template('.github/deployment_message.md')

# Define the variables to be inserted
variables = {
    "results": results
}

# Render the template with the provided variables
rendered_template = template.render(variables)

# Print the rendered template
print(rendered_template)
