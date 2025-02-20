# Assignment (2):
# – BMI (Body Mass Index) is a measurement of body fat based on
# • height and weight that applies to both men and women between the
# ages of 18 and 65 years. BMI can be used to indicate if you are
# overweight, obese, underweight or normal.
# – You should receive the following fields : Name , Weight (KG), Height
# (CM).
# – Use the following formula to calculate BMI :
# •BMI = (Weight in Kilograms / (Height in Meters x Height in
# Meters))
# • Notes :
# – bmi <= 18.5 then UNDERWEIGHT
# – bmi >18.5 AND bmi<=24.9 then NORMAL WEIGHT
# – bmi >24.9 AND num<=29.9 then OVERWEIGHT
# – bmi > 30.0 then OBESE
# • Demo for the final result:
# – "Your BMI value is <<BMI_VALUE>>and you are : <<STATUS>>

def calculate_bmi(weight, height):
    height_m = height / 100 
    bmi = weight / (height_m ** 2)

    if bmi <= 18.5:
        status = "UNDERWEIGHT"
    elif bmi <= 24.9:
        status = "NORMAL WEIGHT"
    elif bmi <= 29.9:
        status = "OVERWEIGHT"
    else:
        status = "OBESE"
    
    return bmi, status

name = input("Enter your name: ")
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (cm): "))

bmi, status = calculate_bmi(weight, height)

print(f"Your BMI value is {bmi:.2f} and you are: {status}")
