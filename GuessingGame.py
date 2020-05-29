from random import randint as rand


class GuessNumber:

    # Constructor for the game
    def __init__(self):
        self.min = 0
        self.max = 1
        self.goal = 0
        self.num_guesses = 0

        # Constants for difficulty settings
        self.EASY_DIFFICULTY = 10
        self.MEDIUM_DIFFICULTY = 50
        self.HARD_DIFFICULTY = 100

    # Sets the difficulty for the game between easy, medium, and hard
    def set_difficulty(self):
        pick = input(f'What difficulty would you like to play at? (Easy, Medium, Hard)\n').lower()

        # Uses player input to set difficulty based on constants already set
        if self.check_difficulty(pick):
            if pick == 'easy':
                self.max = self.EASY_DIFFICULTY
            elif pick == 'medium':
                self.max = self.MEDIUM_DIFFICULTY
            elif pick == 'hard':
                self.max = self.HARD_DIFFICULTY
        else:
            print('Invalid input')
            self.set_difficulty()

        # Generates the random number inside of set parameters
        self.goal = rand(self.min, self.max)

    # Checks the word if it is correct or not
    def check_difficulty(self, pick):
        try:
            word = str(pick)
        except:
            return False

        return pick == 'easy' or pick == 'medium' or pick == 'hard'

    # Takes in a guess from the user and calls the logic check for the number
    def get_guess(self):
        guess = input(f'Make a guess between {self.min} and {self.max} ')

        if self.check_number(guess):
            return int(guess)
        else:
            print(f'Enter a valid number.')
            return self.get_guess()

    # Logic check for the user's guesses
    def check_number(self, guess):
        try:
            number = int(guess)
        except:
            return False

        return self.min <= number <= self.max

    # The main method for the game
    def play(self):
        self.set_difficulty()

        while True:
            self.num_guesses += 1

            guess = self.get_guess()

            if guess < self.goal:
                print('Your guess was under')
            elif guess > self.goal:
                print('Your guess was above')
            else:
                print(f'You found the number in: {self.num_guesses} attempts. Great Job!')
                break


game = GuessNumber()
game.play()
