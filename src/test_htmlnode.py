import unittest
from htmlnode import HTMLNode  # Adjust import based on your file structure

class TestHTMLNode(unittest.TestCase):

    def test_creation_no_attributes(self):
        """Test creating an HTMLNode without any attributes."""
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

    def test_props_to_html(self):
        """Test the props_to_html method."""
        node = HTMLNode(tag="a", value="Click Here", props={
            "href": "https://www.example.com",
            "target": "_blank"
        })
        props_html = node.props_to_html()
        self.assertEqual(props_html, 'href="https://www.example.com" target="_blank"')

    def test_repr_method(self):
        """Test the __repr__ method for the HTMLNode."""
        node = HTMLNode(tag="p", value="This is a paragraph.", props={
            "class": "text-center"
        })
        repr_str = repr(node)
        self.assertIn('HTMLNode(tag=p', repr_str)
        self.assertIn('value=This is a paragraph.', repr_str)
        self.assertIn('props={\'class\': \'text-center\'}', repr_str)

if __name__ == "__main__":
    unittest.main()
