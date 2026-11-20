height = float(input("Enter your height in cm: "))
wheight = float(input("Enter your weight in kg: "))

BMI = wheight / ((height / 100) ** 2)
print("Your BMI is:",BMI)

if BMI < 18.5:
    print("You are underweight.")
elif BMI < 24.9:
    print("You have a normal weight.")
elif BMI < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
