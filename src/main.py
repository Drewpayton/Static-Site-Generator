from textnode import TextNode
from leafnode import LeafNode
from parentnode import ParentNode

def __main__():
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    print(node)

__main__()