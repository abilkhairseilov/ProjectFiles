# name = input('What is your name?\n> ')
# age = int(input('What is your age?\n> '))
#
# __import__('pprint').pprint(f"You've been alive for {age * 365} days, total {age * 365 * 24} hours, total {age * 365 * 24 * 60} minutes, {age * 365 * 24 * 60 * 60} seconds.")
# print(" Name:", name, "\n", "Days:", age * 365, "\n", "Hours:", age * 365 * 24, "\n", "Minutes:", age * 365 * 24 * 60, "\n", "Seconds:", age * 365 * 24 * 60 * 60)
while True:
  rating = int(input("How are you feeling today? Rate your mood from 0 to 10\n> "))
  if rating < 0 or rating > 10:
    print("Please input a proper value.")
    break
  elif rating <= 3:
    print("Dont be sad, life messes with everybody.")
    break
  elif rating <= 6:
    print("Atleast you didnt end up like that absolute donkeyfart dork who rated 3 out of 10.")
    break
  elif rating <= 10:
    print("Feeling fantastic today, ehh?")
    break