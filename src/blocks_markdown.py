def markdown_to_blocks(markdown):
    raw_blocks = markdown.split("\n\n")
    filtered_blocks = []

    for raw_block in raw_blocks:
        if raw_block == "":
            continue

        raw_block = raw_block.strip()
        filtered_blocks.append(raw_block)

    return filtered_blocks
