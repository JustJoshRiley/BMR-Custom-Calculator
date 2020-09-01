#BMR Calculator
#description
print("This Calculator Will Help Determine Your Basal Metabolic Rate (BMR). A low BMR means you have to eat less calories in order to lose body fat and weight. The Metabolic age is calculated by comparing your Basal Metabolic Rate to the average BMR of your chronological age group. If your metabolic age is higher than your actual age, it's an sign that you need to improve your metabolic rate.")

#made the bmr calculator into a function so that it can call itself to start over
def calculate_bmr():
    #ask the users gender
    gender = input("Are you M or F? ")

    #print(gender)
    if gender == "F" or gender == "f":
        #ask for female details
        female_weight = (input("Enter your Weight in LBS: "))
        female_weight = float(female_weight)
        #ask for female height
        female_height = (input("Enter your Height in Inches: "))
        female_height = float(female_height)
        #ask for female age
        female_age = int(input("Please enter your age in years: "))
        female_age = float(female_age)
        #calculate BMR based on female answer
        calculate = ' '
        calculate = input("Do you want to Calculate your BMR? Y/N: ")
        if calculate == 'y' or calculate == 'Y':
            #fbr is the BMR calculation based on the answers provided by the female
            fbr = (655 + (4.35 * female_weight) + (4.7 * female_height) + (4.7 * female_age))
            print(f"Here is your BMR: {fbr}")
        else:
            print("Try Again Later")
            calculate_bmr()

    elif gender == "M" or gender == "m":
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
        calculate = ' '
        calculate = input("Do you want to Calculate your BMR? Y/N: ")
        if calculate == 'y' or calculate == 'Y':
            fbrm = (66 + (6.2 * male_weight) + (12.7 * male_height) + (6.76 * male_age))
            print(f"Here is your BRM: {fbrm}")
        else:
            print("Try Again Later")
            calculate_bmr()
    else:  
        print("Try Again Later")

calculate_bmr()