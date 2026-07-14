print("==========BMI Calculator==========")

try:
    weight = float(input("Enter your Weight(kg):"))
    height = float(input("Enter your Height(m):"))

    if weight<=0 or height<=0:
        print("Error: Weight and Height must be greater than 0.")
    else:
        bmi = weight/(height**2)
        print(f"\n Your BMI Value is: {bmi:.2f}")

        if bmi<18.5:
            print("Category: Underweight")
        elif bmi<25:
            print("Category: Normal weight")
        elif bmi<30:
            print("Category: Overweight")
        else:
            print("Category: Obese")
    
except ValueError:
    print("Error: Enter valid numeric values only.")