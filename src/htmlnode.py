class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        prop = ''
        if self.props is None:
            return prop
        for key, value in self.props.items():
            prop += f'{key}="{value}" '
        
        return prop.rstrip()

    def __repr__(self):
        return f"HTMLNode({self.props_to_html()})"