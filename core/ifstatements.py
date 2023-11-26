# age = input('What is your age?\n> ')
# if age >= 18:
#     print("You are old enough to vote")
# else:
#     print("You are not old enough to vote.")

# name = input('What is your name?\n> ')
# if name == "Nina":
#     print("Hello Nina!")
# else:
#     print("Hello stranger")

# singer = input('Welcome user\nWho is your favorite singer?\n> ')
# if singer == "Beyonce":
#     print("Good singer (false)")
# elif singer == "Ed":
#     print("Meh")
# else:
#     print("Git gud")

# grade = int(input('What percentage did you get in your exam?\n> '))
# if grade >= 90:
#     print("Thats a Grade 9 / A**... good stuff")
# elif grade >= 80:
#     print("Thats a Grade 8 / A*... man you can get better next time")
# elif grade >= 70:
#     print("Thats a Grade 7 / A... thats pretty average")
# else:
#     print("Pass")

# lockdown = input("Is there a lockdown?\n> ")
# if lockdown == "no":
#     print("Have a nice day")
# else:
#     home = input("Are you at home?")
#     if home == "yes":
#         print("Well done, stay safe")
#     else:
#         print("Go home")

# num1 = int(input('Enter your first number\n> '))
# num2 = int(input('Enter your second number\n> '))
# confirmation = input('Would you like to multiply the numbers together?\n> ')
# if confirmation == "yes":
#     print(num1 * num2)
# else:
#     print("Ok boss")

# num = int(input('Enter a number\n> '))
# if num > 100:
#     print("Too large")
# else:
#     print("Too small")

# team = input('What is your favorite team\n> ')
# if team == "Chelsea":
#     print("Blue")
# elif team == "Liverpool":
#     print("Red")
# else:
#     print("Team not registered")

# num1 = int(input('Enter a number\n> '))
# num2 = int(input('Enter another number\n> '))
# if num1 > 10:
#     print(num1 + num2)
# else:
#     print(num1 * num2)

# ticket = input('Do you have the seasonal ticket? (y/n)\n> ')
# if ticket == "y":
#     print("Your final cost is $", 20 * 0.5)
# elif ticket == "n":
#     print("Your final cost is $", 20 * 0.75)

# colour = input("Enter a traffic light color (red, yellow, green)\n> ")
# if colour == "red":
#     print("Stop")
# elif colour == "yellow":
#     print("Get ready")
# elif colour == "green":
#     print("GO")
# else:
#     print("error")

num1 = int(input('Input number 1\n> '))
num2 = int(input('Input number 2\n> '))
operator = input('What do you wanna do? (add; multiply)\n> ')
if operator == "add":
    print(num1 + num2)
elif operator == "multiply":
    print(num1 * num2)
else:
    print("error")