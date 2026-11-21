from functools import wraps
import time


def training_timer(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        execution_time = end - start
        print(f"execution time approximetly{execution_time:.1f}seconds")
        return result

    return wrapper


@training_timer
def genrate_training_report():
    print("GENRATING TRAINIGN REPORT")
    time.sleep(2)


genrate_training_report()
