def remove_first_level(tree):
    new_tree = []
    for i in tree:
        if not isinstance(i, list):
            continue
        for j in i:
            new_tree.append(j)
    return new_tree


tree1 = [[5], 1, [3, 4]]
print(remove_first_level(tree1))  # [5, 3, 4]
tree2 = [1, 2, [3, 5], [[4, 3], 2]]
print(remove_first_level(tree2))  # [3, 5, [4, 3], 2]
