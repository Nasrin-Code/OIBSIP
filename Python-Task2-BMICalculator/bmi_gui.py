import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("400x300")
window.resizable(False,False)
weight_label = tk.Label(window, text = "Weight (kg)", font = ("Arial", 12))
weight_label.pack(pady = 8)

weight_entry = tk.Entry(window)
weight_entry.pack(pady = 8)

height_label = tk.Label(window, text = "Height (m)", font = ("Arial", 12))
height_label.pack(pady = 8)

height_entry = tk.Entry(window)
height_entry.pack(pady = 8)

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
    
        if weight<=0 or height<=0:
            messagebox.showerror("Invalid Input, Weight and Height must be greater than zero.")
            return
        bmi = weight/(height**2)
        if bmi<18.5:
            category = "Underweight"
        elif bmi<25:
            category = "Normalweight"
        elif bmi<30:
            category = "Overweight"
        else:
            category = "Obese"
    except ValueError:
        messagebox.showerror("Invalid Input, Enter numeric values only.")

    result_label.config(text = f"BMI = {bmi:.2f}\nCategory = {category}")
calculate_button = tk.Button(window, text = "Calculate BMI", command = calculate_bmi, bg = "green", fg = "white", font = ("Arial", 11))
calculate_button.pack(pady = 8)
result_label = tk.Label(window, text = "", font = ("Arial", 13))
result_label.pack(pady = 8)

def reset_fields():
    weight_entry.delete(0,tk.END)
    height_entry.delete(0,tk.END)
    result_label.config(text = "")
reset_button = tk.Button(window, text = "Reset", command = reset_fields)
reset_button.pack(pady = 8)

window.mainloop()