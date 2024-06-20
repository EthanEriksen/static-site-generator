import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "Lorem ipsum", None, {"class": "body-text"})
        self.assertEqual(node.props_to_html(), " class=\"body-text\"")

if __name__ == "__main__":
    unittest.main()