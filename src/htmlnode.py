
class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        if self.value is None and self.children is None:
            raise ValueError("invalid HTML: no value and no children")
        if self.tag is None and self.children is None:
            return str(self.value)
        if self.children:
            children_html = ""
            for child in self.children:
                children_html += child.to_html()
            return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{str(self.value)}</{self.tag}>"

    
    def props_to_html(self):
        if self.props:
            stringup = "".join([f" {k}=\"{v}\"" for k, v in self.props.items()])
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
        html_tag = f"<{self.tag}{ props_str if props_str else ''}>{str(self.value)}</{self.tag}>"
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

