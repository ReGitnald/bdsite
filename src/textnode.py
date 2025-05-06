from enum import Enum

# TextType = Enum('TType', ['NORMAL', 'BOLD', 'ITALICS', 'CODE', 'LINK', 'IMAGE'])
class TextType(Enum):
    NORMAL, BOLD, ITALICS, CODE, LINK, IMAGE = 'NORMAL', 'BOLD', 'ITALICS', 'CODE', 'LINK', 'IMAGE'

class TextNode():
    def __init__(self, content, ttype, url = None):
        self.text = content
        self.text_type = ttype
        self.url = url

    def __eq__(self, TextNode2):
        return (self.text == TextNode2.text and self.text_type == TextNode2.text_type
                and self.url == TextNode2.url)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    