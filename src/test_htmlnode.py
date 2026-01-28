import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        paragraph = HTMLNode(tag="p", value="This is a paragraph")
        link = HTMLNode(
            tag="a", 
            value="Click me", 
            props={"href": "https://boot.dev", "target": "_blank"}
        )
        heading = HTMLNode(tag="h2", value="Section Title")
        div = HTMLNode(
            tag="div",
            children=[
                HTMLNode(tag="h1", value="Title"),
                HTMLNode(tag="p", value="Content goes here")
            ]
         )       
        text = HTMLNode(value="Just some plain text")
        # print(div)
        print(link.props_to_html())
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node2.to_html(), "<a href=https://www.google.com>Click me!</a>")



if __name__ == "__main__":
    unittest.main()