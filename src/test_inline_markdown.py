import unittest
from textnode import TextNode, text_types
from inline_markdown import split_nodes_delimiter

class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        input_nodes = [
            TextNode("This is some text.", text_types["text"]),
            TextNode("This text is bold.", text_types["bold"]),
            TextNode("This should be **bold**", text_types["text"])
        ]

        output_nodes = split_nodes_delimiter(input_nodes, "**", text_types["bold"])

        correct_output_nodes = [
            TextNode("This is some text.", text_types["text"]),
            TextNode("This text is bold.", text_types["bold"]),
            TextNode("This should be ", text_types["text"]),
            TextNode("bold", text_types["bold"])
        ]

        self.assertEqual(output_nodes, correct_output_nodes)


if __name__ == "__main__":
    unittest.main()