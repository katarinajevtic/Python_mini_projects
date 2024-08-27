def bmi_calculation(weight, height):
    return round(weight / (height ** 2), 2)


def bmi_category(bmi):
    if bmi <= 18.5:
        return "underweight"
    elif bmi <= 24.9:
        return "normal"
    elif bmi <= 29.9:
        return "overweight"
    else:
        return "obese"


def main():
    print("--BMI Calculator \n")
    while True:
        try:
            weight_input = float(input("Enter your weight in kg: "))
            height_input = float(input("Enter your height in m: "))

            bmi = bmi_calculation(weight_input, height_input)
            category = bmi_category(bmi)

            print(f"Your BMI is {bmi} which means your BMI is in the {category}")
        except ValueError:
            print("Please enter a valid number")

        another_entry = input("Do you want to calculate another BMI (y/n)?: ")
        if another_entry != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
