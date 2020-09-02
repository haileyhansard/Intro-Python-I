# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12

def change_x():
    x = 99
    print(x)
change_x()

# - I added print(x) above to print x when the function is called, it prints 99.
# This prints 12. What do we have to modify in change_x() to get it to print 99?
# - The print(x) below prints 12 because the variable assigning 12 is above the function definition, so its outside of the scope. ( ? Is this the correct reasoning?)
print(x)


# This nested function has a similar problem.

def outer():
    y = 120

    def inner():
        y = 999
        print(y)

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".
    print(y)


outer()
