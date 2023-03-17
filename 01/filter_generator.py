def filter_generator(fileobject, words: list):
    words_set = set(map(lambda w: w.lower(), words))

    lines = fileobject.readlines()

    for line in lines:
        line_set = set(line.lower().split())
        if words_set & line_set:
            yield line
