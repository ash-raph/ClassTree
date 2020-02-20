def get_subtree(cl, depth=0):
    if depth:
        print(' ' * 3 * depth, '|-->', sep='', end='')
    print(f'{cl.__name__}')

    for c in cl.__subclasses__():
        get_subtree(c, depth + 1)
