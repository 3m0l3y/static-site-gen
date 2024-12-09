
from textnode import TextNode
from textnode import TextType
from textnode import text_node_to_html_node


def main():
    # hello world
    print("hello world")
    test = TextNode("Test text in main.", TextType.BOLD, "https://www.dummydomain.com")
    test_text = "This is test text in the main.py file."
    text_node_to_html_node(test_text)
    print(test)

if __name__ == "__main__":
    main()
