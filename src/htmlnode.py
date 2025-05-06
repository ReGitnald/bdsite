
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