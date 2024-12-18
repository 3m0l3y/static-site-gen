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


# convert a TextNode to an HTMLNode. # Not complete
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.NORMAL:
        # handle NORMAL type
        print(text_node.text_type)
    elif text_node.text_type == TextType.BOLD:
        # handle BOLD type
        # and so on for other TextTypes...
        print(text_node.text_type)
    elif text_node.text_type == TextType.ITALIC:
        # handle ITALIC type
        # and so on for other TextTypes...
        print(text_node.text_type)
    elif text_node.text_type == TextType.CODE:
        # handle CODE type
        # and so on for other TextTypes...
        print(text_node.text_type)
    elif text_node.text_type == TextType.LINK:
        # handle LINK type
        # and so on for other TextTypes...
        print(text_node.text_type)
    elif text_node.text_type == TextType.IMAGE:
        # handle IMAGE type
        # and so on for other TextTypes...
        print(text_node.text_type)
    else:
        raise ValueError("Unknown TextType")
    

    



