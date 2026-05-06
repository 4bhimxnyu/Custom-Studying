import time

def decorator_logTime(func):

    def wrapper():
        start_time = time.time()
        print(f"executing function: {func.__name__}" )
        func()
        end_time = time.time()
        execution_time = start_time - end_time
        print(f"Execution time: {execution_time:.4f} seconds")
    return wrapper


@decorator_logTime
def sameple_func():
    time.sleep(5)
    print("function is already running")


sameple_func()