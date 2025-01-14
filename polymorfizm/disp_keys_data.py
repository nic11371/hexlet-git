MAP = {
    'img': 'src',
    'a': 'href',
    'link': 'href'
}


def get_links(tags):
    links = []
    for tag in tags:
        name = tag['name']
        if name in MAP:
            attr = MAP[name]
            links.append(tag[attr])
    return links


tags = [
  {'name': 'img', 'src': 'hexlet.io/assets/logo.png'},
  {'name': 'div'},
  {'name': 'link', 'href': 'hexlet.io/assets/style.css'},
  {'name': 'h1'},
]

links = get_links(tags)
print(links)
