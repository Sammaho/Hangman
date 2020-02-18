import random

def hangman(word):
    wrong = 0
    stages = ["",
              "__________  ",
              "     |      ",
              "     0      ",
              "    /|\     ",
              "     |      ",
              "    / \      ",
              "    / \      "
              ]
    remaining_letters = list(word)
    remaining_letters_lower_case = list(word.lower())
    board = ["_"] * len(word)
    win = False
    print("Welcom to Hangman")

    char = " "
    spaces = True
    while spaces == True:
        if char in remaining_letters:
            cind = remaining_letters.index(char)
            board[cind] = char
            remaining_letters[cind] = "$"
        else:
            spaces = False
    
    
    
    while wrong < len(stages) - 1:
        print("\n".join(stages[0: wrong]));
        print("");
        print((" ".join(board)));
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char.lower() in remaining_letters_lower_case:
            try:
                cind = remaining_letters.index(char)
                board[cind] = char
                remaining_letters[cind] = "$"
            except ValueError:
                cind = remaining_letters.index(char.upper())
                board[cind] = char.upper()
                remaining_letters[cind] = "$"

        else:
            wrong +=1
            e = wrong + 1
            if "_" not in board:
                print("You win!");
                win = True
                break
    if not win:
        print("\n".join(stages[0: wrong]));
        print("");
        print("You lose! It was '{}'".format(word));

hangmanList = ["Cowboy", "Play Ball", "Hide and Seek", "Airplane", "Taxi", "Dog"]
word = hangmanList[random.randint(0,len(hangmanList)-1)]
#another random way below
#word = random.choice(["cat", "apple", "monkey", "horse", "blue", "yellow"])
hangman(word)


        
              
