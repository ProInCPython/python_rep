def add(a,b):
    try:
        return a+b
    except TypeError:
        return "Incorrect input data format!"
    except:
        return "Other error"
def subtract(a,b):
    try:
        return a-b
    except TypeError:
        return "Incorrect input data format!"
    except:
        return "Other error"
def multiply(a,b):
    try:
        return a*b
    except TypeError:
        return "Incorrect input data format!"
    except:
        return "Other error"
def divide(a,b):
    try:
        return a//b if a%b==0 else round(a/b,5)
    except ZeroDivisionError:
        return "Second argument is 0"
    except TypeError:
        return "Incorrect input data format!"
    except:
        return "Other error"
