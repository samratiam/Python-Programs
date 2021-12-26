"""Python Descriptors"""

class DescrArttribute:
    def __get__(self, obj, type = None):
        print("accessing the attribute to get the value")
        print("__get__ is called")
        return 100
    def __set__(self,obj,value):
        print("accessing the attribute to set the value")
        print("__set__ is called")
        raise AttributeError("Cannot change the value")
class MyClass:
    attr1 = DescrArttribute()

obj = MyClass()
print(obj.attr1) #__get__ is called

obj.attr1 = 10 #__set__(dunder set) is called

