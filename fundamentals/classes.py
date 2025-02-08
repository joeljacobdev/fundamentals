class SampleClass:
    class_var1 = [1]
    class_var2 = 1

    def __init__(self):
        self.instance_var = 1


obj1 = SampleClass()
obj2 = SampleClass()
# This will create a class variable in the object 1 instance.
obj1.class_var2 = 2
print(obj2.class_var2)
# obj1 will have "class_var2" attribute added, while "obj2" won't have
# kind of having namespace isolation - instead of modifying the class value, create create an
# instance variable overriding the original class variable for this object
# Note - that class variables are not shown in the dict.
print(obj1.__dict__, obj2.__dict__)
SampleClass.class_var2 = 4
print(obj2.class_var2)

# But if it is a mutable object
obj1.class_var1.append(2)
print(obj2.class_var1)
# obj1 will have "class_var" attribute added, while "obj2" won't have
print(obj1.__dict__, obj2.__dict__)
