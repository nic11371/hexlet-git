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


def solution(dom):
    htmlString = "<" + dom["tag"]

    if "attributes" in dom:
        for key, value in dom["attributes"].items():
            htmlString += f' {key}="{value}"'

    htmlString += ">"

    if "content" in dom:
        if isinstance(dom["content"], list):
            for child in dom["content"]:
                htmlString += solution(child)
        else:
            htmlString += dom["content"]

        htmlString += "</" + dom["tag"] + ">"

    return htmlString


print(solution(tree))
