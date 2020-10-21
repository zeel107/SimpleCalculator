import tkinter as tk

from simple_calculator.calculator import Calculator

c = Calculator()
past_answers = []
past_equations = []

def solve_equation():
    ans = c.calculate(equation.get())
    ans_str.set(str(ans))
    past_answers.append(str(ans))
    past_equations.append(equation.get())


window = tk.Tk()
window.title("calculator")
window.geometry('800x600')

equation = tk.Entry(window, width="50")
equation.grid(row=0, column=0)
btn_enter = tk.Button(window, text="Enter", command=solve_equation)
btn_enter.grid(row=0, column=1)
ans_str = tk.StringVar(window)
ans_str.set("0")

ans_label = tk.Entry(window, textvariable=ans_str, width="50")
ans_label.grid(row=0, column=2)
window.mainloop()