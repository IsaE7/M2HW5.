import random

class GuessNumberGame:
    def __init__(self, min_number, max_number, attempts, initial_capital):
        self.min_number = min_number
        self.max_number = max_number
        self.attempts = attempts
        self.initial_capital = initial_capital
        self.secret_number = random.randint(self.min_number, self.max_number)
        self.current_capital = initial_capital

    def make_bet(self, bet_amount, guessed_number):
        if bet_amount > self.current_capital:
            return False, "Not enough capital to make this bet."

        self.attempts -= 1
        if guessed_number == self.secret_number:
            self.current_capital += bet_amount
            return True, f"Congratulations! You guessed the number {self.secret_number} and won {bet_amount}."
        else:
            self.current_capital -= bet_amount
            return False, f"Wrong guess! You lost {bet_amount}. The secret number was {self.secret_number}."

    def can_continue(self):
        return self.attempts > 0 and self.current_capital > 0
