from random import randint


def play(target, limit=10):
    for attempt in range(1, limit + 1):
        while True:
            try:
                guess = int(input("Guess a number from 1 to 100: "))
            except EOFError:
                print("\nGame ended.")
                return
            except ValueError:
                print("Enter a whole number.")
                continue
            if 1 <= guess <= 100:
                break
            print("That guess is outside the range.")

        if guess == target:
            print(f"Correct! Guesses used: {attempt}.")
            return
        print("Too low." if guess < target else "Too high.")

    print(f"No guesses left. The number was {target}.")


if __name__ == "__main__":
    play(randint(1, 100))
