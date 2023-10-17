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


charges = {
  "pic": 0.35,
  "text": 0.10,
  "data": 2.50
}

pics = int(input('How many pictures are you going to upload?\n> '))
texts = int(input('How many text messages are you going to send?\n> '))
datas = int(input('How many megabytes of data are you going to use?\n> '))

print(f"For pictures we will be charging you ${round(charges['pic'] * pics, 2)} \nFor texts ${round(charges['text'] * texts, 2)} \nFor your data usage we will be charging ${round(charges['data'] * (datas / 500), 2)}.")