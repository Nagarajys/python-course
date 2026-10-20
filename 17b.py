# TOPIC : ERRORS AND EXCEPTION HANDLINGGG::::::
class ExpenseLimitError(Exception):
    pass


try:
    amount = 15000

    if amount > 10000:
        raise ExpenseLimitError("Expense exceeds the allowed limit")

    print("Expense accepted")

except ExpenseLimitError as error:
    print("Invalid expense:", {error})

print("Program continues")


try:
    number = int("hello")
    print(number)

except ValueError as error:
    print("Invalid number:", {error})


## USEING DEBUGGER AND BREAKPOINT:::
def calculate_total(prices):
    total = 0

    for price in prices:
        total += price

    return total


prices = [200, 300, 500]

result = calculate_total(prices)

print("Total:", result)


##final cheking :: for revisionn codee
# Custom exceptions
class InvalidExpenseError(Exception):
    pass


class BudgetExceededError(Exception):
    pass


# Validate and add an expense
def add_expense(amount, category, total_expenses, budget):

    # Validate amount data type
    if type(amount) not in (int, float):
        raise TypeError("Amount must be a number")

    # Validate budget data type
    if type(budget) not in (int, float):
        raise TypeError("Budget must be a number")

    # Validate existing total data type
    if type(total_expenses) not in (int, float):
        raise TypeError("Total expenses must be a number")

    # Validate amount
    if amount <= 0:
        raise InvalidExpenseError("Expense amount must be positive")

    # Validate category
    if type(category) != str or category.strip() == "":
        raise InvalidExpenseError("Category cannot be empty")

    # Validate budget
    if budget < 0:
        raise ValueError("Budget cannot be negative")

    # Validate existing total
    if total_expenses < 0:
        raise ValueError("Total expenses cannot be negative")

    # Calculate new total
    new_total = total_expenses + amount

    # Check budget limit
    if new_total > budget:
        raise BudgetExceededError("Total expenses exceed the budget")

    return new_total


# Process the expense
def process_expense(amount, category, total_expenses, budget):

    try:
        updated_total = add_expense(amount, category, total_expenses, budget)

    except InvalidExpenseError as error:
        print("Invalid expense:", error)

    except BudgetExceededError as error:
        print("Budget error:", error)

    except (TypeError, ValueError) as error:
        print("Input error:", error)

    except Exception as error:
        print("Unexpected error:", error)

    else:
        print("Updated total:", updated_total)

    finally:
        print("Expense processing completed.")


# Test 1: Valid expense
process_expense(500, "Food", 1000, 2000)

# Test 2: Invalid data type
process_expense("abc", "Food", 1000, 2000)

# Test 3: Zero amount
process_expense(0, "Food", 1000, 2000)

# Test 4: Empty category
process_expense(500, "   ", 1000, 2000)

# Test 5: Negative budget
process_expense(500, "Food", 1000, -2000)

# Test 6: Negative existing total
process_expense(500, "Food", -100, 2000)

# Test 7: Budget exceeded
process_expense(1500, "Shopping", 1000, 2000)
