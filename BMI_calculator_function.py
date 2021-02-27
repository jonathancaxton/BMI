#BMI calculator for men 
#from BMI_library

weight = int(input("What is your weight in kg ?:"))
height = int(input("What is your height cm ?:"))

def BMI (x,y) :
   bmivalue =  x/((y/100)*(y/100))
   if bmivalue < 18.5:
       return "Your BMI is " + "{:.2f}".format(bmivalue) + "," + "your're  underweight." 
   elif bmivalue <= 25:
       return "Your BMI is " +  "{:.2f}".format(bmivalue) + "," + "your're normal weight."
   elif bmivalue < 30:
       return "Your BMI is " + "{:.2f}".format(bmivalue) + "," + "your're overweight."
   else: 
       return "Your BMI is " +  "{:.2f}".format(bmivalue) + "," + "you're obese."


print(I(weight,height))
