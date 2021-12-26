#Iterables have __iter__ method and don't have __next__
#Iterators have __next__ method as well as __iter__
#To check whether iterable or iterator use dir(name) and check those methods in the list
#For example list is iterable but not iterator

#From iterable we can make iterator object
#Iterator are all object we can use loop
#But we use loop in iterable as well but in fact it will be using iterator object

#Iterator object maintain the state as shown below
my_list = [1,2,3]
n = my_list.__iter__() #n is an iterator object
print(n.__next__())
print(n.__next__())
print(n.__next__())
#print(n.__next__()) #shows StopIteration exception as list is exhausted

#Creating our own Range iterator object
class MyRange:
    def __init__(self,start,end):
        self.value = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

nums = MyRange(1,3)
print("My Range: ")
# for num in nums:  It works as it become iterator
#     print(num)

print(next(nums))  # print(nums.__next__())
print(next(nums))  # print(nums.__next__())
#print(next(nums))  # Create StopIteration exception

#For loop is actually While Loop Demonstration
print("For Loop is While Loop")
names = ["Jon", "Jane"]
name_iter = iter(names) #Creating iteratable object
while True:
    try:
        name = next(name_iter)
        print(name)
    except StopIteration:
        break