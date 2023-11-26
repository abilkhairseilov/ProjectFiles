# choice = input("Would you like to convert to Celsius or Fahrenheit?\n> ")
# if choice == "Celsius":
#     print((int(input("Enter a temperature in Fahrenheit\n> ")) * 9 / 5) + 32)
# if choice == "Fahrenheit":
#     print(((int(input("Enter a temperature in Celsius\n> "))) - 32) * 5 / 9)
# 
# 
# 
# gamename = input("what is your favorite game?\n> ")
# if gamename == "Guild Wars":
#     print("Old but good!")
# else:
#     gameyear = int(input("What year was it released?\n> "))
#     if year > 2010:
#         print("Decent!")
#     else:
#         print("Good old games...")

# miles = int(input("How many miles do you have to drive?\n> "))
# hasMembershipCard = input("Do you have a membership card?\n> ")
# price = 0
# if hasMembershipCard == "yes":
#     price = 2 + ((miles - 1) * 0.25)
# else:
#     price = 2 + ((miles - 1) * 0.25) + 5
# dieselCost = miles * 0.5
# totalCost = price + dieselCost
# print(f"Your total cost is ${totalCost}")

number = int(input("Enter a number\n> "))
if number > 90:
    print("A*")
else:
    if number > 80:
        print("A")
    else:
        print("Pass")
