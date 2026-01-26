from textnode import TextNode, TextType
import re
from enum import Enum
from htmlnode import *

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADER = "heading"
    CODE_BLOCK = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown): 
    lines = markdown.split("\n")
    blocks = []
    current_block = []
    for line in lines:
        stripped_line = line.strip()
        if stripped_line == "":
            if current_block:
                blocks.append("\n".join(current_block))
                current_block = []
        else:
            current_block.append(line)
    if current_block:
        blocks.append("\n".join(current_block))
    return blocks

def block_to_block_type(block):
    stripped = block.strip()
    lines = block.split("\n")
    if re.match(r'^(#{1,6})\s+', stripped):
        return BlockType.HEADER
    if stripped.startswith("```\n") and stripped.endswith("```"):
        return BlockType.CODE_BLOCK
    if all(line.startswith("> ") for line in lines):
        return BlockType.QUOTE
    if all(re.match(r'-\s', line) for line in lines):
        return BlockType.UNORDERED_LIST
    if all(re.match(rf'{i+1}\.\s', line) for i, line in enumerate(lines)):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            p_node = HTMLNode("p")
            p_node.children = text_to_textnodes(block)
            html_nodes.append(p_node)
        elif block_type == BlockType.HEADER:
            match = re.match(r'^(#{1,6})\s+(.*)', block.strip())
            if match:
                hashes, content = match.groups()
                level = len(hashes)
                h_node = HTMLNode(f"h{level}")
                h_node.children = text_to_textnodes(content)
                html_nodes.append(h_node)
        elif block_type == BlockType.CODE_BLOCK:
            code_content = block.strip()[3:-3].strip()
            code_node = HTMLNode("pre")
            code_child = HTMLNode("code")
            code_child.value = code_content
            code_node.children.append(code_child)
            html_nodes.append(code_node)
        elif block_type == BlockType.QUOTE:
            quote_node = HTMLNode("blockquote")
            quote_content = "\n".join(line[2:] for line in block.split("\n"))
            quote_node.children = text_to_textnodes(quote_content)
            html_nodes.append(quote_node)
        elif block_type == BlockType.UNORDERED_LIST:
            ul_node = HTMLNode("ul")
            for line in block.split("\n"):
                li_content = line[2:].strip()
                li_node = HTMLNode("li")
                li_node.children = text_to_textnodes(li_content)
                ul_node.children.append(li_node)
            html_nodes.append(ul_node)
        elif block_type == BlockType.ORDERED_LIST:
            ol_node = HTMLNode("ol")
            for line in block.split("\n"):
                li_content = re.sub(r'^\d+\.\s', '', line).strip()
                li_node = HTMLNode("li")
                li_node.children = text_to_textnodes(li_content)
                ol_node.children.append(li_node)
            html_nodes.append(ol_node)