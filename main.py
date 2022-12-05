import random
print("H A N G M A N")
wins = 0
loses = 0
while True:
    menu = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if menu == "results":
        print("You won: {0} times.\nYou lost: {1} times".format(wins, loses))
    elif menu == "play":
        words = ("python", "java", "swift", "javascript")
        word = random.choice(words)
        word_list = list("-" * len(word))
        a = 8
        done = list()
        print("".join(word_list))
        while a != 0:
            print("".join(word_list))
            letter = input("Input a letter:")
            if len(letter) != 1:
                print("Please, input a single letter.")
            elif letter.islower() == False:
                print("Please, enter a lowercase letter from the English alphabet.")
            else:
                if letter in done:
                    print("You've already guessed this letter.")
                elif letter in word:
                    for i in range(0, len(word)):
                        if letter == word[i]:
                            word_list[i] = letter
                else:
                    print("That letter doesn't appear in the word.")
                    a = a - 1
                if "-" not in word_list:
                    break
            done.append(letter)
        if a == 0:
            loses += 1
            print("You lost!")
        else:
            wins += 1
            print("You guessed the word {0}!\nYou survived!".format(word))
    elif menu == "exit":
        break
