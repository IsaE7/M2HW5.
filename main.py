from decouple import Config, config
from logic import GuessNumberGame


def main():
    min_number = config('min_number', cast=int)
    max_number = config('max_number', cast=int)
    attempts = config('attempts', cast=int)
    initial_capital = config('initial_capital', cast=int)

    game = GuessNumberGame(min_number, max_number, attempts, initial_capital)

    print(
        f"Welcome to 'Guess the Number'! You have {attempts} attempts to guess the number between {min_number} and {max_number}.")
    print(f"Your initial capital is {initial_capital}.")

    while game.can_continue():
        try:
            bet_amount = int(input("Enter your bet amount: "))
            guessed_number = int(input(f"Guess the number between {min_number} and {max_number}: "))
            success, message = game.make_bet(bet_amount, guessed_number)
            print(message)
            print(f"Current capital: {game.current_capital}")
            print(f"Remaining attempts: {game.attempts}")
        except ValueError:
            print("Please enter valid numbers for the bet and guess.")

    print("Game over!")
    if game.current_capital > 0:
        print(f"You finished the game with {game.current_capital} capital.")
    else:
        print("You lost all your capital.")


if __name__ == "__main__":
    main()
