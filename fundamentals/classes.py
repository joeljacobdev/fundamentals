class SampleClass:
    class_var = 1

    def __init__(self):
        self.instance_var = 1


obj1 = SampleClass()
obj2 = SampleClass()
# This will create a class variable in the object 1 instance.
obj1.class_var = 2
print(obj2.class_var)
# obj1 will have "class_var" attribute added, while "obj2" won't have
print(obj1.__dict__, obj2.__dict__)
SampleClass.class_var = 4
print(obj2.class_var)
