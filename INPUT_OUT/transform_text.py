def transform(input_file, output_file, rules):
    min_length = rules['word_min_len']
    censor = rules['censored_words']
    capital = rules['capital_letters']
    input_file = open(input_file, 'r')
    for line in input_file:
        line = line.split()
    
    f.writelines()
    return f

# word = 'python was language'


def word_min_len(rules, lines):
    new_string = list(filter(lambda word: len(word) >= rules, lines))
    return ' '.join(new_string)


def censored_words(rules, lines):
    new_string = list(filter(lambda word: word not in rules, lines))
    return ' '.join(new_string)


def capital_letters(rules, lines):
    new_string = list(map(
        lambda word: word[0].upper() + word[1:]
        if word[0] in rules else word, lines))
    return ' '.join(new_string)


rules = {
    'word_min_len': 3,
    'censored_words': ['language', 'show'],
    'capital_letters': ['l', 'a'],
}

# print(capital_letters(rules, word))

print(transform('python.txt', 'out.txt', rules=rules))
print(open('out.txt').read())
