from hexlet.fs import mkdir, mkfile, get_children, get_meta, get_name, is_file
import copy


def du(node):
    children_node = get_children(node)

    def get_files_count(size):
        if is_file(size):
            meta = copy.deepcopy(get_meta(size))
            return meta['size']
        children = get_children(size)
        recursive = list(map(get_files_count, children))
        return sum(recursive)

    result = map(
        lambda child: (get_name(child), get_files_count(child)),
        children_node
    )

    return sorted(list(result), key=lambda i: i[1], reverse=True)


tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('nginx.conf', {'size': 800}),
        ]),
        mkdir('consul', [
            mkfile('.config.json', {'size': 1200}),
            mkfile('data', {'size': 8200}),
            mkfile('raft', {'size': 80}),
        ]),
    ]),
    mkfile('hosts', {'size': 3500}),
    mkfile('resolve', {'size': 1000}),
])


print(du(tree))
