
from textnode import TextNode
from textnode import TextType
from textnode import text_node_to_html_node


def main():
    # hello world
    print("hello world")
    test = TextNode("Test text in main.", TextType.BOLD, "https://www.dummydomain.com")

    # Testing text_node_to_html_node. Incomplete textnode.py file function.
    text_node = TextNode(text="This is test text in the main.py file.", type=TextType.BOLD)
    text_node_to_html_node(text_node)

    print(test)

if __name__ == "__main__":
    main()
