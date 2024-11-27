import unittest

from htmlnode import HTMLNode, LeafNode

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
        print(repr_output)


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


if __name__ == "__main__":
    unittest.main()