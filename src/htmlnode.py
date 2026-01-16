
class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is not None:
            stringup = " ".join([f"{k}={v}" for k, v in self.props.items()])
        else:
            stringup = ""
        return stringup
    
    def __repr__(self):
        return f" tag is {self.tag}, value is {self.value}, children are {self.children}, properties are \n {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value,  props=None) :
        super().__init__(tag = tag, value = value, props = props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf Node must have a value")
        if self.tag is None:
            return str(self.value)
        props_str = self.props_to_html()
        html_tag = f"<{self.tag}{' ' + props_str if props_str else ''}>{str(self.value)}</{self.tag}>"
        return html_tag
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid HTML: no tag")
        if self.children is None:
            raise ValueError("invalid HTML: no children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

def text_node_to_html_node(text_node):
    if text_type := text_node.text_type == 'NORMAL':
        return LeafNode(tag=None, value=text_node.text)
    elif text_type == 'BOLD':
        return LeafNode(tag='b', value=text_node.text)
    elif text_type == 'ITALICS':
        return LeafNode(tag='i', value=text_node.text)
    elif text_type == 'CODE':
        return LeafNode(tag='code', value=text_node.text)
    elif text_type == 'LINK':
        return LeafNode(tag='a', value=text_node.text, props={'href': text_node.url})
    elif text_type == 'IMAGE':
        return LeafNode(tag='img', value='', props={'src': text_node.url, 'alt': text_node.text})
    else:
        raise ValueError(f"Unknown text type: {text_node.text_type}")