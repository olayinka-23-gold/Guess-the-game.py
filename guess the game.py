import random

while True:
    guess = random.randint(1, 10)
    user = int(input("Enter a number and know if it is the guess number: "))

    if user == guess:
        print(f"The number {user} you inputted is the same as the guess number {guess}")
        print("Congratulations")
    elif user < guess:
        print(f"The number {user} is lower than the guess number {guess}. Try again!!")
    elif user > guess:
        print(f"The number {user} is higher than the guess number {guess}. Try again!!")
    
    check_again = input("Do you wish to try again?:(y/n) ").lower().strip()
    if check_again[0] == 'n':
        break
