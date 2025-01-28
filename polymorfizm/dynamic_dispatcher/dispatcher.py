_virtual_table = {}


def defmethod(type_name, method_name, fn):
    if type_name not in _virtual_table:
        _virtual_table[type_name] = {}
    _virtual_table[type_name][method_name] = fn


def call(obj, full_method_name, args):
    type_name = obj['name']
    method_name = full_method_name.split('.')[-1]
    fn = _virtual_table.get(type_name, {}).get(method_name)
    if not fn:
        return None
    return fn(obj, *args)
