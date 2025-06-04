import requests


url = 'https://parsinger.ru/3.4/3/dialog.json'

response = requests.get(url, verify=False)

members_resp = [response.json()]

dictionary = {}


def count_members(members):
    count = 1
    for member in members:
        username = member['username']
        if username in dictionary:
            dictionary[username] += 1
        else:
            dictionary[username] = count
        comments = member['comments']
        if not comments:
            continue
        else:
            count_members(comments)
    return dictionary


def dictionary_sort():
    dictionary_count = count_members(members_resp)
    dictionary_sorted = dict(
        sorted(dictionary_count.items(), key=lambda x: (-x[-1], x[0])))
    return dictionary_sorted


print(dictionary_sort())
