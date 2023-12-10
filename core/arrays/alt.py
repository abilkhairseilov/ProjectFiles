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

#names = ["Ted", "Arin", "Mark", "Son", "Jim", "Lily"]
#i = 0
#while True:
#    guess = input('Enter a name')
#    current = names[i]
#    if guess == current:
#        print(f"{Guess} is found on index {i}")
#        break
#    else:
#        print("Not Found")
#        pass
#    i += 1

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
