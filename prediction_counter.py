# EXCECUTION COUNT USING DECORATERS:
from functools import wraps


def excecution_counter(function):
    total_calls = 0

    @wraps(function)
    def wrapper(*args, **keargs):
        nonlocal total_calls
        total_calls = total_calls + 1
        print("Function_excecuted:", total_calls, "times")

    return wrapper


@excecution_counter
def classify_images():
    print("CLASSIIFYING IMAGES")


classify_images()
classify_images()
classify_images()
classify_images()
classify_images()
classify_images()
classify_images()
classify_images()
classify_images()
classify_images()
classify_images()
classify_images()
classify_images()
classify_images()
classify_images()
classify_images()
classify_images()
classify_images()
