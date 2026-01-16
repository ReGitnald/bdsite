import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        node3 = TextNode("This is a different text node", TextType.BOLD)
        node4 = TextNode("This is a text node", TextType.ITALICS)
        node5 = TextNode("This is a text node", TextType.BOLD, url = "www.fml.com")
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node2, node4)
        self.assertNotEqual(node, node5)
def test_text(self):
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "This is a text node")



if __name__ == "__main__":
    unittest.main()
