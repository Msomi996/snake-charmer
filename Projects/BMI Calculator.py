name = input("Enter your name: ")
weight = int(input("Enter your weight in pounds: "))
height = int(input("Enter your height in inches: "))
BMI = (weight * 703) / (height * height)
print("Your BMI is: " + str(BMI))

if BMI>0:
 if (BMI < 18.5):
    print(name + ", you are in the underweight range.")
 elif (BMI <= 24.9):
    print(name + ", your weight is within the normal range. Keep it up.")  

 elif (BMI <= 29.9):
    print(name + ", you are in the overweight range.") 

 elif (BMI <= 34.9):
    print(name + ", you are in the obesity range.") 

 elif (BMI <= 39.9):
    print(name + ", you are in the severe obesity range.") 

 elif (BMI > 40):
    print(name + ", you are in the highest obesity range.") 
else:
        print('Please enter valid inputs.')




