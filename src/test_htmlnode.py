import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "random value", None, {"href": "the bizness", "paragraph": "fake.info.com"})
        node2 = HTMLNode()
        node3 = HTMLNode(children=["list item", "another list item", "garbage"], props={"i am tired": "thats too damn bad", "let me go home": "no you have to work all day", "please stop breaking stuff at the aramis solar sight": "no go fuck yourself"})
        node.props_to_html()
        node2.props_to_html()
        node3.props_to_html()