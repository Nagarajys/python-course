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


# TOPIC 15 - CLASS BASED DECORATERS:
class prediction_monitor:
    def __init__(self, function):
        self.function = function

    def __call__(self):
        print("Prediction started")
        self.function()
        print("Prediction completed")


@prediction_monitor
def predicts():
    print("Genrating AI prediction")


predicts()


# TOPIC 16 - DECORATING CLASS METHODS:
from functools import wraps


def prediction_monitors(function):
    @wraps(function)
    def wrapper(self):
        print("AI prediction started")
        function(self)
        print("AI prediction finished")

    return wrapper


class AImodel:
    @prediction_monitors
    def predictss(self):
        print("Genratinng AI prediction")


md = AImodel()
md.predictss()


# TOPIC - 17 BUILT IN DECORATERS:
# 1.Staticmethod
class Dataanalyzer:
    @staticmethod
    def show_tools():
        print("Numpy")
        print("pandas")
        print("Matplotlib")


Dataanalyzer.show_tools()


# TOPIC 17:
# 2. @classmethod
class Neuralnetwork:
    framework = "Tensorflow"

    @classmethod
    def display_framework(cls):
        print("FRAMEWORK:", cls.framework)


Neuralnetwork.display_framework()
