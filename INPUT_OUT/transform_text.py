def transform(input_file, output_file, rules):
    min_length = rules['word_min_len']
    censor = rules['censored_words']
    capital = rules['capital_letters']
    input = open(input_file)
    output = open(output_file, 'w')
    for line in input:
        line = line.split()
        line = word_min_len(min_length, line)
        line = censored_words(censor, line)
        line = capital_letters(capital, line)
        if line:
            output.writelines(f"{' '.join(line)}\n")
    input.close()
    output.close()


def word_min_len(rules, lines):
    return list(filter(lambda word: len(word) >= rules, lines))


def censored_words(rules, lines):
    return list(filter(lambda word: word.lower() not in rules, lines))


def capital_letters(rules, lines):
    return list(map(
        lambda word: word[0].upper() + word[1:]
        if word[0] in rules else word, lines))


rules = {
    'word_min_len': 3,
    'censored_words': ['ugly', 'than'],
    'capital_letters': ['b', 'a'],
}


print(transform('./INPUT_OUT/2.txt', './INPUT_OUT/output.txt', rules=rules))
print(open('./INPUT_OUT/output.txt').read())
