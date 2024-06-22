from textnode import TextNode, text_types

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != text_types["text"]:
            new_nodes.append(old_node)
            continue

        sections = old_node.text.split(delimiter)

        if len(sections) % 2 == 0:
            raise Exception("No closing delimiter found.")
            
        for i in range(0, len(sections)):
            if sections[i] == "":
                continue

            if i % 2 == 0:
                new_nodes.append(TextNode(sections[i], text_types["text"]))

            else:
                new_nodes.append(TextNode(sections[i], text_type))

    return new_nodes