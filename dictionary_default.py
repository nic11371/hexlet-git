def collect_indexes(source):
    dict = {}
    for i, e in enumerate(source):
        dict.setdefault(e, []).append(i)
    return dict


d = collect_indexes("hello")
print(d["h"])  # [0]
print(d["e"])  # [1]
print(d["l"])  # [2, 3]
print(d["l"])  # [2, 3]
