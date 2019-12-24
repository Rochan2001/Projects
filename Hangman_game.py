from os import system, name 
def clear():  
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 
class Hangman:
    word = input("Enter the word you want the person to guess: ")
    @classmethod
    def secret(cls):
        return cls.word
class game(Hangman):
    turns = 10
    def play(self):
        secret_word = Hangman.secret()
        clear()
        guesses = ''
        while game.turns > 0:
            failed = 0
            for char in secret_word:
                if char in guesses:
                    print(char,end=' ')
                else:
                    print("_ ",end='')
                    failed += 1
            if failed==0:
                print("\nYou won")
                break
            guess=input("\nGuess a character :")
            guesses+=guess
            if guess not in secret_word:
                game.turns-=1
                print("Wrong"+" You have {} chances left".format(game.turns))
            if game.turns == 0:
                print("You loose")


play_game = game()
play_game.play()

