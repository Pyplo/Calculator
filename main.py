from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))
for x in operations:
    print(x)
symbol = input("Pick operations from the line above")
calc_function = operations[symbol]
answer = calc_function(num1, num2)

print(f"{num1} {symbol} {num2} = {answer}")
