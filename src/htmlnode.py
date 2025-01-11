from textnode import TextNode, TextType


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
        #print(f"Props: {self.props}")  # Debug print
        if self.value is None:
            raise ValueError("Leaf node must have a value")
        if self.tag is None:
            return self.value
        
        props_str = self.props_to_html()  # Use the parent's method
        if props_str:
            props_str = " " + props_str  # Add a space before props if they exist
        return f'<{self.tag}{props_str}>{self.value}</{self.tag}>'
        
            
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if props is None:
            props = {}
        #print(f"Children initialized: {children}")  # Debug   
        super().__init__(tag=tag, children=children, props=props)
        #print(f"Initializing ParentNode with children: {self.children}")


    def to_html(self):

        #print(f"Tag: {self.tag}")  # Debug print
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        
        #print(f"Converting to HTML. Tag: {self.tag}, Children: {self.children}")  # Debug
        if self.children is None:
            raise ValueError("ParentNode must have children")
        
        if not self.tag:
            raise ValueError("ParentNode must have a tag")

        if not self.children:
            raise ValueError("ParentNode must have children")
        
        html_string = ""
        for child in self.children:
            if isinstance(child, LeafNode) or isinstance(child, ParentNode):
                html_string += child.to_html()
            else:
             raise ValueError("Unexpected Error building parent to children nodes")
        return f'<{self.tag}>{html_string}</{self.tag}>'
                

# convert a TextNode to a HTMLNode.
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b",text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code",text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt":text_node.text})
    else:
        raise ValueError("Unknown TextType")
    

    




