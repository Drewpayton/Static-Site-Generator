import unittest

from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(props={
            "href": "https://www.google.com", "target": "_blank"
        })
        self.assertEqual(
            'HTMLNode(href="https://www.google.com" target="_blank")', repr(node)
            )
    


if __name__ == "__main__":
    unittest.main()
