import equation_functions, graph_function
from enum import Enum
import sympy, numpy

class EqFuncs(Enum):
    FACTOR = 0
    EXPAND = 1
    GRAPH = 2

def identify(expression):
    if "(" in expression or ")" in expression:
        print(equation_functions.expansion(expression))
    else:
        print(equation_functions.factorize(expression))

identify("(x + 2)*(x + 3)")
