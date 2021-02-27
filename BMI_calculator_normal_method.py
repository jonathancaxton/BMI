height = float(input("what is your height in cm:"))
weight = float(input("what is your weight in kg:"))

BMI = weight/((height/100)*(height/100))


print(BMI)

if BMI < 18.5:
    print("you are under weight")

elif BMI <= 25:
    print("you are normal weight")

elif BMI < 30: 
    print("you are overweight")

elif BMI > 30:
    print("you are obese")

else:
    ("you didnt put the right value in")