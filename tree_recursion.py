from hexlet.fs import mkdir, mkfile, get_children, get_name, get_meta, is_file
import copy


def downcase_file_names(node):
    name = get_name(node)
    new_meta = copy.deepcopy(get_meta(node))
    if is_file(node):
        return mkfile(name.lower(), new_meta)
    children = get_children(node)
    new_child = list(map(lambda child: downcase_file_names(child), children))
    new_tree = mkdir(name, new_child, new_meta)
    return new_tree


tree = mkdir('/', [
    mkdir('eTc', [
        mkdir('NgiNx', [], {'size': 4000}),
        mkdir(
            'CONSUL',
            [mkfile('config.JSON', {'uid': 0})],
        ),
    ]),
    mkfile('HOSTS'),
])


new_tree = downcase_file_names(tree)
new_file = get_children(new_tree)[1]
print(get_name(new_file))  # hosts
