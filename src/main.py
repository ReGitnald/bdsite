from textnode import *
from others import *
from htmlnode import *
from markdown_blocks import *
import os
print("Hello world")
def main():
    tn = TextNode( "dink doink", TextType.BOLD, "www.boot.dev")
    print(tn)
    if os.path.exists("public"):
        dir_copy_files("static", "public", "*")
    else:
        os.mkdir("public")
        dir_copy_files("static", "public", "*")
main()