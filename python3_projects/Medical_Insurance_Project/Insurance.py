age =22
sex = "Male"
name = input("Enter Your Name")
#  if we not add float then this show error because this think height and weight is string and in bmi formula we are trying mathimatical operation.
weight = float(input("Enter your weight in kg"))
height = float(input("Enter you r height in meter"))
bmi = weight/( height ** 2)
rounded_bmi= round(bmi ,2)
print(name + "BMI is this :"+ str(rounded_bmi))