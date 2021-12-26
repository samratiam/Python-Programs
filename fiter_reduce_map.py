#Filter example
even = lambda x : x % 2 == 0
result = filter(even,[1,2,3,4,5,6,7,8])
print(list(result))

#Map example
mul = lambda x: x ** 2
multiply = map(mul,[1,2,3,4,5])
print(list(multiply))

#Reduce example
from functools import reduce
add = lambda x,y: x+y
total = reduce(add,[1,2,3,4,5,6])
print(total)