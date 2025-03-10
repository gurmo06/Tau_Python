def add(a, b):
    val = a + b
    return str(a) + " + " + str(b) + " = " + str(val)

def sub(a, b):
    val = a - b
    return str(a) + " - " + str(b) + " = " + str(val)

def mul(a, b):
    val = a * b
    return str(a) + " x " + str(b) + " = " + str(val)

def div(a, b):
    val = a / b
    return str(a) + " / " + str(b) + " = " + str(val)

def mod(a, b):
    val = a % b
    return str(a) + " % " + str(b) + " = " + str(val)

def pow(a, b):
    val = a ** b
    return str(a) + "^" + str(b) + " = " + str(val)

def sqrt(a):
    val = a ** 0.5
    return "sqrt(" + str(a) + ") = " + str(val)