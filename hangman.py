from random import randint


def word_guess(num_of_guesses):

    if num_of_guesses == 6:
        print("""
            _________
            |       |
            |       0
            |
            |
            |
            |
            |
        _________
        Don't worry keep guessing
        """)

    elif num_of_guesses == 5:
        print("""
            _________
            |       |
            |       0
            |      |||
            |
            |
            |
            |
        _________
    
        Are you even trying?
        """)

    elif num_of_guesses == 4:
        print("""
            _________
            |       |
            |       0
            |      /|\
            |       |
            |
            |
            |
        _________
        What's up with your spelling?
        """)

    elif num_of_guesses == 3:
        print("""
         _________
            |       |
            |       0
            |     //|\\
            |       |
            |
            |
            |
        _________
        Come on mate!
        """)

    elif num_of_guesses == 2:
        print("""
            _________
            |       |
            |       0
            |     //|\\
            |       |
            |      /
            |
            |
            _________
        Come now!
        """)

    elif num_of_guesses == 1:
        print("""
            _________
            |       |
            |       0
            |     //|\\
            |       |
            |      / \
            |
            |
            _________
        Looks like you're going to die here!    
        """)

    elif num_of_guesses == 0:
        print("""
            _________
            |       |
            |       0
            |     //|\\
            |       |
            |     // \\
            |
            |
            _________
        You lose!
        """)

    print("You have {} guesses left.'".format(num_of_guesses))

wordlist = ("acres", "adult", "film", "canal", "breeze", "calm", "customs", "january",
            "habit", "grandmother", "garage", "kids", "label", "hunter", "mission", "monkey",
            "norway", "poetry", "pride", "recall", "palace", "skeleton", "shout", "slope",
            "thumb", "solar", "species", "silicon", "valley")

word = wordlist[randint(0, len(wordlist))]
wordlength = len(wordlist)

guesses = 7
letters = []
for letter in word:
    letters.append(letter)

print("""

Welcome to Hangman!
            _________
            |       |
            |       
            |
            |
            |
            |
            |
        _________
        """ +
      " -" * wordlength)

while True:
    guess = input("Guess a letter on the whole word:")

    if guess == word:
        print("Yay! You have won and saved my neck!")
        break

    else:
        for letter in letters:
            if letter in letters:
                continue

            else:
                guesses -= 1
            word_guess(guesses)

    if guess == 0:
        break