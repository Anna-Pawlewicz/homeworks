patients = [[70, 1.8], [80, 1.9], [150, 1.7]]


def calculate_bmi(weight, height):
    return weight / (height ** 2)


for patient in patients:
    weight, height = patient
    bmi = calculate_bmi(weight, height)
    print(f"Patient\'s BMI is: {bmi}")

