height = float(input("Enter your height in meters:"))
weight = float(input("Enter your weight in kilograms"))

bmi = weight/(height**2)

if bmi <= 18.4:
    category = "underweight"
elif 18.5 <= bmi <= 24.9:
    category = "normal"
elif 25.0 <= bmi <= 39.9:
    category = "overweight"

else:
    category = "obese"
print(f"Your BMI is{bmi} and your category is {category}")