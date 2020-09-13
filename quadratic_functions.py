import matplotlib
import sympy
from enum import Enum

import plot_equation

class EqFuncs(Enum):
    FACTOR = 0
    EXPAND = 1
    GRAPH = 2

def factorize(string_eq):
    equation = sympy.parse_expr(string_eq)
    return sympy.factor(equation)

def expansion(string_eq):
    equation = sympy.parse_expr(string_eq)
    return sympy.expand(equation)

plot_equation.plot_quad(expansion("x**2 + 5*x + 6"))

