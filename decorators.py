# a function that takes a function of input and returns a modified version as an element

def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper


@announce
def hello():
    print("Hello WORLD")


hello()
