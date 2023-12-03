for i in range(1, 31):  # run the loop 31 times
    print(i * "$")  # print "$" multiplied by the current iteration number, which is {i}


for i in range(1, 100):
    print("Hello")
print("Bye")

for i in range(1, 100):
    print(i)

num = int(input("Enter a number to count to: "))
for i in range(1, num):
    print(i * i)

num = int(input("Enter a number to count to: "))
for i in range(1, num):
    print("i HATE turtles")

name = input("Enter your name: ")
num = int(input("Enter a number to count to: "))
for i in range(1, num):
    print(name)

num = int(input("Enter a number to count to: "))
for i in range(1, 5):
    print(f"{num} * {i} = {num * i}")

age = int(input("Enter your age: "))
name = input("Enter your name:")
for i in range(1, age):
    print(name)

for i in range(1, 7):
    num = int(input("Enter a number: "))
    print(num + 5)

name = input("Enter a name: ")
for i in range(1, len(name)):
    print(name)

negative = int(input("How many negatives did you get: "))
if negative == 1:
    for i in range(0, 10):
        print("Prompt")
elif negative == 2:
    for i in range(0, 50):
        print("Reminder")
elif negative == 3:
    for i in range(0, 100):
        print("Warning")
else:
    for i in range(0, 500):
        print("Removal")

yOrN = input("Is Wzzap market open? y/n: ")
if yOrN == "y":
    for i in range(0, 5):
        print("Can i get a face mask please")
else:
    for i in range(0, 100):
        print("I need to stay at home")

age = int(input("What is your age: "))
if age > 12 and age < 101:
    for i in range(0, 100):
        print("Happy Birthday!")
else:
    for i in range(0, 12):
        print("Happy Birthday")

for i in range(0, 99):
    if i % 2 != 0:
        print(i)

for i in range(0, 100):
    if i % 2 == 0:
        print(i)

