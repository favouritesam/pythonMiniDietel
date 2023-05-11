weightInPounds = float(input("Enter your weight in pounds"))
heightInInches = float(input("Enter your height in inches"))

Bmi = weightInPounds * 703 / heightInInches * heightInInches
underWeight = 18.5
normalWeight = 24.9
overWeight = 29.9
obesityClass = 39.9

print("BMI ={:.1f}".format(Bmi))
if Bmi < underWeight:
    print("your under weight")
elif Bmi < normalWeight:
    print("your weight is normal")
elif Bmi < overWeight:
    print("you are over weight")
else:
    print("you are obese")
