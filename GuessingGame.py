from random import randint as rand


class GuessNumber:

    # Constructor for the game
    def __init__(self):
        self.min = 0
        self.max = 1
        self.goal = 0
        self.num_guesses = 0

        # Constants for difficulty settings
        self.SETTINGS = ('easy', 'medium', 'hard', 'custom')
        self.MAX_SETTINGS = {'easy': 10, 'medium': 50, 'hard': 100}

    # Sets the difficulty for the game between easy, medium, and hard
    def set_difficulty(self):
        pick = input(f'What difficulty would you like to play at? (Easy, Medium, Hard, Custom)\n').lower()

        # Uses player input to set difficulty based on constants already set
        if self.check_difficulty(pick):
            if pick == 'custom':
                self.custom_difficulty()
            else:
                self.max = self.MAX_SETTINGS[pick]
        else:
            print('Invalid input')
            self.set_difficulty()

        # Generates the random number inside of set parameters
        self.goal = rand(self.min, self.max)

    # Set custom difficulty parameters
    def custom_difficulty(self):
        print('Enter a custom minimum and maximum value for the game.')
        tMin = input('Minimum: ')
        tMax = input('Maximum: ')

        if self.check_custom(tMin, tMax):
            self.min = int(tMin)
            self.max = int(tMax)
        else:
            print('Invalid minimum and maximum inputs')
            self.custom_difficulty()

        # Takes in a guess from the user and calls the logic check for the number
    def get_guess(self):
        guess = input(f'Make a guess between {self.min} and {self.max} ')

        if self.check_guess(guess):
            return int(guess)
        else:
            print(f'Enter a valid number.')
            return self.get_guess()

    # Checks user difficulty input against preset settings
    def check_difficulty(self, pick):
        try:
            word = str(pick)
        except:
            return False

        for check in self.SETTINGS:
            if word == check:
                return True

        return False

    # Logic check for custom difficulty setting parameters submitted by user
    def check_custom(self, test_min, test_max):
        try:
            tMax = int(test_max)
            tMin = int(test_min)
        except:
            return False

        if tMin < 0:
            return False
        elif tMin > tMax:
            return False

        return True

    # Logic check for the user's guesses
    def check_guess(self, guess):
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
