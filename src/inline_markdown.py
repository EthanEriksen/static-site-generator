import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_italic,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_link,
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue

        sections = old_node.text.split(delimiter)

        if len(sections) % 2 == 0:
            raise Exception("No closing delimiter found.")

        for i in range(0, len(sections)):
            if sections[i] == "":
                continue

            if i % 2 == 0:
                new_nodes.append(TextNode(sections[i], text_type_text))

            else:
                new_nodes.append(TextNode(sections[i], text_type))

    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def split_nodes_images(old_nodes):
    new_nodes = []

    for old_node in old_nodes:

        # if old_node is empty, skip it
        if old_node.text == "":
            continue

        images = extract_markdown_images(old_node.text)

        # if old_node has no images, put it back without altering it
        if images == []:
            new_nodes.append(old_node)
            continue

        remaining_text = old_node.text

        for image in images:
            alt_text = image[0]
            url = image[1]

            # split the text on the image
            split_text = remaining_text.split(f"![{alt_text}]({url})", 1)

            # if there was text before the image, put it in a new node
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], text_type_text))

            # add the image node
            new_nodes.append(TextNode(image[0], text_type_image, image[1]))

            # put the remaining text back for next iteration
            remaining_text = split_text[1]

        # if there is text leftover, add a final node containing it
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, text_type_text))

    return new_nodes


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def split_nodes_links(old_nodes):
    new_nodes = []

    for old_node in old_nodes:

        # if old_node is empty, skip it
        if old_node.text == "":
            continue

        links = extract_markdown_links(old_node.text)

        # if old_node has no links, put it back without altering it
        if links == []:
            new_nodes.append(old_node)
            continue

        remaining_text = old_node.text

        for link in links:
            text = link[0]
            url = link[1]

            # split the text on the link
            split_text = remaining_text.split(f"[{text}]({url})", 1)

            # if there was text before the image, put it in a new node
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], text_type_text))

            # add the image node
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))

            # put the remaining text back for next iteration
            remaining_text = split_text[1]

        # if there is text leftover, add a final node containing it
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, text_type_text))

    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_images(nodes)
    nodes = split_nodes_links(nodes)
    return nodes
