import pandas as pd
from jinja2 import Template

# Load the CSV data
csv_file = 'schedule.csv'
data = pd.read_csv(csv_file)
data.fillna('', inplace=True)
data = data.astype(str)
data['Lecture #'] = data['Lecture #'].apply(lambda x: str(int(float(x))) if x != '' else x)

template_path = 'schedule_template.html'
with open(template_path, 'r') as file:  # r to open file in READ mode
    html_template = file.read()
# Create Jinja2 template
template = Template(html_template)

# Render the HTML
html_output = template.render(data=data)

# Save the HTML to a file
output_file = '../schedule.html'

with open(output_file, 'w') as f:
    f.write(html_output)

print(f"HTML generated and saved to '{output_file}'")
