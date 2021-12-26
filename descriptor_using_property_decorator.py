class MyClass():
    def __init__(self,value):
        self._value = value #protected member as there is underscore before value

    #getting value
    @property
    def value(self) -> object:
        print('getting value...')
        return self._value

    #setting value
    @value.setter
    def value(self,value) -> None:
        print('Setting value to ' + str(value))
        self._value = value

    #deleting value
    @value.deleter
    def value(self):
        print('Deleting...')
        del self._value

obj = MyClass(24) #instantiating obj
print(obj.value)  #get value
obj.value = 40    #set value
print(obj.value)
del obj.value     #delete value
print(obj.value)
