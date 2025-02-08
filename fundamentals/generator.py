from typing import List, Union


# Special kind of iterable that allows you to iterate over data *lazily*
# yield is used inside a generator function to produce a value.
# - Unlike return, yield pauses the function execution and remembers its state.
# - The next time the next() is called on generator, it resumes from where it left off.
# yield from is used when iterating over an iterable inside a generator.
# - Short hand for doing yield in a for loop of an iterable


def sub_generator():
    yield 1
    yield 2

def main_generator_yield_from():
    yield "A"
    # Instead of manually yielding 1 and 2
    yield from sub_generator()
    yield "B"

def main_generator():
    yield "A"
    for x in sub_generator():
        yield x
    yield "B"

class NestedInteger:
    def __init__(self, value: Union[int, List['NestedInteger']]):
        if isinstance(value, int):
            self._integer = value
            self._list = None
        elif isinstance(value, list):
            self._integer = None
            self._list = [
                x if isinstance(x, NestedInteger) else NestedInteger(x)
                for x in value
            ]
        else:
            raise TypeError("NestedInteger must be initialized with an int or a list of NestedInteger")

    def isInteger(self) -> bool:
        return self._integer is not None

    def getInteger(self) -> int:
        return self._integer if self.isInteger() else None

    def getList(self) -> List['NestedInteger']:
        return self._list if not self.isInteger() else None


# Allow us to suspend the iterations of a loop and resume later
# Otherwise we would have needed to create a stack to store the state
class NestedIterator:
    def __init__(self, nested_list: [NestedInteger]):
        self.peek = None
        self._generator = self.generator(nested_list)

    def generator(self, nested_list):
        for item in nested_list:
            if item.isInteger():
                yield item.getInteger()
            else:
                yield from self.generator(item.getList())

    def next(self) -> int:
        element, self.peek = self.peek, None
        return element

    def hasNext(self) -> bool:
        if self.peek is not None: return True
        try:
            self.peek = next(self._generator)
            return True
        except:
            return False


nestedList = [
    NestedInteger(1),
    NestedInteger([
        NestedInteger(2),
        NestedInteger([
            NestedInteger(3),
            NestedInteger(4)
        ]),
        NestedInteger(5)
    ]),
    NestedInteger([
        NestedInteger(6),
        NestedInteger([
            NestedInteger(7),
            NestedInteger(8),
            NestedInteger([
                NestedInteger(9),
                NestedInteger(10)
            ])
        ])
    ])
]
iterator = NestedIterator(nestedList)
flattened_list = []
while iterator.hasNext():
    flattened_list.append(iterator.next())

print(flattened_list)  # Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


