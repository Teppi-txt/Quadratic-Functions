import matplotlib
import sympy

def factorize(string_eq):
    equation = sympy.parse_expr(string_eq)
    return sympy.factor(equation)

def expansion(string_eq):
    equation = sympy.parse_expr(string_eq)
    return sympy.expand(equation)