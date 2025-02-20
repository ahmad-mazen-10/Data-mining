# Assignment (1):
# • –We want to know your grade ( Pass / Good / Very Good /
# Excellent )from your degree. So , you should receive the
# following values from the user : Name , Department , Degree .
# Then show the following (Demo) : Hello Mohammed ,
# “Your
# department is IS and your degree is <<GRADE>>! ” .

def get_grade(degree):
    if degree >= 85:
        return "Excellent"
    elif degree >= 75:
        return "Very Good"
    elif degree >= 60:
        return "Good"
    elif degree >= 50:
        return "Pass"
    else:
        return "Fail"

name = input("Enter your name: ")
department = input("Enter your department: ")
degree = float(input("Enter your degree: "))

grade = get_grade(degree)

print(f"Hello {name}, “Your department is {department} and your degree is {grade}!”")
