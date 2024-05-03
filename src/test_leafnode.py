import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        
        self.assertEqual(
            "<p>This is a paragraph of text.</p>", node.to_html()
            )

        self.assertEqual(
            '<a href="https://www.google.com">Click me!</a>', node2.to_html()
            )



if __name__ == "__main__":
    unittest.main()
