import json


def func(string: str):
    return len(string)


def parse_json(json_str: str, keyword_callback, required_fields=None, keywords=None):
    json_doc = json.loads(json_str)
    for field in required_fields:
        value = json_doc[field]
        words = value.split()
        for i in range(len(words)):
            if words[i] in keywords:
                words[i] = str(keyword_callback(words[i]))
                json_doc[field] = ' '.join(words)
    # print(json_doc)
    return json.dumps(json_doc)

# json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
# required_fields = ["key1"]
# keywords = ["word2"]
# # Тогда keyword_callback будет вызвана только для слова 'word2' для ключа 'key1'.
# print(parse_json(json_str, func, required_fields, keywords))
