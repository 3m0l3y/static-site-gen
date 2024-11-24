
from textnode import TextNode
from textnode import TextType


def main():
    # hello world
    print("hello world")
    test = TextNode("Test text in main.", TextType.BOLD, "https://www.dummydomain.com")
    print(test)

if __name__ == "__main__":
    main()
