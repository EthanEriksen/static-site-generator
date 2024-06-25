import unittest
from blocks_markdown import *


class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        blocks = markdown_to_blocks(
            "This is **bolded** paragraph\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n* This is a list\n* with items"
        )
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_block_to_block_type(self):
        paragraph = "This is a paragraph."
        heading = "# This is a heading."
        code = "```This is a code block.\nThis is more code.```"
        quote = "> This is a quote.\n> This is the second line of the quote."
        unordered_list = "* List item 1\n* List item 2\n* List item 3\n* List item 4"
        ordered_list = "1. List item 1\n2. List item 2\n3. List item 3"

        self.assertEqual(block_to_block_type(paragraph), block_type_paragraph)
        self.assertEqual(block_to_block_type(heading), block_type_heading)
        self.assertEqual(block_to_block_type(code), block_type_code)
        self.assertEqual(block_to_block_type(quote), block_type_quote)
        self.assertEqual(block_to_block_type(unordered_list), block_type_unordered_list)
        self.assertEqual(block_to_block_type(ordered_list), block_type_ordered_list)


if __name__ == "__main__":
    unittest.main()
