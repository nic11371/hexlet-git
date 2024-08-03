import copy

from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile


tree = mkdir(
            'my documents',
            [
                mkdir('documents.jpg'),
                mkfile('avatar.jpg', {'size': 100}),
                mkfile('passport.jpg', {'size': 200}),
                mkfile('family.jpg', {'size': 150}),
                mkfile('addresses', {'size': 125}),
                mkdir('assets'),
            ],
            {'test': 'haha'},
        )

# BEGIN (write your solution here)


def compress_images(node):
    new_meta = copy.deepcopy(get_meta(node))
    name = get_name(node)
    if name.endswith('jpg'):
        if is_file(node):
            new_meta['size'] //= 2
            mkfile(name, new_meta)
    children = get_children(node)
    new_children = list(map(compress_images, children))
    new_tree = mkdir(name, new_children, new_meta)
    return new_tree


print(compress_images(tree))


# END
