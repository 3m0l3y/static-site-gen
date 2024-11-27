class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        return " ".join(f'{key}="{value}"' for key, value in self.props.items())
        
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if props is None:
            props = {}
        super().__init__(tag, value, None, props)

    def to_html(self):
        print(f"Props: {self.props}")  # Debug print
        if self.value is None:
            raise ValueError("Leaf node must have a value")
        if self.tag is None:
            return self.value
        
        props_str = self.props_to_html()  # Use the parent's method
        if props_str:
            props_str = " " + props_str  # Add a space before props if they exist
        return f'<{self.tag}{props_str}>{self.value}</{self.tag}>'
        
            



