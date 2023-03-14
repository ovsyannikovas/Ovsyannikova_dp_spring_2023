def filter_generator(filename: str, words: list):
    words_set = set(map(lambda w: w.lower(), words))

    with open(filename, 'r', encoding='UTF-8') as file:
        lines = file.readlines()

    for line in lines:
        line_set = set(line.lower().split())
        if words_set & line_set:
            yield line
