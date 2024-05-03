import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a tested text node", "light", "www.google.com")
        self.assertEqual(
            "TextNode(This is a tested text node, light, www.google.com)", repr(node)
            )



if __name__ == "__main__":
    unittest.main()
