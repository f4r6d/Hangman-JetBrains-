from string import ascii_lowercase
import random
print("H A N G M A N")
while True:
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu == "play":    
        print()
        word_list = ['python', 'java', 'kotlin', 'javascript']
        lives = 8
        random.seed()
        random_word = random.choice(word_list)
        random_word_list = list(random_word)
        random_word_length = len(random_word)
        random_word_chklist = ["-"] * random_word_length
        correct_answer_set = set()
        all_answer_set = set()
        while lives > 0:
            print(''.join(random_word_chklist))
            letter = input("Input a letter: ")
            if letter in all_answer_set:
                print("You already typed this letter")
            if letter not in ascii_lowercase:
                print("It is not an ASCII lowercase letter")
            if len(letter) != 1:
                print("You should input a single letter")
            for i in range(random_word_length):
                if letter == random_word_list[i]:
                    random_word_chklist[i] = letter
                    correct_answer_set.add(letter)
            if letter not in random_word_chklist:
                if (letter in ascii_lowercase) and (len(letter) == 1) and (letter not in all_answer_set):
                    print("No such letter in the word")
                    lives -= 1
            all_answer_set.add(letter)
            if lives > 0:
                print()  
            if random_word_chklist == random_word_list:
                break                 
        if random_word_chklist == random_word_list:
            print(''.join(random_word_chklist))
            print("You guessed the word!")
            print("You survived!")
        else:
            print("You are hanged!")
    elif menu == "exit":
        break
