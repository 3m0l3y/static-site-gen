import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextNode, TextType


class TestHTMLNode(unittest.TestCase):

    def test_html_initialization(self):  # Include 'self' here
        node = HTMLNode("p", "Hello, World!", [], {"class": "intro"})

        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello, World!")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "intro"})

        default_node = HTMLNode()

        self.assertIsNone(default_node.tag)
        self.assertIsNone(default_node.value)
        self.assertIsNone(default_node.children)
        self.assertIsNone(default_node.props)


    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        result = node.props_to_html()
        expected = 'href="https://www.google.com" target="_blank"'

        self.assertEqual(result, expected)
        

    def test__rpr__(self):
        node = HTMLNode(tag="h1", value="The heading text is an h1 tag", children=["listvalue1", "listvalue2", "listvalue3"], props={"href": "https://boot.dev", "target": "_blank"})
        repr_output = repr(node)
        #print(repr_output)


    def test_leaf_node(self):
        node1 = LeafNode("p", "Hello, world!")
        self.assertEqual(node1.to_html(), "<p>Hello, world!</p>")

        node2 = LeafNode("a", "Click Here!", {'href':'https://www.google.com', 'target':'_blank'})
        self.assertEqual(node2.to_html(), '<a href="https://www.google.com" target="_blank">Click Here!</a>')
        
        # Test raw text (no tag)
        node3 = LeafNode(None, "Just some text")
        self.assertEqual(node3.to_html(), "Just some text")

        # Test invalid case (no value)
        with self.assertRaises(ValueError):
            node4 = LeafNode("p", None)
            node4.to_html()


    def test_parent_node(self):
        # Test multiple leaf children
        li1 = LeafNode("li", "List item 1")
        li2 = LeafNode("li", "List item 2")
        li3 = LeafNode("li", "List item 3")
        ul_list = ParentNode("ul", [li1, li2, li3])
        #print(ul_list.children)
        self.assertEqual(ul_list.to_html(), "<ul><li>List item 1</li><li>List item 2</li><li>List item 3</li></ul>")

        # Test single leaf child
        sp1 = LeafNode("span", "Span item 1")
        div1 = ParentNode("div", [sp1])
        #print(div1.children)
        self.assertEqual(div1.to_html(), "<div><span>Span item 1</span></div>")

        # Test when parent has no tag
        li1 = LeafNode("li", "List item 1")
        li2 = LeafNode("li", "List item 2")
        li3 = LeafNode("li", "List item 3")
        ul_list = ParentNode(None, [li1, li2, li3])
        #print(f"Debug - ul_list.tag: {ul_list.tag}") 
        with self.assertRaises(ValueError):
            ul_list.to_html()

        # Test when there are no children
        ul_empty = ParentNode("ul", [])
        with self.assertRaises(ValueError):
            ul_empty.to_html()

        # Nested ParentNode objects
        parent = ParentNode("div", [
            ParentNode("p", [
            LeafNode("b", "Hello")
            ])
        ])
        self.assertEqual(parent.to_html(), "<div><p><b>Hello</b></p></div>")

        # Nested LeafNode objects
        inner_items = [
            LeafNode("li", "List1"),
            LeafNode("li", "List2"),
            LeafNode("li", "List3")
        ]
        inner_ul = ParentNode("ul", inner_items)
        outer_li = ParentNode("li", [inner_ul])
        parent = ParentNode("div", [
            ParentNode("ul", [outer_li])
        ])
        self.assertEqual(parent.to_html(), "<div><ul><li><ul><li>List1</li><li>List2</li><li>List3</li></ul></li></ul></div>")


    def test_text_node_to_html_node(self):
        text_node = TextNode("Hello, text only!", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        assert html_node.value == "Hello, text only!"
        
        text_node = TextNode("Hello, world!", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == "b"
        assert html_node.value == "Hello, world!"

        text_node2 = TextNode("SUP FOO!", TextType.ITALIC)
        html_node2 = text_node_to_html_node(text_node2)
        assert html_node2.tag == "i"
        assert html_node2.value == "SUP FOO!"

        text_node3 = TextNode("Website Link:", TextType.LINK, "https://www.nonsenselink.com")
        html_node3 = text_node_to_html_node(text_node3)
        assert html_node3.tag == "a"
        assert html_node3.value == "Website Link:"
        assert html_node3.props["href"] == "https://www.nonsenselink.com"

        text_node4 = TextNode("some alternative text", TextType.IMAGE, "https://example.com/image.jpg")
        html_node4 = text_node_to_html_node(text_node4)
        assert html_node4.tag == "img"
        assert html_node4.props["src"] == "https://example.com/image.jpg"
        assert html_node4.props["alt"] == "some alternative text"






if __name__ == "__main__":
    unittest.main()