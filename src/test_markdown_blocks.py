import unittest

from textnode import TextNode, TextType
from others import *
from markdown_blocks import *


class TestMarkdownBlocks(unittest.TestCase):
    def test_block_to_block_type(self):
        paragraph = "This is a simple paragraph."
        header = "## This is a header"
        code_block = "```\nprint('Hello, World!')\n```"
        quote = "> This is a quote.\n> It has two lines."
        unordered_list = "- Item 1\n- Item 2\n- Item 3"
        ordered_list = "1. First item\n2. Second item\n3. Third item"

        self.assertEqual(block_to_block_type(paragraph), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(header), BlockType.HEADER)
        self.assertEqual(block_to_block_type(code_block), BlockType.CODE_BLOCK)
        self.assertEqual(block_to_block_type(quote), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(unordered_list), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type(ordered_list), BlockType.ORDERED_LIST)