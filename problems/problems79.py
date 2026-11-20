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


# TOPIC 8 - DECORATERS WITH ARGUMNETS
def dataset_monitor(function):
    def wrapper(dataset_name):
        print("Dateset training started")
        function(dataset_name)
        print("Dataset processing completed")

    return wrapper


@dataset_monitor
def process_dataset(dataset_name):
    print("PROCESSING:", dataset_name)


process_dataset("AI training dataset")


# TOPIC 8 - DECORATERS WITH RETURN RESULT
def accuracy_monitor(function):
    def wrapper():
        print("Accuracy calculation started")
        result = function()
        print("Accuracy calculation completed")
        return result

    return wrapper


@accuracy_monitor
def calculate_accuracy():
    return 98


result = calculate_accuracy()
print(result)


# TOPIC 9 - DECORATORS WITH *ARGS AND **KWARGS:4
def prediction_monitor(function):
    def wrapper(*args, **kwargs):
        print("AI prediction started")
        result = function(*args, **kwargs)
        print("AI prediction completed")
        return result

    return wrapper


@prediction_monitor
def predict(model_name, dataset, accuracy):
    print("model_name:", model_name)
    print("dataset:", dataset)
    print("accuracy", accuracy)
    return "prediction_successfull"


result = predict("ANN", "image dataset", 97)
print(result)
