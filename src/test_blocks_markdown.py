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


if __name__ == "__main__":
    unittest.main()
