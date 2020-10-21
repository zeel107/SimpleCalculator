"""
Name: Aidan Fallstrom
Description: A simple calculator.  Can handle (“+”,”-“,”*”,”/”, ”^”, sin, cos, tan, cot, ln, log10) with
real numbers involving parenthesis (“()”)
"""
import math


class Calculator:

    def __init__(self, num_digits=11):
        self.operators = ['c', 'l', 't', 's', '/', '^', '*', '-', '+']
        self.digits=num_digits

    def calculate(self, equation):
        equation = self.__format_string(equation)
        ans = self.__compute(equation)
        if(type(ans) == str):
            return ans
        ans = round(ans, self.digits)
        return ans

    def __format_string(self, equation):
        # remove all spaces
        equation = equation.replace(" ", "")
        # simplify -+ and +- to -
        equation = equation.replace("-+", "-")
        equation = equation.replace("+-", "-")
        # simplify -- to +
        equation = equation.replace("--", "+")

        # replace ")(" with ")*("
        equation = equation.replace(")(", ")*(")

        # replace "x(" with "x*(" and ")x" with ")*x" where x is an int 1-9
        for i in range(10):
            num = str(i)
            num_left = num + "("
            num_right = ")" + num
            equation = equation.replace(num_left, num + "*(")
            equation = equation.replace(num_right, ")*" + num)

        # handle cases where - is a urinary operator.  2^-2 will not give the right answer.  Change to 2^(-2)
        arr = equation.split("-")
        while(len(arr) >= 2):
            if(arr[0] == ''):       # the first number/expression is negated
                arr[0] = arr[0] + "-" + arr[1]
                del arr[1]
            elif(arr[0][-1] == ')' or arr[0][-1] == '('):     # if ')' then this is a subtraction. if '(' then the number/expression to the right is negated
                arr[0] = arr[0] + "-" + arr[1]
                del arr[1]
            elif(arr[0][-1] == '*' or arr[0][-1] == '/' or arr[0][-1] == '^'):        # equation has something like 2*-2
                # find where the matching ) is going to go
                operator_index = -1
                for i in range(len(arr[1])):
                    if(not arr[1][i].isdigit()):
                        operator_index = i
                        break

                if operator_index == -1:        # there are no operators in arr[1]
                    arr[0] = arr[0] + "(-" + arr[1] + ")"
                    del arr[1]
                else:                           # split arr[1] on the first operator
                    temp = arr[1].split(arr[1][operator_index], 1)
                    arr[0] = arr[0] + "(-" + temp[0] + ")" + arr[1][operator_index] + temp[1]
                    del arr[1]
            else:
                arr[0] = arr[0] + "-" + arr[1]
                del arr[1]

        return arr[0]

    def __get_order(self, operator):
        if (operator == '+' or operator == '-'):
            return 4
        elif (operator == '*' or operator == '/'):
            return 3
        elif (operator == '^'):
            return 2
        elif (operator == 's' or operator == 'c' or operator == 't' or operator == 'l'):  # if the operation is sin, cos, cot, tan, ln, or log
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
            return float(str)

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
        if (operator == ''):  # there is no operator, so the str may be inclosed with (), so remove those and return the answer
            if (str.count('(') > 0):
                # remove the ()
                return self.__compute(self.__remove_paren(str))
            else:
                return float(str)

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

        try:
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
                return math.sin(math.radians(self.__compute(split[1])))
            if (operator == 'cos'):
                return math.cos(math.radians(self.__compute(split[1])))
            if (operator == 'cot'):
                ans = math.radians(self.__compute(split[1]))
                return math.cos(ans) / math.sin(ans)
            if (operator == 'tan'):
                return math.tan(math.radians(self.__compute(split[1])))
            if (operator == 'ln'):
                return math.log(self.__compute(split[1]), math.e)
            if (operator == 'log'):
                return math.log(self.__compute(split[1]), 10)
        except:
            return "undefined"


