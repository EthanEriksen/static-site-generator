from htmlnode import LeafNode


text_types = {
    "text": "text",
    "bold": "bold",
    "italic": "italic",
    "code": "code",
    "link": "link",
    "image": "image",
}


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text != other.text:
            return False

        if self.text_type != other.text_type:
            return False

        if self.url != other.url:
            return False

        return True

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
    if text_node.text_type == text_types["text"]:
        return LeafNode(None, text_node.text)

    if text_node.text_type == text_types["bold"]:
        return LeafNode("b", text_node.text)

    if text_node.text_type == text_types["italic"]:
        return LeafNode("i", text_node.text)

    if text_node.text_type == text_types["code"]:
        return LeafNode("code", text_node.text)

    if text_node.text_type == text_types["link"]:
        return LeafNode("a", text_node.text, {"href": text_node.url})

    if text_node.text_type == text_types["image"]:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

    raise ValueError(f"Invalid text type: {text_node.text_type}")
