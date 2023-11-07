choice = input("Would you like to convert to Celsius or Fahrenheit?\n> ")
if choice == "Celsius":
    print((int(input("Enter a temperature in Fahrenheit\n> ")) * 9 / 5) + 32)
if choice == "Fahrenheit":
    print(((int(input("Enter a temperature in Celsius\n> "))) - 32) * 5 / 9)
