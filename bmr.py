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
else :
    #ask for male weight
    male_weight = (input("Enter your Weight in LBS: "))
    male_weight = float(male_weight)
    #ask male age
    male_height = (input("Enter your Height in Inches: "))
    male_height = float(male_height)
    #ask male age
    male_age = (input("Enter you Age: "))
    male_age = float(male_age)
    #calculate BMR based on male answer
    calculate = 'a'
    if calculate not in 'YyNn':
        calculate = input("Do you want to Calculate your BMR? Y/N: ")
        if calculate == 'y' or 'Y':
            fbr = (66 + (6.2 * male_weight) + (12.7 * male_height) + (6.76 * male_age))
            print(f"Here is your BRM: {fbr}")

