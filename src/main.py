from textnode import *
from others import *
from htmlnode import *
from markdown_blocks import *
from page_generate import *
import os
import sys

print("Starting up...")
def main():
    if sys.argv.__len__() > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    if os.path.exists("docs"):
        dir_copy_files("static", "docs", "*")
    else:
        os.mkdir("docs")
        dir_copy_files("static", "docs", "*")
    generate_pages_recursive("content", "template.html", "docs", basepath=basepath)
main()