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

    result = calculate_accuracy()

    def calculate_loss():
        loss = 0.11
        return loss

    calculate_loss()


evaluate_model()
