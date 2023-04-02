def filter_generator(words: list, fileobject=None, filename=None):
    words_set = set(map(lambda w: w.lower(), words))

    if filename:
        fileobject = open(filename, 'r', encoding='UTF-8')

    with fileobject as file:
        for line in file:
            line_set = set(line.lower().split())
            if words_set & line_set:
                yield line
