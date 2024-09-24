import logging
import time
from functools import wraps


logging.basicConfig(filename='decoratorExampleLog.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_function_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f'Function {func.__name__} called')
        return func(*args, **kwargs)
    return wrapper

def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f'Function {func.__name__} executed in {execution_time:.4f} seconds')
        return result
    return wrapper


@log_function_name
@log_execution_time
def example_function(x, y):
    time.sleep(2)
    return x + y

# Example usage
if __name__ == "__main__":
    print(example_function(5, 3))
