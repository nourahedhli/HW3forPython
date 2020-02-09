import math

from MathOperations.additon import Addition
from MathOperations.subtraction import Subtraction
from MathOperations.multiplication import Multiplication
from MathOperations.division import Division
from MathOperations.exponentiation import Exponent
from MathOperations.nthroot import nthRoot
from MathOperations.log import Log


class Calculator:
    Result = 0

    def __init__(self):
        pass

    def Sum(self, a, b):
        self.Result = Addition.sum(a, b)
        return self.Result

    def Difference(self, a, b):
        self.Result = Subtraction.difference(a, b)
        return self.Result

    def Product(self, a, b):
        self.Result = Multiplication.product(a, b, )
        return self.Result

    def Fraction(self, a, b):
        self.Result = Division.fraction(a, b)
        return self.Result

    def Power(self, a, b):
        self.Result = Exponent.power(a, b)
        return self.Result

    def Root(self, a, b):
        self.Result = nthRoot.NthRoot(a, b)
        return self.Result

    def Log(self, a, b):
        self.Result = Log.logarithm(a, b)
        return self.Result
