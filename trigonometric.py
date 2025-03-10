import math

def sin(a):
    return "sin(" + str(a) + ") = " + str(round(math.sin(a), 10))

def cos(a):
    return "cos(" + str(a) + ") = " + str(round(math.cos(a), 10))

def tan(a):
    return "tan(" + str(a) + ") = " + str(round(math.tan(a), 10))

def cot(a):
    return "cot(" + str(a) + ") = " + str(round(1 / math.tan(a), 10))

def sec(a):
    return "sec(" + str(a) + ") = " + str(round(1 / math.cos(a), 10))

def csc(a):
    return "csc(" + str(a) + ") = " + str(round(1 / math.sin(a), 10))

def asin(a):
    return "arcsin(" + str(a) + ") = " + str(round(math.asin(a), 10))

def acos(a):
    return "arccos(" + str(a) + ") = " + str(round(math.acos(a), 10))

def atan(a):
    return "arctan(" + str(a) + ") = " + str(round(math.atan(a), 10))

def acot(a):
    return "arccot(" + str(a) + ") = " + str(round(math.atan(1 / a), 10))

def asec(a):
    return "arcsec(" + str(a) + ") = " + str(round(math.acos(1 / a), 10))

def acsc(a):
    return "arccsc(" + str(a) + ") = " + str(round(math.asin(1 / a), 10))