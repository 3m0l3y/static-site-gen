from enum import Enum

class TextType(Enum):
    NORMAL  = "normal"
    BOLD = "bold"
    ITALICT = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"

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
