tree = {
    "tag": "div",
    "content": [
        {
            "tag": "h1",
            "content": "Заголовок"
        },
        {
            "tag": "p",
            "content": "Это пример HTML-строки, созданной из подобия DOM-рева."
        }
    ],
    "attributes": {
        "class": "container",
        "id": "main-container"
    }
}


def solution(root):
    collection = ""
    attributes = ""
    content = []

    def walk(node):
        return f"<{node['tag']}>{node['content']}</{node['tag']}>"
    tag = root['tag']
    if isinstance(root['content'], list):
        for item in root['content']:
            content.append(walk(item))
    if root['attributes']:
        for key, value in root['attributes'].items():
            attributes += f" {key}=\"{value}\""
    collection += f"<{tag}{attributes}>{"".join(content)}</{tag}>"

    return collection


print(solution(tree))
