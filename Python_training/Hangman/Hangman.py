import random

def hangman():
    word = random.choice(["pug", "pokemon", "avenger", "himanshu", "earth"])
    validletters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''

    while len(word) > 0:
        main = ""

        for letter in word:
            if letter in guessmade:
                main = main + letter

            else:
                main = main + "_" + ""

        if main == word:
            print(main)
            print("win")
            break

        print("guess the word", main)
        guess = input()
        if guess in validletters:
            guessmade = guessmade + guess

        else:
            print("enter a valid char")
            guess = input()

        if guess not in word:
            turns = turns - 1

            if turns == 9:
                print("  --------  ")

            if turns == 8:
                print("  ---------  ")
                print("      0      ")

            if turns == 7:
                print("  ---------  ")
                print("      0      ")
                print("      |      ")

            if turns == 6:
                print("  ---------  ")
                print("      0      ")
                print("      |      ")
                print("     /       ")

            if turns == 5:
                print("  ---------  ")
                print("      0      ")
                print("      |      ")
                print("     / \     ")

            if turns == 4:
                print("  ---------  ")
                print("    \ 0      ")
                print("      |      ")
                print("     / \     ")

            if turns == 3:
                print("3 turns remaining")
                print("  ---------  ")
                print("    \ 0 /    ")
                print("      |      ")
                print("     / \     ")

            if turns == 2:
                print("2 turns remaining")
                print("  ---------  ")
                print("    \ 0|/    ")
                print("      |      ")
                print("     / \     ")

            if turns == 1:
                print("1 turn remaining")
                print("  ------|--  ")
                print("    \ 0_|   ")
                print("      |      ")
                print("     / \     ")

            if turns == 0:
                print("you are out of turns")
                print("  ------|--  ")
                print("      0_|    ")
                print("     /|\     ")
                print("     / \     ")
                print("The man is hanged")
                break


name = input("Enter your name")
print("Welcome", name)
print("try to guess the word in less than 10 attempts.")
hangman()
