print("Always Executed!!")
a = 10
print(a)
def my_function():
    print("I am inside function")
    '''print("__name__ = ", __name__)'''

if __name__ == "__main__":
    print("Executed when invoked directly")
    print("__name__ = ", __name__)
    my_function()
else:
    print("Executed when imported")
    print("__name__ = ", __name__)

class abc:
    print("Hello, I am in class ABC")

    def f(self):
        print("In function f() of class ab")