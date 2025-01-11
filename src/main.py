
from textnode import TextNode
from textnode import TextType
from textnode import text_node_to_html_node
from split_nodes import split_nodes_delimiter


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

    print(f"testing main.py")

if __name__ == "__main__":
    main()
