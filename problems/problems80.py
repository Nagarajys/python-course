# TOPIC 14 - DECORATERS WITH PARAMETERS:
def model_status(message):

    def decorator(function):

        def wrapper():
            print(message)
            function()

        return wrapper

    return decorator


@model_status("AI prediction Started")
def predict():
    print("Genrating AI prediction")


predict()
