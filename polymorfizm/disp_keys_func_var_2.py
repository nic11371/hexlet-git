excluded_attrs = ['name', 'tag_type', 'body']


def build_attrs(tag):
    acc = []
    for attr in tag:
        if attr not in excluded_attrs:
            acc.append(f' {attr}="{tag[attr]}"')
    return ''.join(acc)


mapping = {
    'single': lambda tag: f"<{tag['name']}{build_attrs(tag)}>",
    'pair': lambda tag: f"<{tag['name']}{build_attrs(tag)}>{tag['body']}</{tag['name']}>",  # noqa: E501
}


def stringify(tag):
    build = mapping[tag['tag_type']]
    return build(tag)


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
