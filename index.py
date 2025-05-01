# Hangman Game in Python

import random



# List of words to choose from
words = ['python', 'typescript', 'language', 'javascript', 'swift', 'iphone', 'programming', 'computer', 'Colab', 'artificial']

# Randomly select a word from the list
word = random.choice(words)

# Initialize the game state
guessed_letters = []
attempts = 6

print("Welcome to the Hangman Game!")
print("_ " * len(word))

while attempts > 0:
    guess = input("\n guess the letters : ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Write one alphabet only!")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    guessed_letters. append(guess)
    if guess in word:
        print("correct guess!")
    else:
        attempts -= 1
        print("Incorrect guess!")
        print("You have", attempts, "attempts.")

        displayed_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
        print(displayed_word)

        if "_" not in displayed_word:
            print(f"Congratulations! You won! the correct word is: {word}")
            break

        else:
            print(f"Game Over! the correct word is : {word}")