
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            print(f'LOG: Run time: {execution_time}s')
            return result
        except Exception as e:
            print(f'Error: {str(e)}')
    return wrapper