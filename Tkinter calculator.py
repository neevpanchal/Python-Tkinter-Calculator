import tkinter as tk

# Function to handle button clicks
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# Function to clear the display
def button_clear():
    entry.delete(0, tk.END)

# Function to calculate the result
def button_equal():
    try:
        expression = entry.get()
        result = eval(expression, {"__builtins__": {}}, {})
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(0, "Cannot divide by zero")
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Create the input/display field
entry = tk.Entry(
    root,
    width=20,
    font=("Arial", 18),
    justify="right",
    borderwidth=5
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define calculator buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create and arrange buttons
for text, row, col in buttons:
    if text == 'C':
        command = button_clear
    elif text == '=':
        command = button_equal
    else:
        command = lambda value=text: button_click(value)

    button = tk.Button(
        root,
        text=text,
        font=("Arial", 14),
        width=5,
        height=2,
        command=command
    )
    button.grid(row=row, column=col, padx=5, pady=5)

# Run the application
root.mainloop()