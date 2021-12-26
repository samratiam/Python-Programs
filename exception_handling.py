#raise exception
distance = 5
if distance < 6:
    raise Exception('Distance must be greater than 6')

#assertion which is consider as raise-if statement
def validate(distance):
    assert(distance > 6),'Distance must be greater than 6'
print(validate(5))

#try,except,else,finally
try:
    distance = input("Enter distance: ")
except TypeError as error: #execute when exception
    print(error)
else:
    print('Else clause executed!') #execute if there is no exception
finally:
    print("Finally clause executed") #always execute whether exception or not
