# numbers = [3, 4, 7, 1, 4]
# new = 0
# for i in range(0, len(numbers)):
#     print(f"i = {i}")
#     num = numbers[i]
#     if num > 3:
#         new = new + num
#     else:
#         new = new - num
#     print(f"New = {new}")
# print(new)

array = ["N/A", "Pink", "Queen", "N/A", "Beatles"]
for i in range(0, len(array)):
    band = array[i]
    if band == "N/A":
        name = input("Enter a band name")
        print(name)
    else:
        print(band)

names = ["Ted", "Arin", "Mark", "Son", "Jim", "Lily"]
for i in range(0, len(names)):
    guess = input('Enter a name')
    if guess in names:
        print(f"{guess} is found on index {names.index(guess)}")
        break
    else:
        print("Not Found")
        pass

numbers = [5,2,78,8,2,5,9,4,22,66,11,88,77,38,266,12,1]
lowest = 1000
highest = 0
total = 0
average = 0

for i in range(0, len(numbers)):
    current = numbers[i]
    if current < lowest:
        lowest = current
    if current > highest:
        highest = current
    total += current
average = total / len(numbers)

print(f"The highest is {highest}\nThe lowest is {lowest}\nThe total is {total}\n The average is {average}")

pets = ["Cat", "Dog", "Cat", "Cat", "Cat", "Cat", "Dog"]
cats = 0
dogs = 0
for i in range(0, len(pets)):
    if pets[i] == "Cat":
        cats += 1
    elif pets[i] == "Dog":
        dogs += 1

print(f"Cats got total {cats} votes")
print(f"Dogs got total {dogs} votes")
print(f"Total votes: {cats + dogs}")