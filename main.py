import os
from src.common import utils
from src.modules.interfaces import Module
from src.modules import *


# Compile assignments into a list
assignments = {}
modules = [
    Gradescope()
]
for module in modules:
    module.run(assignments)

# Update GitHub workflow with all environment variables
workflow_template = utils.load_template('workflow_template.yml')
envs = [x + ': ${{ secrets.' + x + ' }}' for x in Module.envs]
workflow = workflow_template.replace(
    '__ENV__',
    ('\n' + ' ' * 8).join(envs)
)
with open(os.path.join('.github', 'workflows', 'main.yml'), 'w') as file:
    file.write(workflow)

# Save the list to a JavaScript file for Planit to import later
utils.save_data('assignments', assignments)
