import unittest
from textnode import TextNode, text_types
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_images,
    split_nodes_links,
    text_to_textnodes,
)


class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_delimiter_bold(self):
        input_nodes = [
            TextNode("This is some text.", text_types["text"]),
            TextNode("This text is bold.", text_types["bold"]),
            TextNode("This should be **bold**", text_types["text"]),
            TextNode("**This is all bold**", text_types["text"]),
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
            TextNode("`This is code` but this isn't", text_types["text"]),
        ]

        output_nodes = split_nodes_delimiter(input_nodes, "`", text_types["code"])

        correct_output_nodes = [
            TextNode("This is some text.", text_types["text"]),
            TextNode("This text is code.", text_types["code"]),
            TextNode("This should be ", text_types["text"]),
            TextNode("code", text_types["code"]),
            TextNode("This is all code", text_types["code"]),
            TextNode("This is code", text_types["code"]),
            TextNode(" but this isn't", text_types["text"]),
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

    def test_split_nodes_images(self):
        new_nodes = split_nodes_images(
            [
                TextNode(
                    "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
                    text_types["text"],
                )
            ]
        )

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an ", text_types["text"]),
                TextNode(
                    "image",
                    text_types["image"],
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
                ),
                TextNode(" and another ", text_types["text"]),
                TextNode(
                    "second image",
                    text_types["image"],
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png",
                ),
            ],
        )

    def test_split_nodes_links(self):
        new_nodes = split_nodes_links(
            [
                TextNode(
                    "This is text with an [link](https://boot.dev/link) and another [second link](https://boot.dev/link2)",
                    text_types["text"],
                )
            ]
        )

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an ", text_types["text"]),
                TextNode("link", text_types["link"], "https://boot.dev/link"),
                TextNode(" and another ", text_types["text"]),
                TextNode("second link", text_types["link"], "https://boot.dev/link2"),
            ],
        )

    def test_text_to_textnodes(self):
        new_nodes = text_to_textnodes(
            "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        )

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", text_types["text"]),
                TextNode("text", text_types["bold"]),
                TextNode(" with an ", text_types["text"]),
                TextNode("italic", text_types["italic"]),
                TextNode(" word and a ", text_types["text"]),
                TextNode("code block", text_types["code"]),
                TextNode(" and an ", text_types["text"]),
                TextNode(
                    "image",
                    text_types["image"],
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
                ),
                TextNode(" and a ", text_types["text"]),
                TextNode("link", text_types["link"], "https://boot.dev"),
            ],
        )


if __name__ == "__main__":
    unittest.main()
