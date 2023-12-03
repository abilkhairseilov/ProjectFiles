films = ["The Mario Movie", "Garfield Movie", "Despicable Me"]
print(films)
print(films[0])
print(films[len(films) - 1])

numbers = [1, 2, 3, 4, 5]
print(numbers[2])

singers = ["Rihanna", "Katy", "Adele", "Ed"]
print(singers[0])
print(singers[0:3])
print(singers[len(singers) - 1])

game = ["Overwatch", "Counter-Strike 2", "FIFA", "Fortnite"]
for i in range(1, len(game)):
    print(game[i - 1])

numbers = [2, 3, 4, 5, 6, 7, 90]
while True:
    guess = int(input("Guess the number"))
    if guess in numbers:
        print("Correct")
    else:
        print("Try again")
