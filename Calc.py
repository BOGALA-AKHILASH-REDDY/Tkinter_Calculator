
'''
import tkinter as tk  # Imports Tkinter module

# Function called when a number or operator is clicked
def press(v):
    entry.insert(tk.END, v)  # Inserts the pressed value at the end of Entry widget

# Clears the Entry widget
def clear():
    entry.delete(0, tk.END)

# Calculates the result of the expression
def calc():
    try:
        result = eval(entry.get())  # Evaluates the expression
        entry.delete(0, tk.END)     # Clear the screen
        entry.insert(0, result)     # Display the result
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")    # Handles errors

# Main window creation
root = tk.Tk()  # Creates main application window
root.title("Calculator")
root.geometry("300x400")  # Sets window size
root.resizable(0, 0)      # Prevents resizing
root.configure(bg="lightblue")  # Sets background color

# Entry widget for display screen
entry = tk.Entry(
    root,
    width=16,
    font=('Arial', 24),
    bd=0,
    fg="white",
    bg="black",
    relief=tk.RIDGE,
    justify='right'
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)  # Place entry

# Calculator buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Loop to create buttons
row_val = 1
col_val = 0
for b in buttons:
    cmd = calc if b == '=' else lambda x=b: press(x)  # Assign command

    tk.Button(
        root,
        text=b,
        width=5,
        height=2,
        font=('Calibri', 18),
        bd=0,
        fg="black",
        bg="white",
        command=cmd
    ).grid(row=row_val, column=col_val, padx=5, pady=5)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
tk.Button(
    root,
    text="C",
    width=5,
    height=2,
    font=('Calibri', 18),
    bd=0,
    fg="black",
    bg="red",
    command=clear
).grid(row=row_val, column=0, padx=5, pady=5, columnspan=4)  # Span across full row

# Start the main event loop
root.mainloop()
'''


import tkinter as tk

def press(v):
    entry.insert(tk.END, v)

def clear():
    entry.delete(0, tk.END)
def backspace():
    current=entry.get()
    if current:
        entry.delete(len(current)-1,tk.END)
        '''Deletes last digit if entry is not empty'''

def cal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid Expression")

# Main window
root = tk.Tk()
root.title("Calculator")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

# Entry widget
entry = tk.Entry(
    root,
    font=("Times New Roman", 20),
    bg="#ffffff",
    bd=0,
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12, ipady=10)

# Buttons
Buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
]

r, c = 1, 0
for b in Buttons:
    cmd = cal if b == "=" else lambda x=b: press(x)
    tk.Button(
        root,
        text=b,
        command=cmd,
        font=("Calibri", 14),
        width=5,
        height=2,
        bg="#ff9500" if b in "+-*/" else "black",
        fg="white",
        bd=0
    ).grid(row=r, column=c, padx=6, pady=6)

    c += 1
    if c == 4:
        r += 1
        c = 0

# Clear button
tk.Button(
    root,
    text="C",
    command=clear,
    font=("Calibri", 14),
    bg="#ff3b3b",
    fg="white",
    bd=0,
    width=22,
    height=2
).grid(row=r, column=0, columnspan=4, pady=8)

#Backspace Button
tk.Button(
    root,
    text="B",
    command=backspace,
    width=10,
    height=2,
    font=("Calibri", 14),
    bg="lightblue",
    fg="black",
    bd=0,
).grid(row=r, column=2,columnspan=2,pady=8)


root.mainloop()
