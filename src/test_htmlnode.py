import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "Lorem ipsum", None, {"class": "body-text"})
        node2 = HTMLNode("a", "Link text", None, {"href": "https://boot.dev/"})
        self.assertEqual(node.props_to_html(), " class=\"body-text\"")
        self.assertEqual(node2.props_to_html(), " href=\"https://boot.dev/\"")

if __name__ == "__main__":
    unittest.main()