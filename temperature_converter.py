temperature = float(input("Enter the temperature: "))
unit = input("Celsius or Farenheit? (C/F): ")

if unit == 'C':
    temperature=round((9*temperature)/5+32,1)
    unit = "F"
elif unit == 'F':
    temperature=round((temperature-32)*5/9,1)
    unit = "C"
else:
    print("Invalid unit!")
    exit()

print(f"The temperature is {round(temperature, 1)} {unit}")
