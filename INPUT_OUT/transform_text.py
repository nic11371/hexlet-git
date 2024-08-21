def transform(input_file, output_file, rules):
    min_length = rules['word_min_len']
    censor = rules['censored_words']
    capital = rules['capital_letters']
    input = open(input_file)
    file = input.read()
    # for line in file:
    #     line = line.split()
    #     print(line)
    words = file.split()
    output = open(output_file, 'w')
    output.writelines(word_min_len(min_length, words))
    output.writelines(censored_words(censor, words))
    output.writelines(capital_letters(capital, words))
    input.close()
    output.close()


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


print(transform('./INPUT_OUT/2.txt', './INPUT_OUT/output.txt', rules=rules))
print(open('./INPUT_OUT/output.txt').read())
