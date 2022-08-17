import time

def time_check(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(end-start)
    return wrapper
@time_check
def myfunc():
    print("함수실행")
    time.sleep(5)

myfunc()