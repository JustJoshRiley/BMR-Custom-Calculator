#BMR Calculator
#description
print("This Calculator Will Help Determine Your Basal Metabolic Rate (BMR)")

#ask the users gender
gender = ' '
while gender not in 'mMfF' or gender == ' ':
    gender = input("Are you M or F? ")
    #
    #print(gender)
if gender == 'f' or 'F':
    #ask for female details
    female_weight = (input("Enter your Weight in LBS: "))
    female_weight = float(female_weight)
    #ask for female height
    female_height = (input("Enter your Height in Inches: "))
    female_height = float(female_height)
    #ask for female age
    female_age = int(input("Please enter your age in years"))
    female_age = float(female_age)
    #calculate BMR based on female answer
    calculate = ' '
    while calculate not in 'YyNn' or calculate == ' ':
        calculate = input("Do you want to Calculate your BMR? Y/N: ")
        if calculate == 'y' or 'Y':
            fbr = (655 + (4.35 * female_weight) + (4.7 * female_height) + (4.7 * female_age))
            print(f"Here is your BMR: {fbr}")
        else :
            print({calculate})


