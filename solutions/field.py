
def field(items, *args):
    assert len(args) > 0
    for d in items:
        new_dict = {}
        for el in args:
            if el in d.keys():
                if len(args) == 1:
                    yield d[el]
                else:
                    new_dict[el] = d[el]
        if len(args) > 1:
            yield new_dict 


