from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    NORMAL  = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return (
                self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url
            )
        return False
    
    def __repr__(self):
       text = self.text
       text_type = self.text_type.value
       url = self.url
       combined_string = f"TextNode({text}, {text_type}, {url})"
       return combined_string


# convert a TextNode to an HTMLNode.
def text_node_to_html_node(text_node):
    text = text_node.text
    print(text)
    text_type = text_node.text_type
    print(text_type)
    if text_node.url is not None:
        # do things
    if text_node.alt is not None:
        # do things

    



