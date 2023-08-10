class _Single(object):

    def __str__(self):
        return 'I am the only one'

    def roar(self):
        return u'roar'


_instance = None


def Single():
    global _instance
    if _instance is None:
        _instance = _Single()
    return _instance


a = Single()
b = Single()

print(f'ID(a) is {id(a)}')
print(f'ID(b) is {id(b)}')
print(f'Are the same? {id(a) == id(b)}')