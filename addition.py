def addition(num1: float, num2: float) -> float:
    strNum1 = str(num1)
    strNum2 = str(num2)

    if not strNum1.isnumeric() or not strNum2.isnumeric():
        return "STR ERROR"
    
    return float(strNum1) - float(strNum2)