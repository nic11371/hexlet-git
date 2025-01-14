special_keys = ['name', 'tag_type', 'body']


def single(tag):
    attr = []
    for k, v in tag.items():
        if k not in special_keys:
            attr.append(f'{k}="{v}"')
    return f"<{tag['name']} {" ".join(attr)}>"


def pair(tag):
    attr = []
    body = tag['body'] if tag.get('body') else ""
    for k, v in tag.items():
        if k not in special_keys:
            attr.append(f'{k}="{v}"')
    return f"<{tag['name']}{" ".join(attr)}>{body}</{tag['name']}>"


def dictionary_keys():
    return {'pair': pair, 'single': single}


def stringify(tags):
    tag_type = tags['tag_type']
    keys = dictionary_keys()
    func = keys.get(tag_type)
    return func(tags)


hr_tag = {
  'name': 'hr',
  'class': 'px-3',
  'id': 'myid',
  'tag_type': 'single',
}

print(stringify(hr_tag))  # <hr class="px-3" id="myid">


div_tag = {
  'name': 'div',
  'tag_type': 'pair',
  'body': 'text2',
  'id': 'wow',
}
print(stringify(div_tag))  # <div id="wow">text2</div>

empty_div_tag = {
  'name': 'div',
  'tag_type': 'pair',
  'body': '',
  'id': 'empty',
}
print(stringify(empty_div_tag))  # <div id="empty"></div>
