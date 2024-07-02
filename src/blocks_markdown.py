import re
from htmlnode import ParentNode
from textnode import text_node_to_html_node

from inline_markdown import text_to_textnodes

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(markdown):
    raw_blocks = markdown.split("\n\n")
    filtered_blocks = []

    for raw_block in raw_blocks:
        if raw_block == "":
            continue

        raw_block = raw_block.strip()
        filtered_blocks.append(raw_block)

    return filtered_blocks


def block_to_block_type(block):
    if block[:2] == "# ":
        return block_type_heading

    if block[:3] == "```" and block[-3:] == "```":
        return block_type_code

    block_lines = block.split("\n")

    is_quote = True

    for line in block_lines:
        if line[:2] != "> ":
            is_quote = False
            continue

    if is_quote:
        return block_type_quote

    is_ul = True

    for line in block_lines:
        if line[:2] != "* " and line[:2] != "- ":
            is_ul = False
            break

    if is_ul:
        return block_type_unordered_list

    is_ol = True

    for line in block_lines:
        if not re.match(r"\d+\.\ .*", line):
            is_ol = False
            break

    if is_ol:
        return block_type_ordered_list

    return block_type_paragraph


def paragraph_block_to_html(block):
    lines = block.split("\n")
    text = " ".join(lines)
    text_node = text_to_textnodes(text)
    children = text_node_to_html_node(text_node)
    html_node = ParentNode("p", children)

    return html_node


def heading_block_to_html(block):
    level = 0

    for char in block:
        if char == "#" and level < 6:
            level += 1
        else:
            break

    text_node = text_to_textnodes(block)
    children = text_node_to_html_node(text_node)
    html_node = ParentNode(f"h{level}", children)

    return html_node
