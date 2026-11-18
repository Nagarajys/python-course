# TOPIC 2 - INNER FUNCTIONS::
def train_model():
    print("AI training started")

    def load_data_set():
        print("Data set loaded successfully")

    load_data_set()


train_model()


# 2.
def evaluate_model():
    print("MODEL EVALVATION STARTED")

    def calculate_accuracy():
        accuracy = 95
        return accuracy

    accuracy = calculate_accuracy()

    def calculate_loss():
        loss = 0.11
        return loss

    loss = calculate_loss()

    print(f"accuracy:{accuracy}")
    print(f"loss:{loss}")


evaluate_model()


# 3.
def create_model():

    def train():
        print("AI model training started..")

    return train


model = create_model()
model()


# 4.
def select_model(model_type):

    def ANN_model():
        print("ANN model selected")

    def CNN_model():
        print("CNN model selected")

    if model_type == "ANN":
        return ANN_model

    elif model_type == "CNN":
        return CNN_model

    else:
        print("Invalid model type")
        return None


models = select_model("ANN")

print(type(models))
models()  # type: ignore


n = int(input("Enter a number: "))

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")
