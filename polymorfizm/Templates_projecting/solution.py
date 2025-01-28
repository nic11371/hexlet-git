def save(tag, path):
    html = tag.render()
    with open(path, 'w') as f:
        f.write(html)
