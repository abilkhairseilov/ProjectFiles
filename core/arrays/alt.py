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
