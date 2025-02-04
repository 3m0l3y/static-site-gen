
from textnode import TextNode
from textnode import TextType
from htmlnode import text_node_to_html_node
from split_nodes import split_nodes_delimiter, extract_markdown_images


def main():
    # hello world
    print("hello world")
    test = TextNode("Test text in main.", TextType.BOLD, "https://www.dummydomain.com")

    # Testing text_node_to_html_node. Incomplete textnode.py file function.
    text_node = TextNode(text="This is test text in the main.py file.", text_type=TextType.BOLD)
    text_node_to_html_node(text_node)

    print(test)

    # Testing split_nodes.py Create a sample TextNode
    node = TextNode("This is a `code example`.", TextType.TEXT)
    # Call the split_nodes_delimiter function
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

    # Start with one node containing all the text
    initial_nodes = [TextNode("This is **bold** and `code` text", TextType.TEXT)]

    # First pass - handle bold
    after_bold = split_nodes_delimiter(initial_nodes, "**", TextType.BOLD)

    # Second pass - handle code (passing in the nodes from first pass)
    after_code = split_nodes_delimiter(after_bold, "`", TextType.CODE)

    #Testing splitnodes extract links
    test_node = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(test_node))


    print(f"testing main.py bootdev sync with Git")

if __name__ == "__main__":
    main()
