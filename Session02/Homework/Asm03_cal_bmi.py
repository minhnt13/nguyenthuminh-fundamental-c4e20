hcm = int(input("Enter height in cm: "))
wgh = float(input("Enter weight in kg: "))
hm = hcm/100
bdmi = wgh/(hm*hm)
if bdmi < 16:
    print("Your BMI is: {}. You are 'Severely underweight'".format(round(bdmi,1)))
elif bdmi < 18.5:
    print("Your BMI is: {}. You are 'Underweight'".format(round(bdmi,1)))
elif bdmi < 25:
    print("Your BMI is: {}. You are 'Normal'".format(round(bdmi,1)))
elif bdmi < 30:
    print("Your BMI is: {}. You are 'Overweight'".format(round(bdmi,1)))
else:
    print("Your BMI is: {}. You are 'Obese'".format(round(bdmi,1)))