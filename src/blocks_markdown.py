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
