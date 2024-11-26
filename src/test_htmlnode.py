import unittest

from htmlnode import HTMLNode

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


if __name__ == "__main__":
    unittest.main()