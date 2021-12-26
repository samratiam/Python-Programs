#Generators are simplified iterators
#Generator is much more efficient than return function for large data
#To make iterator but not storing the data, generator is used

def square_numbers(nums):
    for i in nums:
        yield i*i #Generator expression

my_nums = square_numbers([1,2,3,4]) #Generator expression my_nums
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))

print("Generator comprehension")
num = (x*x for x in [1,2,3,4]) #Generator comprehension
print(list(num))

#Generator expression chain
print("Generator chain:")
def integers():
    for i in range(1,5):
        yield i

def squared(seq):
    for i in seq:
        yield i * i

def negated(seq):
    for i in seq:
        yield -i

initial = integers()
print(list(initial)) #print(initial) gives initial is a generator object

square_chain = squared(integers())
print(list(square_chain))

print(list(negated(squared(integers()))))


