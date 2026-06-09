import tkinter as tk

count = 0

def increase():
    global count
    count += 1
    label.config(text=f"Count: {count}")

def decrease():
    global count
    count -= 1
    label.config(text=f"Count: {count}")

def reset():
    global count
    count = 0
    label.config(text=f"Count: {count}")

app = tk.Tk()
app.title("Simple Counter App")
app.geometry("300x200")

label = tk.Label(app, text="Count: 0", font=("Arial", 20))
label.pack(pady=20)

btn_frame = tk.Frame(app)
btn_frame.pack()

tk.Button(btn_frame, text="+", width=5, command=increase).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="-", width=5, command=decrease).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Reset", width=5, command=reset).grid(row=0, column=2, padx=5)

app.mainloop()
