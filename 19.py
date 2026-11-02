# DECORATORS IN PYTHON:::: - allows us to modify the beheviour of a function without changing actual code


##1.
def decorater_name(
    func,
):  #  decorater name is decorater name here , func used to call decorater
    def wrapper():
        print("Namskara !")
        func()  # takes main function
        print("Take care!")

    return wrapper


@decorater_name  # apllying decorater where that decorater take this intro function to func() region
def intro():
    print("hi i am nagraj from karnataka")


intro()


@decorater_name  # apllying decorater where that decorater take this bye function to func() region
def bye():
    print("bye boss see you next time!!")


bye()


##2. DECORATERS WITH ARGUMENTS
def greett(func):
    def wrapper(name):
        print("hello bro")
        func(name)
        print("have a nice day")

    return wrapper


@greett
def say_name(name):
    print(f"my name is:{name}")


say_name("Naguraj")


# 3 DECORATOR FOR LOGGING::
def logging(func):
    def wrapper():
        print(f"function '{func.__name__}' is being called")
        func()

    return wrapper


@logging
def greet():
    print("hello dostho")


greet()


# 4.
def login_required(function):
    def wrapper():
        print("checking if user is logged in .....")
        function()

    return wrapper


@login_required
def view_profile():
    print("ravi s'profile opened")


view_profile()


#### --------------------------HOMEWORK -------------------------- ####
# 1 . CREATE A DECORATOR TO LOG CALLS:
def log_function_call(function):
    def wrapper():
        print(f"function name is {function.__name__} is being called ")
        function()

    return wrapper


@log_function_call
def add():
    print("addition")


add()


# HW3 -- MULTIPLE DECORATORSSSS -- - - -
def dec1(func):
    def wrapper():
        print("==============")
        func()
        print("==============")

    return wrapper


def dec2(func):
    def wrapper():
        print(f"<<<<<<<<", end="")
        func()

    return wrapper


@dec1
@dec2
def multi():
    print("NAGARAJ.YS")


multi()


## 2 QUESTIONS REMAINIG DO IT AFTER COMPLETING FULL DECORATERSSS


# 1.
def train_model():
    print("AI")


def test_model():
    print("test")


def evaluate_model():
    print("evalvate")


def deploy_model():
    print("deploy")


tasks = {train_model: "1", test_model: "2", evaluate_model: "3", deploy_model: "4"}
for key, values in tasks.items():
    print("task:", values)
    key()  # bcz here tasks are actings as keys


# 2.
def calculate_accuracy():
    accuracy = 95
    return accuracy


def calculate_loss():
    loss = 0.25
    return loss


def display_result(function):
    print("RETURNED VALUES")
    result = function()
    print("result:", result)


display_result(calculate_accuracy)
display_result(calculate_loss)
