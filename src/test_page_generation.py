import unittest

from htmlnode import HTMLNode, LeafNod
from others import dir_copy_files
from page_generate import generate_page, extract_title


class TestHTMLNode(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# This is a title"
        title = extract_title(markdown)
        self.assertEqual(title, "This is a title")

        markdown = "# This is a title\n\nSome content"
        title = extract_title(markdown)
        self.assertEqual(title, "This is a title")

        markdown = "## This is a subtitle\n\nSome content"
        with self.assertRaises(ValueError):
            extract_title(markdown)