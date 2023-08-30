import random
import sys

HANGMAN_PICS = [r"""
 +--+
 |  |
    |
    |
    |
    |
=====""",
                r"""
 +--+
 |  |
 O  |
    |
    |
    |
=====""",
                r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====""",
                r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====""",
                r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====""",
                r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
=====""",
                r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
====="""]

CATEGORY = 'Animals'
WORDS = 'ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE HAWK LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PARROT PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE WOLF WOMBAT ZEBRA'.split()


class HangmanGame:
    def __init__(self):
        self.missed_letters = []
        self.correct_letters = []
        self.secret_word = random.choice(WORDS)

    def run(self):
        print('Hangman, by Al Sweigart al@inventwithpython.com')

        while True:
            self.draw_hangman()
            guess = self.get_player_guess(self.missed_letters + self.correct_letters)

            if guess in self.secret_word:
                self.correct_letters.append(guess)
                if self.found_all_letters():
                    self.handle_win()
                    break
            else:
                self.missed_letters.append(guess)
                if self.lost_game():
                    self.handle_loss()
                    break

    def draw_hangman(self):
        print(HANGMAN_PICS[len(self.missed_letters)])
        print(f'The category is: {CATEGORY}\n')
        print('Missed letters:', ' '.join(self.missed_letters) if self.missed_letters else 'No missed letters yet.')
        blanks = [letter if letter in self.correct_letters else '_' for letter in self.secret_word]
        print(' '.join(blanks))

    def get_player_guess(self, already_guessed):
        while True:
            print('Guess a letter.')
            guess = input('> ').upper()
            if len(guess) != 1:
                print('Please enter a single letter.')
            elif guess in already_guessed:
                print('You have already guessed that letter. Choose again.')
            elif not guess.isalpha():
                print('Please enter a LETTER.')
            else:
                return guess

    def found_all_letters(self):
        return all(letter in self.correct_letters for letter in self.secret_word)

    def lost_game(self):
        return len(self.missed_letters) == len(HANGMAN_PICS) - 1

    def handle_win(self):
        print(f'Yes! The secret word is: {self.secret_word}')
        print('You have won!')

    def handle_loss(self):
        self.draw_hangman()
        print(f'You have run out of guesses!\nThe word was "{self.secret_word}"')


if __name__ == '__main__':
    try:
        hangman_game = HangmanGame()
        hangman_game.run()
    except KeyboardInterrupt:
        sys.exit()
