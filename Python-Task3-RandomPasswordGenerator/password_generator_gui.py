import tkinter as tk
import secrets
import string

window = tk.Tk()
window.title("Random Password Generator")
window.geometry("500x450")
window.configure(bg="#f4f6f8")

password_history = []

label = tk.Label(window, text = "Random Password Generator", font = ("arial", 18, "bold"), fg = "Blue", bg="#f4f6f8")
label.pack(pady = 5)

label = tk.Label(window, text = "Password Length", bg="#f4f6f8")
label.pack(pady = 5)

entry = tk.Entry(window, width = 30)
entry.pack(pady = 5)

upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
digit_var = tk.BooleanVar()
symbol_var = tk.BooleanVar()
exclude_var = tk.BooleanVar()

upper_check = tk.Checkbutton(window, text = "Include Uppercase", variable = upper_var)
upper_check.pack(pady = 5)

lower_check = tk.Checkbutton(window, text = "Include Lowercase", variable = lower_var)
lower_check.pack(pady = 5)

digit_check = tk.Checkbutton(window, text = "Include Digit", variable = digit_var)
digit_check.pack(pady = 5)

symbol_check = tk.Checkbutton(window, text = "Include Symbol", variable = symbol_var)
symbol_check.pack(pady = 5)

exclude_check = tk.Checkbutton(window, text = "Exclude Ambiguous Characters", variable = exclude_var)
exclude_check.pack(pady = 5)

def generate_password():

    try:
        length = int(entry.get())

        if length<=0:
            result_label.config(text = "Length must be greater than zero.", bg="#f4f6f8")
            return
        
        characters = ""

        if upper_var.get():
            characters += string.ascii_uppercase

        if lower_var.get():
            characters += string.ascii_lowercase

        if digit_var.get():
            characters += string.digits

        if symbol_var.get():
            characters += string.punctuation

        if exclude_var.get():
            for char in "OoIl10":
                characters = characters.replace(char, "")

        if characters == "":
            result_label.config(text = "Select at least one option!", bg="#f4f6f8")
            return
        
        password = []

        if upper_var.get():
            password.append(secrets.choice(string.ascii_uppercase))

        if lower_var.get():
            password.append(secrets.choice(string.ascii_lowercase))

        if digit_var.get():
            password.append(secrets.choice(string.digits))

        if symbol_var.get():
            password.append(secrets.choice(string.punctuation))

        if length<len(password):
            result_label.config(text = f"Minimum length should be {len(password)}", bg="#f4f6f8")
            return

        for i in range(length - len(password)):
            password.append(secrets.choice(characters))

        secrets.SystemRandom().shuffle(password)
        password = "".join(password)
        password_history.append(password)
        history_box.delete("1.0",tk.END)

        for item in password_history:
            history_box.insert(tk.END, item + "\n")

        result_label.config(text = password, bg="#f4f6f8")
        check_strength(password)

    except ValueError:
        result_label.config(text = "Enter a valid number!", bg="#f4f6f8")

generate_button = tk.Button(window, text = "Generate Password", command = generate_password, bg="#4CAF50", fg="white", font=("Arial",11,"bold"))
generate_button.pack(pady = 5)

result_label = tk.Label(window, text = "Password will appear here", bg="#f4f6f8")
result_label.pack(pady = 5)

strength_label = tk.Label(window, text = "Strength: ", font = ("Arial", 12, "bold"), bg="#f4f6f8")
strength_label.pack(pady = 5)

def check_strength(password):

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    score = 0

    if has_upper:
        score += 1

    if has_lower:
        score += 1

    if has_digit:
        score += 1

    if has_symbol:
        score += 1

    if len(password)>=12:
        score += 1

    if score<=2:
        strength = "Weak"

    elif score<=4:
        strength = "Medium"

    else:
        strength = "Strong"

    if strength == "Weak":
        strength_label.config(
        text="Strength: Weak",
        fg="red")

    elif strength == "Medium":
        strength_label.config(
        text="Strength: Medium",
        fg="orange")

    else:
        strength_label.config(
        text="Strength: Strong",
        fg="green")

def copy_password():
    password = result_label.cget("text")

    window.clipboard_clear()
    window.clipboard_append(password)
    copy_status.config(text = "Password Copied", fg = "green")

copy_button = tk.Button(window, text = "Copy Password", command = copy_password, bg="#2196F3")
copy_button.pack(pady = 5)

copy_status = tk.Label(window, text = "", font = ("Arial", 10))
copy_status.pack(pady = 5)

history_label = tk.Label(window, text = "Password History", font = ("Arial", 12, "bold"), bg="#f4f6f8")
history_label.pack(pady = 5)

history_box = tk.Text(window, width = 35, height = 6)
history_box.pack(pady = 5)

window.mainloop()