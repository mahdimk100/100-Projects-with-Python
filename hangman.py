import random

def play_hangman():
    words = ['python', 'java', 'javascript', 'ruby', 'php']
    word = random.choice(words)
    guessed_letters = []
    max_attempts = 6
    attempts = 0
    done = False
    
    while not done:
        print('\n' + '-' * len(word))
        for letter in word:
            if letter in guessed_letters:
                print(letter, end="")
            else:
                print("-", end="")
            print("\n")
            
            guess = input('Guess a letter: ')
            if guess in guessed_letters:
                print('You already guessed that letter!')
            elif guess in word:
                print('Correct!')
                guessed_letters.append(guess)
            else:
                print('Incorrect!')
                attempts += 1
                guessed_letters.append(guess)
                
            if attempts >= max_attempts:
                done = True
                print('You lost! The word was', word)
            elif set(word) == set(guessed_letters):
                done = True
                print('You won! The word was', word)

play_hangman()