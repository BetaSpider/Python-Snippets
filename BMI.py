


#BMI=Weight/height**2

Weight=float(input("Enter ur weight in pounds!"))
height=float(input("enter ur height in inches!"))

weight_in_kg=Weight*0.45359237
height_in_meter=height*0.0254

BMI=weight_in_kg/height_in_meter**2
print("BODY MASS INDEX: (BMI)for the given height & weight is:\n", BMI)


