def make_module(step=1):
    return {
        'inc': lambda x: x + step,
        'dec': lambda x: x - step,
    }


m = make_module()
print(m['inc'](10))
# 11
print(m['dec'](20))
# 19
m2 = make_module(step=2)
print(m2['inc'](1))
# 3
