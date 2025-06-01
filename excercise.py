string = "Да, я сумрачен, я беспрерывно закрываюсь Я часто желаю выйти из общества Я, может быть, и буду делать добро людям, но часто не вижу ни малейшей причины им делать добро"

def counter_word(string):
    dictionary = {}
    count = 1
    lists_words = string.replace(',', '').split(' ')
    for i in lists_words:
        dictionary[i] = lists_words.count(i)
    return dictionary


print(counter_word(string))
