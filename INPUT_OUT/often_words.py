def count_words(filepath):
    punc = '''!()-[]{};:'",<>./?@#$%^&*_~'''
    data = open(filepath).read()
    words = data.split()
    dictionary = {}
    for i in words:
        word = i.strip(punc)
        if word not in dictionary:
            dictionary[word.lower()] = 0
        dictionary[word.lower()] += 1
    return dictionary


print(count_words('./1.txt'))
