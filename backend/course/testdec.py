import time

def decorator(f):
    def wrapper():
        print(time.time())
        f()
    return wrapper

@decorator
def f1():
    print("This is a funciton")

f1()

def enrolled_required(f):
    def wrapper():
