import random


# num1 = random.randint(1, 100)
# print(num1)
# num2 = int(input("Enter a number: "))
# print((num1 + num2))
#
# while True:
#     tryagain = input("Would you like to see the random number? y/n\n> ")
#     if tryagain == "y":
#         print(random.randint(1, 1000))
#     else:
#         print("Buh bye!")
#         break
# score = 0
# while True:
#     num1 = random.randint(1, 5)
#     usernum1 = int(input("Guess the number\n> "))
#     if num1 == usernum1:
#         print("Correct")
#         score += 1
#     else:
#         print("Incorrect")
#     tryagain = input("Would you like to try again?")
#     if tryagain == "n":
#         print(score)
#         break

# for i in range(1, 10):
#     print(f"{random.randint(1, 100)}\n{random.randint(1,100)%2==0}")

# for i in range(0, 5):
#     rannum1 = random.randint(0, 10)
#     rannum2 = random.randint(0, 10)
#     answer = input(f"{rannum1} * {rannum2} = ")
#     if rannum1 * rannum2 == answer:
#         print("Correct")

currentHigh = 0
currentLow = 1000
for i in range(0, 6):
    rannum = random.randint(0, 1000)
    print(rannum)
    if rannum > currentHigh:
        currentHigh = rannum
    if rannum < currentLow:
        currentLow = rannum
print(f"The highest number is {currentHigh}")
print(f"The lowest number is {currentLow}")

rannum = random.randint(0, 100)
while True:
    guess = int(input("Guess the number: "))
    if guess > rannum:
        print("Too High")
    elif guess < rannum:
        print("Too Low")
    elif guess == rannum:
        print("Correct")
        break
