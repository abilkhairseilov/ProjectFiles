# name = input('Enter name\n> ')
# password = input('Enter password\n> ')
# if name == "RushB" and password == "CSGO":
    # print("Go go go!")
# else:
    # print("Incorrect details")

# pc = input("Do you play games on a PC?\n> ")
# console = input("Do you play games on a console?\n> ")

# if pc == "yes" and console == "no":
    # print("PC master race")
# elif pc == "yes" and console == "yes":
    # print("Gamer, go outside")
# elif pc == "no" and console == "yes":
    # print("Console gamer")
# else:
    # print("Wrong option")
# age = int(input("Enter your age\n> "))
# if age > 12 and age < 20:
    # print("You are a teenager")
# elif age == 11 or age == 12:
    # print("You are a tween")
# else:
    # print("Invalid age")

# temp = int(input("Enter a temperature outside\n> "))
# rain = input("Is it raining outside?\n> ")
# if temp < 12 and rain == "yes":
#     print("Wear a coat and bring an umbrella")
# elif temp < 12 and rain == "no":
#     print("Wear a coat")
# elif temp >= 12 and rain == "yes":
#     print("Bring an umbrella")
# else:
#     print("You don't need a coat or an umbrella")

# temp = int(input("Enter a temperature outside\n> "))
# if temp > 28:
#     print("TShirt Weather")
# elif temp >= 18 and temp <= 28:
#     print("Lovely Weather")
# else:
#     print("Its cold")

# data = int(input("Enter a number\n> "))
# unit = input("What unit is the number in? (bit, byte, kilobyte)\n> ")
# wish_unit = input("What unit do you wanna convert to? (bit, byte, kilobyte)\n> ")
# match unit:
#     case "bit":
#         match wish_unit:
#             case "bit":
#                 print("The data is already in bits")
#             case "byte":
#                 print(data / 8)
#             case "kilobyte":
#                 print((data / 8) / 1000)
#             case _:
#                 print("Error")
#     case "byte":
#         match wish_unit:
#             case "bit":
#                 print(data * 8)
#             case "byte":
#                 print("The data is already in bytes")
#             case "kilobyte":
#                 print(data / 1000)
#             case _:
#                 print("Error")
#     case "kilobyte":
#         match wish_unit:
#             case "bit":
#                 print(data * 1000 * 8)
#             case "byte":
#                 print(data * 1000)
#             case "kilobyte":
#                 print("The data is already in kilobytes")
#             case _:
#                 print("Error")
#     case _:
#         print("Error")


exec("""\ndata = int(input("Enter a number\\n> "))\nunit = input("What unit is the number in? (bit, byte, kilobyte)\\n> ")\nwish_unit = input("What unit do you wanna convert to? (bit, byte, kilobyte)\\n> ")\nmatch unit:\n    case "bit":\n        match wish_unit:\n            case "bit":\n                print("The data is already in bits")\n            case "byte":\n                print(data / 8)\n            case "kilobyte":\n                print((data / 8) / 1000)\n            case _:\n                print("Error")\n    case "byte":\n        match wish_unit:\n            case "bit":\n                print(data * 8)\n            case "byte":\n                print("The data is already in bytes")\n            case "kilobyte":\n                print(data / 1000)\n            case _:\n                print("Error")\n    case "kilobyte":\n        match wish_unit:\n            case "bit":\n                print(data * 1000 * 8)\n            case "byte":\n                print(data * 1000)\n            case "kilobyte":\n                print("The data is already in kilobytes")\n            case _:\n                print("Error")\n    case _:\n        print("Error")\n""")
