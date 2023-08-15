# What is scope?
# Scope is a particular region of the program where variable is available

# What is the difference between local and global variables?

# if a variable is declared in a function , then it is called local variable and
# it has local scope, we can access the variables only inside the function
# we cannot access the variable outside the function

def check_local_scope():
    a = 0
    return a + 2


# print(a)

# if a variable is declared outside of a function then it is called global variable.
# we can access the global variable throughout our file, functions
# we can declare global variables in 2 ways
# 1. directly declare in the module and
# 2. declaring in the function using --global-- keyword

# 1.
name = "Harish"


def say_hi():
    return f"Hi {name}"


print(say_hi())

# 2.
def f1():
    global a
    a = 10
    print(a)
#
#
def f2():
    print(a)
#
f1()
f2()

# If global variable and local variable having the same name then we can access
# global variable inside a function as follows
a = 10


def func_with_same_var_name():
    a = 11
    print(a)
    print(type(globals()))
    # print(globals().values())
    # print(globals().keys())
    print(globals()['a'])


func_with_same_var_name()

# Why is using the global statement a bad practice?
# Global variables are dangerous because they can be simultaneously accessed
# from multiple sections of a program. This frequently results in bugs.

