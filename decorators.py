"""Decorators"""

def decorate_me(func):
    def inner_func():
        print("It is now decorated")
        func()
    return inner_func

def ordinary():
    print("Ordinary!")

decorated = decorate_me(ordinary)
decorated()

ordinary = decorate_me(ordinary) #name is same but this ordinary stores reference another function
ordinary()  #it returns decorated function

