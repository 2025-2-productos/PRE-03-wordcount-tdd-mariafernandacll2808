def split_into_words(all_lines):
    words = []
    for line in all_lines:
        words.extend(words.strip(",.!?") for words in line.split())
    return words
