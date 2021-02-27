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