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
    meta = copy.deepcopy(get_meta(node))

    def reduce_image_size(node):
        new_meta = copy.deepcopy(get_meta(node))
        name = get_name(node)
        if is_file(node):
            if name.endswith('jpg'):
                new_meta['size'] //= 2
                return mkfile(name, new_meta)
        return node
    children = get_children(node)
    new_children = list(map(reduce_image_size, children))
    new_tree = mkdir(get_name(node), new_children, meta)
    return new_tree


print(compress_images(tree))


# END
