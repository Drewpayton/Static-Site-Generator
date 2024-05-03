from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children,  props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        results = ""
        if self.tag is None:
            raise ValueError("No tag")
        if self.children is None:
            raise ValueError("No Children")
        
        for child in self.children:
            results += child.to_html()

        return f'<{self.tag}{self.props_to_html()}>{results}</{self.tag}>'

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
    
