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


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


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
    children = text_to_children(text)
    html_node = ParentNode("p", children)

    return html_node


def heading_block_to_html(block):
    level = 0

    for char in block:
        if char == "#" and level < 6:
            level += 1
        else:
            break

    children = text_to_children(block[level + 1 :])
    html_node = ParentNode(f"h{level}", children)

    return html_node


def code_block_to_html(block):
    text = block[3:-3]
    children = text_to_children(text)
    html_node = ParentNode("pre", children)

    return ParentNode("code", html_node)


def quote_block_to_html(block):
    lines = block.split("\n")
    treated_lines = []

    for line in lines:
        if line[:2] != "> ":
            raise ValueError("Not a valid quote block")
        else:
            treated_lines.append(line[2:])

    text = " ".join(treated_lines)
    children = text_to_children(text)
    html_node = ParentNode("blockquote", children)

    return html_node


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)
