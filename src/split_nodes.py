import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            parts = node.text.split(delimiter)
            if len(parts) == 2:
                raise Exception(f"Delimiter not closed. Improper Markdown syntax.")
            if len(parts) >= 3:
                result.append(TextNode(parts[0], TextType.TEXT))
                result.append(TextNode(parts[1], text_type))
                result.append(TextNode(parts[2], TextType.TEXT))
            else:
                result.append(node)
        else:
            result.append(node)
    return result


def extract_markdown_images(text):
    links = re.findall(r"\((.*?)\)", text)
    result_tuple = tuple(links)
    return result_tuple
