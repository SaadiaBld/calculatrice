import math

def modulo(num1: float, num2: float) -> float:
    strNum1 = str(num1).replace(".", "")
    strNum2 = str(num2).replace(".", "")

    if not strNum1.isnumeric() or not strNum2.isnumeric():
        return "STR ERROR"
    
    return float(num1) % float(num2)

def exponentiel(num1: float, num2: float) -> float:
    strNum1 = str(num1).replace(".", "")
    strNum2 = str(num2).replace(".", "")

    if not strNum1.isnumeric() or not strNum2.isnumeric():
        return "STR ERROR"
    
    return float(num1) ** float(num2)

def logarithm(num1: float) -> float:
    num1 = math.log(float(num1))

    return num1