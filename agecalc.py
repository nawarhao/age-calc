import tkinter as tk
from datetime import date

def calculate_age():
    try:
        day = int(entry_day.get())
        month = int(entry_month.get())
        year = int(entry_year.get())
        dob = date(year, month, day)
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        result_label.config(text=f"Your Age: {age} years")
    except ValueError:
        result_label.config(text="Invalid input! Please enter valid numbers.")

# Tkinter window
root = tk.Tk()
root.title("Age Calculator App")

# Labels and Entry fields
tk.Label(root, text="Day:").grid(row=0, column=0)
entry_day = tk.Entry(root)
entry_day.grid(row=0, column=1)

tk.Label(root, text="Month:").grid(row=1, column=0)
entry_month = tk.Entry(root)
entry_month.grid(row=1, column=1)

tk.Label(root, text="Year:").grid(row=2, column=0)
entry_year = tk.Entry(root)
entry_year.grid(row=2, column=1)

# Button
calc_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calc_button.grid(row=3, column=0, columnspan=2)

# Result Label
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
