import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "Lorem ipsum", None, {"class": "body-text"})
        node2 = HTMLNode("a", "Link text", None, {"href": "https://boot.dev/"})
        self.assertEqual(node.props_to_html(), ' class="body-text"')
        self.assertEqual(node2.props_to_html(), ' href="https://boot.dev/"')

    def test_to_html(self):
        node = LeafNode("p", "Lorem ipsum", {"class": "body-text"})
        node2 = LeafNode(
            "p", "This is a p tag", {"style": "color: red;", "class": "intro"}
        )
        node3 = ParentNode("p", [node, node2], {"class": "container"})

        self.assertEqual(node.to_html(), '<p class="body-text">Lorem ipsum</p>')
        self.assertEqual(
            node2.to_html(), '<p style="color: red;" class="intro">This is a p tag</p>'
        )
        self.assertEqual(
            node3.to_html(),
            f'<p class="container">{node.to_html()}{node2.to_html()}</p>',
        )


if __name__ == "__main__":
    unittest.main()
