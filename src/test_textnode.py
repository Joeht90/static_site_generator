import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        node3 = TextNode("Test number two", TextType.ITALIC, "https://www.fakeweb.biz")
        node4 = TextNode("Test number two", TextType.BOLD, "https://www.fakeweb.bix")
        self.assertNotEqual(node3, node4)
        self.assertNotEqual(node, node3)
        node5 = TextNode("Test number two", TextType.ITALIC, "https://www.fakeweb.biz")
        self.assertEqual(node5, node3)
        


if __name__ == "__main__":
    unittest.main()