def calculate_bmi(weight, height):
    return round(weight/(height**2),2)

print(calculate_bmi(70,1.75))
print(calculate_bmi(60,1.88))
