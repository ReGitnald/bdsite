from textnode import TextNode, TextType
import re

def extract_markdown_images(text):
    return re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', text)

def extract_markdown_links(text):
    return re.findall(r'\[([^\]]+)\]\(([^)]+)\)', text)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        parts = node.text.split(delimiter)
        if len(parts)%2 == 0:
            raise ValueError("Delimiter splitting error: even number of parts means unmatched delimiter")
        for i, part in enumerate(parts):
            if i%2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        parts = re.split(r'(!\[[^\]]*\]\([^)]+\))', node.text)
        for part in parts:
            match = re.match(r'!\[([^\]]*)\]\(([^)]+)\)', part)
            if match:
                alt_text, url = match.groups()
                new_nodes.append(TextNode(alt_text, TextType.IMAGE, url=url))
            else:
                if part:
                    new_nodes.append(TextNode(part, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        parts = re.split(r'(\[[^\]]+\]\([^)]+\))', node.text)
        for part in parts:
            match = re.match(r'\[([^\]]+)\]\(([^)]+)\)', part)
            if match:
                link_text, url = match.groups()
                new_nodes.append(TextNode(link_text, TextType.LINK, url=url))
            else:
                if part:
                    new_nodes.append(TextNode(part, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    origin_node = TextNode(text, TextType.TEXT)
    nodes_after_images = split_nodes_image([origin_node])
    nodes_after_links = split_nodes_link(nodes_after_images)
    nodes_after_bold = split_nodes_delimiter(nodes_after_links, "**", TextType.BOLD)
    nodes_after_italic = split_nodes_delimiter(nodes_after_bold, "_", TextType.ITALIC)
    nodes_after_code = split_nodes_delimiter(nodes_after_italic, "`", TextType.CODE)
    return nodes_after_code