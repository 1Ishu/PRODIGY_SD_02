import random

def main():
    print("Guess the Number Game!")
    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {target_number} correctly.")
            print(f"It took you {attempts} attempts.")
            break

if __name__ == "__main__":
    main()
