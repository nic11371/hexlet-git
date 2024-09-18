from collection_format import Collection


def format(data):
    c = Collection(data)
    c_cor = []
    c_ = Collection(c_cor)
    for elem in c.all():
        dict_ = {}
        c_cor.append(dict_)
        for k, v in elem.items():
            dict_[k] = v.lower().strip()
    return c_.unique() \
        .group_by(lambda row: (row['country'], row['name'])) \
        .map_(lambda row: {k: sorted(v) for k, v in row.items()}) \
        .sort_by(lambda row: list(row.keys())).all()

# def _normalise(row):
#     return {'name': row['name'].lower().strip(), 'country': row['country'].lower().strip()}


raw = [{'name': 'istambul', 'country': 'turkey'},
       {'name': 'Moscow ', 'country': ' Russia'},
       {'name': 'iStambul', 'country': 'tUrkey'},
       {'name': 'antalia', 'country': 'turkeY '},
       {'name': 'samarA', 'country': '  ruSsiA'}]

expected = [{'russia': ['moscow', 'samara']},
            {'turkey': ['antalia', 'istambul']},]


print(format(raw))


def test_format():
    assert format(raw) == expected


test_format()
