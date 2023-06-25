import operator

def calculator():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    operation = input("Enter operation (+, *, /, -): ")
    
    operatorEquivalent = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }
    op = operatorEquivalent.get(operation)
    result = op(num1,num2)
    return result




