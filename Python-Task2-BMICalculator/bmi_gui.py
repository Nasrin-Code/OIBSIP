import tkinter as tk
from tkinter import messagebox
import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("400x300")
window.resizable(False,False)

name_label = tk.Label(window, text = "Name", font = ("Arial", 12))
name_label.pack(pady = 1)

name_entry = tk.Entry(window)
name_entry.pack(pady = 1)

weight_label = tk.Label(window, text = "Weight (kg)", font = ("Arial", 12))
weight_label.pack(pady = 1)

weight_entry = tk.Entry(window)
weight_entry.pack(pady = 1)

height_label = tk.Label(window, text = "Height (m)", font = ("Arial", 12))
height_label.pack(pady = 1)

height_entry = tk.Entry(window)
height_entry.pack(pady = 1)

def calculate_bmi():
    try:
        name = name_entry.get()
        weight = float(weight_entry.get())
        height = float(height_entry.get())
    
        if weight<=0 or height<=0:
            messagebox.showerror("Invalid Input, Weight and Height must be greater than zero.")
            return
        bmi = weight/(height**2)
        current_time = datetime.now().strftime("%d-%m-%Y %I:%M %p")
        if bmi<18.5:
            category = "Underweight"
            color = "blue"
        elif bmi<25:
            category = "Normalweight"
            color = "green"
        elif bmi<30:
            category = "Overweight"
            color = "orange"
        else:
            category = "Obese"
            color = "red"
    except ValueError:
        messagebox.showerror("Invalid Input, Enter numeric values only.")
    
    file_exists = os.path.exists("bmi_data.csv")
    with open("bmi_data.csv", "a", newline = "") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Name", "Weight", "Height", "BMI", "Category", "Date & Time"])
        writer.writerow([name, weight, height, round(bmi,2), category, current_time])

    result_label.config(text = f"BMI = {bmi:.2f}\nCategory = {category}", fg = color)
calculate_button = tk.Button(window, text = "Calculate BMI", command = calculate_bmi, bg = "green", fg = "white", font = ("Arial", 11))
calculate_button.pack(pady = 1)
result_label = tk.Label(window, text = "", font = ("Arial", 13))
result_label.pack(pady = 1)

def reset_fields():
    name_entry.delete(0,tk.END)
    weight_entry.delete(0,tk.END)
    height_entry.delete(0,tk.END)
    result_label.config(text = "")
reset_button = tk.Button(window, text = "Reset", command = reset_fields)
reset_button.pack(pady = 1)

def view_history():
    history_window = tk.Toplevel(window)
    history_window.title("BMI History")
    history_window.geometry("700x400")

    with open("bmi_data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            history_label = tk.Label(history_window, text = ",".join(row), anchor = "w")
            history_label.pack(pady = 1)
history_button = tk.Button(window, text = "View History", command = view_history)
history_button.pack(pady = 1)

def view_graph():
    bmi_values = []
    with open("bmi_data.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            bmi_values.append(float(row[3]))
    if len(bmi_values) == 0:
        messagebox.showinfo("No Data","No BMI records found.")
        return
    plt.figure(figsize=(8,5))
    plt.plot(bmi_values, marker = "o")
    plt.title("BMI History")
    plt.xlabel("Record Number")
    plt.ylabel("BMI")
    plt.grid()
    plt.show()
graph_button = tk.Button(window, text = "View Graph", command = view_graph)
graph_button.pack(pady = 1)

window.mainloop()
