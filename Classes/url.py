from urllib.parse import urlparse, parse_qs


class Url:
    def __init__(self, url):
        self.url = url

    def get_scheme(self):
        return urlparse(self.url).scheme

    def get_hostname(self):
        return urlparse(self.url).hostname

    def get_query_params(self):
        result = urlparse(self.url)
        return parse_qs(result.query)

    def get_query_param(self, name, name2=None):
        result = urlparse(self.url)
        if name not in parse_qs(result.query):
            return name2
        return parse_qs(result.query)[name][0]

    def __eq__(self, other):
        return self.url == other.url


# url = Url('http://hexlet.io:80?key=value&key2=value2')
# url.get_scheme() # http
# url.get_hostname() # hexlet.io
# print(url.get_query_params())
# # {
# #  key: [value],
# #  key2: [value2],
# # }
# print(url.get_query_param('key')) # value
# # # второй параметр — значение по умолчанию
# print(url.get_query_param('key2', 'lala')) # value2
# print(url.get_query_param('new', 'ehu')) # ehu
# url.get_query_param('new') # None
# url = Url('http://hexlet.io:80?key=value&key2=value2')
# print(url.get_scheme()) # http
# print(url.get_hostname()) # hexlet.io

# url == Url('http://hexlet.io:80?key=value&key2=value2') # True
# url == Url('http://hexlet.io:80?key=value') # False


URL1 = 'http://hexlet.io?key=value&key2=value2'
URL2 = 'https://google.com:80?a=b&c=d&lala=value'


def test_url1():
    url = Url(URL1)
    assert url.get_scheme() == 'http'
    assert url.get_hostname() == 'hexlet.io'
    assert url.get_query_params() == {
        'key': ['value'],
        'key2': ['value2'],
        }
    assert url.get_query_param('key') == 'value'
    assert url.get_query_param('key2', 'lala') == 'value2'
    assert url.get_query_param('new', 'ehu') == 'ehu'
    assert url == (Url(URL1))
    assert not url == (Url(URL2))


def test_url2():
    url = Url(URL2)
    assert url.get_scheme() == 'https'
    assert url.get_hostname() == 'google.com'
    assert url.get_query_params() == {
        'a': ['b'],
        'c': ['d'],
        'lala': ['value'],
        }
    assert url.get_query_param('key') is None
    assert url.get_query_param('key2', 'lala') == 'lala'
    assert url.get_query_param('new', 'ehu') == 'ehu'
    assert url == (Url(URL2))
    assert not url == (Url(URL1))
    assert not url == (Url('https://google.com'))
    assert not url == (Url(URL2.replace('80', '443')))


test_url1()
test_url2()
