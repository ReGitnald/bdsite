import unittest

from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter
from extract_markdown import extract_markdown_links, extract_markdown_images


class TestTextNode(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        old_nodes = [
            TextNode("This is a *bold* text", TextType.TEXT),
            TextNode("This is normal text", TextType.TEXT),
            TextNode("*Italic* text here", TextType.TEXT)
        ]
        delimiter = "*"
        text_type = TextType.BOLD
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        expected_nodes = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
            TextNode("This is normal text", TextType.TEXT),
            TextNode("", TextType.TEXT),
            TextNode("Italic", TextType.BOLD),
            TextNode(" text here", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_extract_markdown_links(self):
        text = "This is a [link](http://example.com) in markdown."
        links = extract_markdown_links(text)
        expected_links = [("link", "http://example.com")]
        self.assertEqual(links, expected_links)
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
