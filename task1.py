import random

# Predefined list of words
word_list = ["python", "hangman", "programming", "algorithm", "computer", "game", "openai", "random"]

# Function to select a random word from the list
def select_random_word(word_list):
    return random.choice(word_list)

# Function to display the current state of the word with guessed letters
def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

# Function to check if the word is fully guessed
def is_word_guessed(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

# Main game function
def hangman_game():
    word = select_random_word(word_list)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    
    print("Welcome to Hangman!")
    print("You have", max_incorrect_guesses, "incorrect guesses allowed.")
    print(display_word(word, guessed_letters))
    
    while incorrect_guesses < max_incorrect_guesses and not is_word_guessed(word, guessed_letters):
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            guessed_letters.add(guess)
            incorrect_guesses += 1
            print("Incorrect guess. You have", max_incorrect_guesses - incorrect_guesses, "guesses left.")
        
        print(display_word(word, guessed_letters))
    
    if is_word_guessed(word, guessed_letters):
        print("Congratulations! You guessed the word:", word)
    else:
        print("Game over! The word was:", word)

# Run the game
hangman_game()
