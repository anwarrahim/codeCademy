age = 22
sex = int(input("0 for female, 1 for male"))
name = input("Enter Your Name")
#  if we not add float then this show error because this think height and weight is string and in bmi formula we are trying mathimatical operation.
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter you r height in meter: "))
bmi = weight/( height ** 2)
rounded_bmi= round(bmi ,2)
print(name + "BMI is this :"+ str(rounded_bmi)) 
 
num_of_children = float(input("Enter Number of children: "))
smoker = int(input("0 for non-smokers, 1 for a smoker"))
insurance_cost = 250 * age - 128 * sex +370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

print("This person's insurance cost is " + str(insurance_cost) + " dollars.")

 