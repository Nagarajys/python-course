def create_model(model_name):
    def display_model():
        print("model_name", model_name)

    return display_model


ann = create_model("ANN")
cnn = create_model("CNN")
ann()
cnn()


# topic 6:
def dataset_tracker(function):
    def wrapper():
        print("Dataset loading started")

        function()

        print("dataset loading completed")

    return wrapper


def load_dataset():
    print("Loading AI training dataset")


result = dataset_tracker(load_dataset)
result()


# TOPIC 7 using @syntax
def model_monitor(function):
    def wrapper():
        print("Model excecution started")
        function()
        print("Model excecution completed")

    return wrapper


@model_monitor
def predict():
    print("AI prediction genrated")


predict()
