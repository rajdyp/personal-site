import yaml
import os
from jinja2 import Environment, FileSystemLoader

# Setup Jinja
template_dir = 'templates' 
loader = FileSystemLoader(template_dir)
env = Environment(
    loader=loader
)
template = env.get_template("index.html")

# Read YAML data
resume_path = "data/resume.yaml"
with open(resume_path, "r") as f:
    data = yaml.safe_load(f)

# Render and save HTML  
output_html = template.render(resume=data["resume"])

docs_dir = "docs"
os.makedirs(docs_dir, exist_ok=True) 

docs_path = os.path.join(docs_dir, "index.html")

# Write the final HTML to the file
with open(docs_path, "w") as f:
    f.write(output_html)

print(f"Successfully generated resume website at: {docs_path}")