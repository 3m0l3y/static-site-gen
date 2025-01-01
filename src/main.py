
from textnode import TextNode
from textnode import TextType
from textnode import text_node_to_html_node
from parse_text import split_nodes_delimiter


def main():
    # hello world
    print("hello world")
    test = TextNode("Test text in main.", TextType.BOLD, "https://www.dummydomain.com")

    # Testing text_node_to_html_node. Incomplete textnode.py file function.
    text_node = TextNode(text="This is test text in the main.py file.", text_type=TextType.BOLD)
    text_node_to_html_node(text_node)

    print(test)



    # Create a sample TextNode
    node = TextNode("This is a `code example`.", TextType.TEXT)

    # Call the split_nodes_delimiter function
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
'''
    # Check the output
    for new_node in new_nodes:
        print(new_node.content, new_node.text_type)
'''


if __name__ == "__main__":
    main()
