import os
import random
import time

import english_words as eng_words


def choose_word(length: int) -> str:
    long_list = [x for x in list(eng_words.english_words_lower_set) if len(x) >= length]
    return random.choice(long_list)


class Logic:

    def __init__(self, param: int):
        self.word = choose_word(param)
        self.word_list = [x for x in self.word]
        self.used_letters = []
        self.tries = 0
        self.progress_list = ['_'] * len(self.word)

    def input_loop(self):
        while True:

            self.display_info()
            guess = input("Enter Guess: ").lower()

            os.system('cls')

            if len(guess) > 1 or len(guess) <= 0:
                print("Invalid input!")
                time.sleep(2)
                os.system('cls')
                self.input_loop()

            self.letter_in_word(guess)

            if self.tries <= 0:
                print(f"You lose, ran out of guesses. :(\nWord was {self.word}")
                input()
                break

    def letter_in_word(self, guess):  # checks if letter is in hidden word
        os.system('cls')

        if guess.upper() in self.used_letters:  # checks if guesses letter has already been used
            return "Letter already used."

        if "_" not in self.progress_list:  # check if all letters in word have been found
            print("Word found! :)")

        if guess in self.word_list:
            for i, letter in enumerate(self.word_list):  # if letter is in word enumerate through each word in letter
                if letter == guess:
                    self.progress_list[i] = self.word_list[i]
                    self.used_letters.append(guess.upper())
            self.display_info()
            return True
        else:
            self.used_letters.append(guess.upper())
            self.tries += 1
            self.display_info()
            return False

    def display_info(self):  # Only for console version
        #  print(f"Word: {self.word}")
        print(f"Remaining tries: {6-self.tries}")
        print(f"Total word length: {len(self.word)}")
        print(f"Progress: {' '.join(self.progress_list)} ")
        print(f"Used letters: {' '.join(self.used_letters)}")


if __name__ == '__main__':
    game = Logic(4)
