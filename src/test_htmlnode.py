import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode



class HTMLNodeTest(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "b", ["ugh", "whatever"], {"href": "garbage"})
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "b")
        self.assertEqual(node.children, ["ugh", "whatever"])
        self.assertEqual(node.props, {"href": "garbage"})
        
        node2 = HTMLNode()
        self.assertEqual(node2.tag, None)
        self.assertEqual(node2.value, None)
        self.assertEqual(node2.children, [])
        self.assertEqual(node2.props, {})
        
        
    def test_to_html(self):
        node3 = HTMLNode()
        self.assertRaises(NotImplementedError, node3.to_html)


    def test__repr__(self):
        node4 = HTMLNode("a", "b")
        self.assertEqual(node4.__repr__(), "HTMLNode(tag=a, value=b, children=[], props={})")
        
        
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
    
        
        
    if __name__ == "__main__":
        unittest.main()