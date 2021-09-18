# Using tkinter for making GUI
from tkinter import *
# making GUI window
root = Tk()
root.title("Calculator")# Giving a title to GUI
root.configure(background="orange")# giving a background to GUI
root.resizable(0,0)

# Adding a entry widget to use the calculator GUI
screen_window = Entry(root, width=35, borderwidth=5, font="classic1 15 bold")
screen_window.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# adding a number to using the calculator
def click(number):
    window_number = screen_window.get()
    screen_window.delete(0, END)
    screen_window.insert(0, str(window_number) + str(number))

# adding a delete function
def clear():
    screen_window.delete(0, END)

# adding a backspace function
def backspace():
    screen_window.delete(1-1)

# making add addition function
def add_button():
    first_number = screen_window.get()
    global f_num
    global math
    math = "addition"
    f_num =int(first_number)
    screen_window.delete(0, END)

# making a substraction function
def subtraction():
    first_number = screen_window.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    screen_window.delete(0, END)

# making a multipliction function
def multiplication():
    first_number = screen_window.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    screen_window.delete(0, END)

# making a division function
def division():
    first_number = screen_window.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    screen_window.delete(0, END)

# making a percentage function
def percentage():
    first_number = screen_window.get()
    global f_num
    global math
    math = "percentage"
    f_num = int(first_number)
    screen_window.delete(0, END)

# making a equal function
def equal():
    second_number = screen_window.get()
    screen_window.delete(0, END)

    if math == "addition":
        screen_window.insert(0, f_num + int(second_number))

    elif math == "subtraction":
        screen_window.insert(0, f_num - int(second_number))

    elif math == "multiplication":
        screen_window.insert(0, f_num * int(second_number))

    elif math == "division":
        screen_window.insert(0, f_num / int(second_number))

    elif math == "percentage":
        screen_window.insert(0, f_num % int(second_number))

# making a number button to use the calculator
bg = background="yellow"
buttons_1 = Button(root, text="1", padx=40, pady=20, font="poetry 10 bold", bg="yellow", fg="black", command=lambda: click(1)).grid(row=4, column=0)
buttons_2 = Button(root, text="2", padx=40, pady=20, font="poetry 10 bold", bg="yellow", fg="black", command=lambda: click(2)).grid(row=4, column=1)
buttons_3 = Button(root, text="3", padx=40, pady=20, font="poetry 10 bold", bg="yellow", fg="black", command=lambda: click(3)).grid(row=4, column=2)
buttons_4 = Button(root, text="4", padx=40, pady=20, font="poetry 10 bold", bg="yellow", fg="black", command=lambda: click(4)).grid(row=3, column=0)
buttons_5 = Button(root, text="5", padx=40, pady=20, font="poetry 10 bold", bg="yellow", fg="black", command=lambda: click(5)).grid(row=3, column=1)
buttons_6 = Button(root, text="6", padx=40, pady=20, font="poetry 10 bold", bg="yellow", fg="black", command=lambda: click(6)).grid(row=3, column=2)
buttons_7 = Button(root, text="7", padx=40, pady=20, font="poetry 10 bold", bg="yellow", fg="black", command=lambda: click(7)).grid(row=2, column=0)
buttons_8 = Button(root, text="8", padx=40, pady=20, font="poetry 10 bold", bg="yellow", fg="black", command=lambda: click(8)).grid(row=2, column=1)
buttons_9 = Button(root, text="9", padx=40, pady=20, font="poetry 10 bold", bg="yellow", fg="black", command=lambda: click(9)).grid(row=2, column=2)
buttons_0 = Button(root, text="0", padx=40, pady=20, font="poetry 10 bold", bg="yellow", fg="black", command=lambda: click(0)).grid(row=5, column=1)
buttons_00 = Button(root, text="00", padx=38, pady=20, font="poetry 10 bold", bg="yellow", fg="black", command=lambda: click(00)).grid(row=5, column=0)

# making some function to use our calculator
buttons_clear = Button(root, text="C", padx=40, pady=20, font="poetry 10 bold", bg="yellow", fg="black", command=clear).grid(row=1, column=0)
buttons_percentage = Button(root, text="%", padx=38, pady=20, font="poetry 10 bold", bg="yellow", fg="black", command=percentage).grid(row=1, column=2)
buttons_divide = Button(root, text="÷", padx=39, pady=20, font="poetry 10 bold", bg="yellow", fg="black", command=division).grid(row=1, column=3)
buttons_multiple = Button(root, text="*", padx=40, pady=20, font="poetry 10 bold", bg="yellow", fg="black", command=multiplication).grid(row=2, column=3)
buttons_substract = Button(root, text="-", padx=40, pady=20, font="poetry 10 bold", bg="yellow", fg="black", command=subtraction).grid(row=3, column=3)
buttons_add = Button(root, text="+", padx=39, pady=20, font="poetry 10 bold", bg="yellow", fg="black", command=add_button).grid(row=4, column=3)
buttons_equal = Button(root, text="=", padx=93, pady=20, font="poetry 10 bold", bg="yellow", fg="black", command=equal).grid(row=5, column=2, columnspan=4)
buttons_backspace = Button(root, text="X", padx=39, pady=20, font="poetry 10 bold", bg="yellow", fg="black", command=backspace).grid(row=1, column=1)

# making a mainloop function to use our calculator
root.mainloop()