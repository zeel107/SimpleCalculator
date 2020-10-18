"""
Name: Aidan Fallstrom
Description: A simple calculator.  Can handle (“+”,”-“,”*”,”/”, ”^”, sin, cos, tan, cot, ln, log10) with
real numbers involving parenthesis (“()”)
"""
import math


class Calculator:

    def __init__(self):
        self.operators = ['c', 'l', 't', 's', '/', '^', '*', '-', '+']

    def calculate(self, equation):
        ans = self.__compute(equation)
        return ans

    def __get_order(self, operator):
        if (operator == '+' or operator == '-'):
            return 4
        elif (operator == '*' or operator == '/'):
            return 3
        elif (operator == '^'):
            return 2
        elif (
                operator == 's' or operator == 'c' or operator == 't' or operator == 'l'):  # if the operation is sin, cos, cot, tan, ln, or log
            return 1

    def __divide_str(self, str, index, operator):
        x = str.split(operator)
        while (len(x) > 2):
            if (len(x[0]) < index):
                x[0] = x[0] + operator + x[1]
                del x[1]
                continue
            x[1] = x[1] + operator + x[2]
            del x[2]

        return x

    def __remove_paren(self, str):
        x = str.split('(')
        del x[0]
        while (len(x) > 1):
            x[0] = x[0] + '(' + x[1]
            del x[1]

        x = x[0].split(')')
        del x[1]
        while (len(x) > 1):
            x[0] = x[0] + ')' + x[1]
            del x[1]

        return x[0]

    def __compute(self, str):
        if (len(str) == 0):
            return 0
        if (len(str) == 1):
            return int(str)

        order = -1
        operator = ''
        paren = 0
        index = 0
        i = 0
        while (i < len(str)):
            if (str[i] == '('):
                paren += 1
                i += 1
                continue
            if (str[i] == ')'):
                paren -= 1
                i += 1
                continue
            if (self.operators.count(str[i]) > 0 and paren == 0):
                if (self.__get_order(str[i]) >= order):
                    operator = str[i]
                    index = i
                    order = self.__get_order(str[i])
                    i += 1
                    if (operator == 'c'):
                        i += 2
                    continue
                else:
                    i += 1
                    continue
            i += 1
        if (
                operator == ''):  # there is no operator, so the str may be inclosed with (), so remove those and return the answer
            if (str.count('(') > 0):
                # remove the ()
                return self.__compute(self.__remove_paren(str))
            else:
                return int(str)

        if (operator == 'c'):
            if (str[index + 2] == 's'):
                operator = 'cos'
            elif (str[index + 2] == 't'):
                operator = 'cot'
        elif (operator == 's'):
            operator = 'sin'
        elif (operator == 't'):
            operator = 'tan'
        elif (operator == 'l'):
            if (str[index + 1] == 'n'):
                operator = 'ln'
            elif (str[index + 1] == 'o'):
                operator = 'log'

        split = self.__divide_str(str, index, operator)

        if (operator == '*'):
            return self.__compute(split[0]) * self.__compute(split[1])
        if (operator == '-'):
            return self.__compute(split[0]) - self.__compute(split[1])
        if (operator == '+'):
            return self.__compute(split[0]) + self.__compute(split[1])
        if (operator == '/'):
            return self.__compute(split[0]) / self.__compute(split[1])
        if (operator == '^'):
            return self.__compute(split[0]) ** self.__compute(split[1])
        if (operator == 'sin'):
            return math.sin(self.__compute(split[1]))
        if (operator == 'cos'):
            return math.cos(self.__compute(split[1]))
        if (operator == 'cot'):
            return 1 / math.tan(self.__compute(split[1]))
        if (operator == 'tan'):
            return math.tan(self.__compute(split[1]))
        if (operator == 'ln'):
            return math.log(self.__compute(split[1]), math.e)
        if (operator == 'log'):
            return math.log(self.__compute(split[1]), 10)


c = Calculator()

print(c.calculate("sin(4*(4^ln(7)))"))
print(c.calculate("(2^(2^(2^2)))^2"))
print(c.calculate("(5+3)*2"))
