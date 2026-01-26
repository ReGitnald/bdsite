from htmlnode import *
from others import *
from markdown_blocks import *

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        stripped = line.strip()
        match = re.match(r'^#\s+(.*)', stripped)
        if match:
            return match.group(1).strip()
    raise ValueError("No header found for title extraction")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} using template {template_path} to {dest_path}")
    with open(from_path, "r", encoding="utf-8") as f:
        with open(template_path, "r", encoding="utf-8") as tf:
            template = tf.read()
            markdown = f.read()
            markdown_string = markdown_to_html_node(markdown).to_html()
            title = extract_title(markdown_string)
            final_html = template.replace("{{ Content }}", markdown_string).replace("{{ Title }}", title)
            with open(dest_path, "w", encoding="utf-8") as df:
                df.write(final_html)
