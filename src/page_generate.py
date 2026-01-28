from htmlnode import *
from others import *
from markdown_blocks import *
import os


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        stripped = line.strip()
        match = re.match(r'^#\s+(.*)', stripped)
        if match:
            return match.group(1).strip()
    raise ValueError("No header found for title extraction")

def generate_page(from_path, template_path, dest_path, basepath = "/"):
    print(f"Generating page from {from_path} using template {template_path} to {dest_path}")
    with open(from_path, "r", encoding="utf-8") as f:
        with open(template_path, "r", encoding="utf-8") as tf:
            template = tf.read()
            markdown = f.read()
            title = extract_title(markdown)
            markdown_string = markdown_to_html_node(markdown).to_html()
            final_html = template.replace("{{ Content }}", markdown_string).replace("{{ Title }}", title)
            final_html = final_html.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
            with open(dest_path, "w", encoding="utf-8") as df:
                df.write(final_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath = "/"):
    print(dir_path_content, dest_dir_path)
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    for item in os.listdir(dir_path_content):
        item_path = os.path.join(dir_path_content, item)
        dest_item_path = os.path.join(dest_dir_path, item)
        if os.path.isdir(item_path):
            generate_pages_recursive(item_path, template_path, dest_item_path, basepath)
        elif item.endswith(".md"):
            dest_html_path = dest_item_path[:-3] + ".html"
            generate_page(item_path, template_path, dest_html_path, basepath)