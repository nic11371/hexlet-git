from collections import Counter


FREE_EMAIL_DOMAINS = [
    'gmail.com',
    'yandex.ru',
    'hotmail.com',
    'yahoo.com',
]


emails = [
    'info@gmail.com',
    'info@yandex.ru',
    'info@hotmail.com',
    'mk@host.com',
    'support@hexlet.io',
    'key@yandex.ru',
    'sergey@gmail.com',
    'vovan@gmail.com',
    'vovan@hotmail.com',
]


def get_free_domains_count(coll):
    domain = map(lambda s: s.split('@')[1], coll)
    filter_domain = filter(lambda s: s in FREE_EMAIL_DOMAINS, domain)
    return dict(Counter(filter_domain))


print(get_free_domains_count(emails))