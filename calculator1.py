import tkinter as tk

# Original math functions
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error: DIVBY0"
def power(x, y): return x ** y
def mod(x, y): return x % y if y != 0 else "Error: MOD0"

# UI callbacks
def click(char):
    entry.insert(tk.END, char)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expr = entry.get()
        for op, func in [("**", power), ("%", mod), ("/", divide),
                         ("*", multiply), ("-", subtract), ("+", add)]:
            if op in expr:
                x_str, y_str = expr.split(op)
                result = func(float(x_str), float(y_str))
                entry.delete(0, tk.END)
                entry.insert(tk.END, str(result))
                return
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Invalid")
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Window & styling setup
window = tk.Tk()
window.title("kLub's Aesthetic Calculator")
window.configure(bg="#2E2F33")

# Centering frame
frame = tk.Frame(window, bg="#2E2F33", padx=10, pady=10)
frame.pack(expand=True)

# Entry field
entry = tk.Entry(frame, width=25, font=("Segoe UI", 18),
                 bg="#F5F7FA", fg="#2E2F33", bd=0, justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=(0,10))

# Button config
btn_cfg = {"font":("Segoe UI",14), "bd":0, "width":5, "height":2}
colors = {
    "num": "#E1E5EA",
    "op": "#A0B3C5",
    "eq": "#6C8CBD",
    "quit": "#D36C6C"
}

buttons = [
    ('7',1,0),('8',1,1),('9',1,2),('+',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('-',2,3),
    ('1',3,0),('2',3,1),('3',3,2),('*',3,3),
    ('0',4,0),('.',4,1),('%',4,2),('/',4,3),
    ('**',5,0),('C',5,1),('=',5,2)
]

# Place buttons
for (text, r, c) in buttons:
    if text == '=':
        bg = colors["eq"]
        cmd = calculate
    elif text == 'C':
        bg = colors["quit"]
        cmd = clear
    else:
        bg = colors["op"] if text in "+-*/%**" else colors["num"]
        cmd = lambda t=text: click(t)
    tk.Button(frame, text=text, bg=bg, fg="#2E2F33", **btn_cfg,
              command=cmd).grid(row=r, column=c, padx=5, pady=5)

# Add Quit button bottom-right
tk.Button(frame, text="Quit", bg=colors["quit"], fg="#FFF",
          command=window.destroy, **btn_cfg).grid(row=5, column=3)

# Center window on screen
window.update_idletasks()
x = (window.winfo_screenwidth()//2) - (window.winfo_width()//2)
y = (window.winfo_screenheight()//2) - (window.winfo_height()//2)
window.geometry(f'+{x}+{y}')

window.mainloop()
