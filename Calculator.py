import tkinter as tk

# ===== STYLISH CALCULATOR WITH TKINTER =====
root = tk.Tk()
root.title("Varsh - Calculator")
root.geometry("340x520")
root.configure(bg="#0a0a0f")
root.resizable(False, False)

# Display variable
expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set(" Error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)

# Display
equation = tk.StringVar()
display_frame = tk.Frame(root, bg="#0a0a0f")
display_frame.pack(pady=20, padx=20, fill="x")

display = tk.Label(display_frame, textvariable=equation, font=("JetBrains Mono", 26, "bold"),
                   bg="#15151e", fg="#e8e8f0", anchor="e", height=2, 
                   padx=20, bd=0, relief="flat")
display.pack(fill="x", ipady=10)
# rounded effect via border
display.config(highlightbackground="#2a2a3d", highlightthickness=1)

# Buttons frame
btn_frame = tk.Frame(root, bg="#0a0a0f")
btn_frame.pack(padx=15, pady=10)

# Button style function
def create_btn(frame, text, cmd, bg="#1e1e2e", fg="white", col=0, row=0, colspan=1):
    btn = tk.Button(frame, text=text, font=("Space Grotesk", 16, "bold"),
                    bg=bg, fg=fg, activebackground="#6c5ce7", activeforeground="white",
                    bd=0, relief="flat", padx=10, pady=18,
                    command=cmd, cursor="hand2")
    btn.grid(row=row, column=col, columnspan=colspan, padx=6, pady=6, sticky="nsew")
    # hover effect
    def on_enter(e):
        btn['bg'] = "#2a2a3d" if bg != "#6c5ce7" and bg != "#ff5f56" else btn['bg']
    def on_leave(e):
        btn['bg'] = bg
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn

# Configure grid weights
for i in range(4):
    btn_frame.grid_columnconfigure(i, weight=1)

# Row 0
create_btn(btn_frame, "C", clear, bg="#ff5f56", col=0, row=0)
create_btn(btn_frame, "⌫", backspace, bg="#2a2a3d", col=1, row=0)
create_btn(btn_frame, "%", lambda: press("%"), bg="#2a2a3d", col=2, row=0)
create_btn(btn_frame, "÷", lambda: press("/"), bg="#6c5ce7", col=3, row=0)

# Row 1
create_btn(btn_frame, "7", lambda: press(7), col=0, row=1)
create_btn(btn_frame, "8", lambda: press(8), col=1, row=1)
create_btn(btn_frame, "9", lambda: press(9), col=2, row=1)
create_btn(btn_frame, "×", lambda: press("*"), bg="#6c5ce7", col=3, row=1)

# Row 2
create_btn(btn_frame, "4", lambda: press(4), col=0, row=2)
create_btn(btn_frame, "5", lambda: press(5), col=1, row=2)
create_btn(btn_frame, "6", lambda: press(6), col=2, row=2)
create_btn(btn_frame, "-", lambda: press("-"), bg="#6c5ce7", col=3, row=2)

# Row 3
create_btn(btn_frame, "1", lambda: press(1), col=0, row=3)
create_btn(btn_frame, "2", lambda: press(2), col=1, row=3)
create_btn(btn_frame, "3", lambda: press(3), col=2, row=3)
create_btn(btn_frame, "+", lambda: press("+"), bg="#6c5ce7", col=3, row=3)

# Row 4
create_btn(btn_frame, "0", lambda: press(0), col=0, row=4, colspan=2)
create_btn(btn_frame, ".", lambda: press("."), col=2, row=4)
create_btn(btn_frame, "=", equalpress, bg="#00ff88", fg="#0a0a0f", col=3, row=4)

# Footer
footer = tk.Label(root, text="varsh.dev • B.Sc IT • Python Tkinter", 
                  font=("JetBrains Mono", 9), bg="#0a0a0f", fg="#9a9ab0")
footer.pack(side="bottom", pady=12)

root.mainloop()