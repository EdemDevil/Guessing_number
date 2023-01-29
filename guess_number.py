import random as r


dif = {
    'easy': 10,
    'hard': 5,
}
lifes = []
print("Welcome to the Number Guessing Game!\nI`m thinking of a number between 1 and 100.")
choice = input("Choose a difficulty. Type 'hard' or 'easy': ").lower()


def random_number():
    """Return a random number between 0 and 100"""
    return r.randint(0, 101)


def choose_difficult(life):
    """Returns the number of lives relative to the selected difficulty"""
    if choice == 'easy':
        life = dif['easy']
    if choice == 'hard':
        life = dif['hard']
    return lifes.append(life)


def hot_cold():
    """Returns how close the guess is to the hidden number"""
    if user_choice == rand:
        return "WIN"
    elif user_choice > rand:
        return "Too high"
    elif user_choice < rand:
        return "Too low"


def count_life():
    """Returns a count of the remaining lives for each failed attempt"""
    if hot_cold() == "Too high" or "Too low":
        lifes[0] -= 1
        print(f"You have left {lifes[0]} lifes")
        if lifes[0] == 0:
            return "LOSE"
    if hot_cold() == "WIN":
        return "YOU WIN"


rand = random_number()
while lifes != 0:
    user_choice = int(input("Type a guess number: "))
    choose_difficult(life=lifes)
    count = count_life()
    hot_cold()
    print(f"{hot_cold()}")
    if count == "LOSE":
        print(count)
        break
    if count == "YOU WIN":
        print(f"The answer was {rand}")
        break

