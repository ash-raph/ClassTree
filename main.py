def get_tree(cl, depth=0, kind='SUB'):
    mapper = {
        'SUB': '__subclasses__',
        'SUPER': '__bases__',
    }
    
    if depth:
        print(' ' * 3 * depth, '|-->', sep='', end='')
    
    print(f'{cl.__name__}')
    res = getattr(cl, mapper[kind])

    for c in res() if callable(res) else res:
        get_tree(c, depth=depth + 1, kind=kind)
