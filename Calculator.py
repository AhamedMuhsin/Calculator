# Using tkinter for making GUI
from tkinter import *
# making GUI window
root = Tk()
root.title("Calculator")# Giving a title to GUI
root.wm_iconbitmap("C:\\Users\\MUHSIN\\My Projects\\Calculator\\icon_cal.ico")
root.configure(background="orange")# giving a background to GUI
root.resizable(0,0)

# Adding a entry widget to use the calculator GUI
scvalue = StringVar()
scvalue.set("")
screen_window = Entry(root, textvar=scvalue, width=35, borderwidth=5, font="classic 15 bold")
screen_window.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# making a functions which operaters our calculator
def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=": #making a equal to functions
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen_window.get())
            except Exception as e:
                value = "Error"

        scvalue.set(value)
        screen_window.update()

    elif text == "C": #making a delete screen functions
        scvalue.set("")
        screen_window.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen_window.update()

def backspace():
    screen_window.delete(1-1)

# making a number button to use the calculator
bg = background="yellow"
buttons_1 = Button(root, text="1", padx=40, pady=20, font="poetry 10 bold", bg="yellow", fg="black")
buttons_2 = Button(root, text="2", padx=40, pady=20, font="poetry 10 bold", bg="yellow", fg="black")
buttons_3 = Button(root, text="3", padx=40, pady=20, font="poetry 10 bold", bg="yellow", fg="black")
buttons_4 = Button(root, text="4", padx=40, pady=20, font="poetry 10 bold", bg="yellow", fg="black")
buttons_5 = Button(root, text="5", padx=40, pady=20, font="poetry 10 bold", bg="yellow", fg="black")
buttons_6 = Button(root, text="6", padx=40, pady=20, font="poetry 10 bold", bg="yellow", fg="black")
buttons_7 = Button(root, text="7", padx=40, pady=20, font="poetry 10 bold", bg="yellow", fg="black")
buttons_8 = Button(root, text="8", padx=40, pady=20, font="poetry 10 bold", bg="yellow", fg="black")
buttons_9 = Button(root, text="9", padx=40, pady=20, font="poetry 10 bold", bg="yellow", fg="black")
buttons_0 = Button(root, text="0", padx=40, pady=20, font="poetry 10 bold", bg="yellow", fg="black")
buttons_dot = Button(root, text=".", padx=41, pady=20, font="poetry 10 bold", bg="yellow", fg="black")

# seting all the buttons in a table form
buttons_1.grid(row=4, column=0)
buttons_2.grid(row=4, column=1)
buttons_3.grid(row=4, column=2)
buttons_4.grid(row=3, column=0)
buttons_5.grid(row=3, column=1)
buttons_6.grid(row=3, column=2)
buttons_7.grid(row=2, column=0)
buttons_8.grid(row=2, column=1)
buttons_9.grid(row=2, column=2)
buttons_0.grid(row=5, column=1)
buttons_dot.grid(row=5, column=0)

# binding all buttons with each other
buttons_1.bind("<1>", click)
buttons_2.bind("<1>", click)
buttons_3.bind("<1>", click)
buttons_4.bind("<1>", click)
buttons_5.bind("<1>", click)
buttons_6.bind("<1>", click)
buttons_7.bind("<1>", click)
buttons_8.bind("<1>", click)
buttons_9.bind("<1>", click)
buttons_0.bind("<1>", click)
buttons_dot.bind("<1>", click)

# making some function to use our calculator
buttons_clear = Button(root, text="C", padx=40, pady=20, font="poetry 10 bold", bg="yellow", fg="black")
buttons_percentage = Button(root, text="%", padx=38, pady=20, font="poetry 10 bold", bg="yellow", fg="black")
buttons_divide = Button(root, text="/", padx=40, pady=20, font="poetry 10 bold", bg="yellow", fg="black")
buttons_multiple = Button(root, text="*", padx=40, pady=20, font="poetry 10 bold", bg="yellow", fg="black")
buttons_substract = Button(root, text="-", padx=40, pady=20, font="poetry 10 bold", bg="yellow", fg="black")
buttons_add = Button(root, text="+", padx=39, pady=20, font="poetry 10 bold", bg="yellow", fg="black")
buttons_equal = Button(root, text="=", padx=93, pady=20, font="poetry 10 bold", bg="yellow", fg="black")
buttons_backspace = Button(root, text="X", padx=39, pady=20, font="poetry 10 bold", bg="yellow", fg="black", command=backspace).grid(row=1, column=1)

# seting all the buttons in a table form
buttons_clear.grid(row=1, column=0)
buttons_percentage.grid(row=1, column=2)
buttons_divide.grid(row=1, column=3)
buttons_multiple.grid(row=2, column=3)
buttons_substract.grid(row=3, column=3)
buttons_add.grid(row=4, column=3)
buttons_equal.grid(row=5, column=2, columnspan=4)

# binding all buttons with each other
buttons_clear.bind("<1>", click)
buttons_percentage.bind("<1>", click)
buttons_divide.bind("<1>", click)
buttons_multiple.bind("<1>", click)
buttons_substract.bind("<1>", click)
buttons_add.bind("<1>", click)
buttons_equal.bind("<1>", click)

# making a mainloop function to use our calculator
root.mainloop()