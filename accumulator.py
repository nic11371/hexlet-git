from hexlet.fs import mkdir, mkfile, flatten, get_children, get_name, is_file, is_directory
import os


def find_files_by_name(tree, sub):

    def walk(node, ancestry):
        name = get_name(node)
        children = get_children(node)
        if name.find(sub) and is_file(node):
            return name
        file_paths = filter(is_directory, children)
        common_path = map(
            lambda child: walk(child, os.path.join(ancestry, name)), file_paths
        )
        return flatten(common_path)
    return walk(tree, sub)


tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('.nginx.conf', {'size': 800}),
        ]),
        mkdir('.consul', [
            mkfile('.config.json', {'size': 1200}),
            mkfile('data', {'size': 8200}),
            mkfile('raft', {'size': 80}),
        ]),
    ]),
    mkfile('.hosts', {'size': 3500}),
    mkfile('resolve', {'size': 1000}),
])


print(find_files_by_name(tree, 'co'))
