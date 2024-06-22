import unittest
from textnode import TextNode, text_types
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_delimiter_bold(self):
        input_nodes = [
            TextNode("This is some text.", text_types["text"]),
            TextNode("This text is bold.", text_types["bold"]),
            TextNode("This should be **bold**", text_types["text"]),
            TextNode("**This is all bold**", text_types["text"])
        ]

        output_nodes = split_nodes_delimiter(input_nodes, "**", text_types["bold"])

        correct_output_nodes = [
            TextNode("This is some text.", text_types["text"]),
            TextNode("This text is bold.", text_types["bold"]),
            TextNode("This should be ", text_types["text"]),
            TextNode("bold", text_types["bold"]),
            TextNode("This is all bold", text_types["bold"]),
        ]

        self.assertEqual(output_nodes, correct_output_nodes)

    def test_split_nodes_delimiter_code(self):
        input_nodes = [
            TextNode("This is some text.", text_types["text"]),
            TextNode("This text is code.", text_types["code"]),
            TextNode("This should be `code`", text_types["text"]),
            TextNode("`This is all code`", text_types["text"]),
            TextNode("`This is code` but this isn't", text_types["text"])
        ]

        output_nodes = split_nodes_delimiter(input_nodes, "`", text_types["code"])

        correct_output_nodes = [
            TextNode("This is some text.", text_types["text"]),
            TextNode("This text is code.", text_types["code"]),
            TextNode("This should be ", text_types["text"]),
            TextNode("code", text_types["code"]),
            TextNode("This is all code", text_types["code"]),
            TextNode("This is code", text_types["code"]),
            TextNode(" but this isn't", text_types["text"])
        ]

        self.assertEqual(output_nodes, correct_output_nodes)

    def test_image_extraction(self):
        text = "This is some text containing ![an image](https://imgur.com/12345.jpg)"
        images = extract_markdown_images(text)

        self.assertEqual(images, [("an image", "https://imgur.com/12345.jpg")])

    def test_link_extraction(self):
        text = "This is some text containing [a link](https://boot.dev/)"
        links = extract_markdown_links(text)

        self.assertEqual(links, [("a link", "https://boot.dev/")])
        

if __name__ == "__main__":
    unittest.main()