from nltk.corpus import words
import random

word_list = [x.lower() for x in words.words() if len(x) == 5]

def apply_feedback(words, tried_word, feedback):
    # feedback: list with 5 items: 0 miss, 1 incorrect place, 2 good
    new_words = words.copy()
    for let in set(tried_word):
        pos = [i for i in range(5) if tried_word[i]==let]
        let_feedback = [set([i for i in pos if feedback[i]==n]) for n in range(3)]
        min_let = len(let_feedback[1].union(let_feedback[2]))
        new_words = [y for y in new_words if y.count(let) >= min_let \
                     and let_feedback[2].issubset(set([i for i in range(5) if y[i]==let])) \
                     and (let_feedback[0].union(let_feedback[1])).intersection(set([i for i in range(5) if y[i]==let])) == set()]
        if let_feedback[0]:
            new_words = [y for y in new_words if y.count(let) == min_let]            
    return new_words

def play_game(word_list):
    print("Welcome to the Wordle assistant.")
    print("The assistant will present a list of five suggestions and print the number of possible words.")
    print("The player has to enter the receveid feedback as a sequence of 5 digits: 0 if grey, 1 if yellow, 2 if green.")
    turn = 0
    while turn < 6:
        print("There are " + str(len(word_list)) + " words remaining.")
        suggestions = random.choices(word_list, k=min(5, len(word_list)))
        print("The suggested words are:")
        for word in suggestions:
            print(word)
        tried_word = input("Enter the word you tried:")
        feedback = input("Enter the feedback received:")
        feedback = [int(x) for x in feedback]
        word_list = apply_feedback(word_list, tried_word, feedback)
        if set(feedback) == {2}:
            print("Congratulations! You win!")
            break
        turn += 1
    if turn == 6:
        print("Sorry, you have lost. :(")
    
play_game(word_list)        