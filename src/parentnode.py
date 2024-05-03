from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, props=None):
        if tag == None:
            raise ValueError()
        super().__init__(tag, None, None, props)

    def to_html(self):
        

    
