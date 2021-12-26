"""
Decorator for function with dynamic arguments
"""

def decorator_function(main_function):
    def inner_function(*args, **kwargs):
        print("I am a passionate Software Engineer")
        return main_function(*args, **kwargs)
    return inner_function

@decorator_function     #another way to call decorator function
def display(msg):
    print(msg)

display("Hello, what's up friends? ")
