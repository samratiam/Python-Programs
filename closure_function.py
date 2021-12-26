"""
Here we are learning closure
"""

def greet(msg):
    # This is the outer enclosing function

    def print_message():
        # this is the nested function
        print(msg)
    return print_message

# 'greet' function is returning the 'print message' fxn which is now assigned to "message"
message = greet("Hello World")
message()  #calling message because it has the reference of function
