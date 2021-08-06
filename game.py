from images import IMAGES
import random, string

def hangman(words_list):
        random_word = random.choice(words_list)
        hidden_word = random_word
        guesses = 7
        answer = ''
        letter_options = list(string.ascii_lowercase)
        blank_spaces = ("-" * len(hidden_word))
        list2 = list(blank_spaces)
        position_list = []
        message = '''You can't guess the same letter twice.'''
        print("")
        print("Welcome to Hangman!")
        print("I am thinking of a letter that is " + str(len(hidden_word)) + " letters long.")
        print(blank_spaces)

        while guesses > 0:
            print("")
            print("You have " + str(guesses) + " chances to guess the correct word")
            print("Avaliable letters to guess:- ")
            print(letter_options)

            try:
                    guess = input("Guess a letter: ")
                    if len(guess) == 1:
                            position_list = []
                            if guess in hidden_word:
                                    list1 = list(hidden_word)
                                    counter = 0
                                    while counter < len(list1):
                                            if list1[counter] == guess:
                                                    if counter not in position_list:
                                                            position_list.append(counter)
                                                    else:
                                                            position_list.append(counter)
                                            else: 
                                                    pass 
                                            counter += 1

                                    for numbers in position_list:
					                        list2[numbers] = guess.upper()
					                        answer = "".join(list2)
					print(answer) 

					                letter_options.remove(guess)
                            else: 
                                    print("Incorrect Guess")
                                    print(IMAGES[8 - guesses])
                                    if guesses == 1:
                                            print("You lost the game")
                                            print("The correct word is " + hidden_word)
                                            print("")
                                    chances -=1
                            if answer.lower() == hidden_word:
                                            print("You win!")
                                            print("")
                                            break
                    else:
                            print("Please enter one letter at a time")
            except:
                    print("")
                    print(message)

        again = restart()
        print(again)


def restart():
	restart = input("Do you wnat to play again(y/n): ").lower()
	if restart == "y":
		return hangman(words)
	else:
		return "Thanks for playing"


words = ['yellow', 'orange', 'blue', 'red', 'green', 'purple', 'brown', 'black', 'white', 'circle', 'rectangle', 'square', 'triangle', 'octagon', 'hexagon', 'pentagon',
'oval', 'dog', 'cat', 'bird', 'elephant', 'lion', 'giraffe', 'zebra', 'monkey', 'flamingo', 'gorilla', 'fish', 'deer', 'elk', 'moose', 'buffalo', 'bison', 'turtle', 'alligator',
'crocodile', 'meercat', 'penguin', 'antelope', 'seagull', 'cardinal', 'robin', 'beaver', 'pigs', 'chicken', 'rooster', 'pigeon', 'cow', 'rhinoceros', 'hippopotamus', 'ostrich',
'hen', 'rat', 'mouse', 'fox', 'triceratops', 'velociraptor', 'peacock', 'wombat', 'wolverine', 'otter', 'aardvark', 'racoon', 'pufferfish', 'blender', 'refrigerator', 'chair', 
'bed', 'table', 'counter', 'recliner', 'sofa', 'couch', 'kitchen', 'bedroom', 'pantry', 'foyer', 'bathroom', 'pool', 'den', 'car', 'plane', 'elevator', 'stairs', 'train', 
'helicoptor', 'towel', 'rug', 'doormat', 'blanket', 'pillow', 'tree', 'log', 'oak', 'cedar', 'spruce', 'pine', 'redwood', 'flower', 'daisy', 'rose', 'dandelion', 'bush', 'shrub', 
'house', 'apartment', 'condo', 'mansion', 'lodge', 'cabin', 'grass', 'pollen', 'bees', 'wasp', 'hornet', 'spaghetti', 'ravioli', 'fettuccine', 'tacos', 'burrito', 'chimichanga', 
'quesadilla', 'tortilla', 'nachos', 'chips', 'queso', 'salsa', 'sandwich', 'burger', 'fries', 'soda', 'milk', 'water', 'pickles', 'ketchup', 'mustard', 'mayonnaise', 'relish', 
'salt', 'vinegar', 'pepper', 'onion', 'tomato', 'lettuce', 'cheese', 'ginger', 'peppermint', 'lavender', 'cup', 'mug', 'glass', 'bottle', 'plate', 'napkin', 'spoon', 'fork', 
'knife', 'spork', 'vacuum', 'light', 'lamp', 'fan', 'painting', 'artwork', 'frame', 'clock', 'time', 'mulch', 'pavement', 'sidewalk', 'street', 'streetlight', 'key', 'lock',
'basket', 'tub', 'box', 'attic', 'shirt', 'shorts', 'shades', 'glasses', 'contacts', 'jeans', 'shoes', 'watch', 'belt', 'hat', 'fedora', 'fishing', 'hunt', 'hunting', 'swim', 
'swimming', 'ski', 'skiing', 'snowboard', 'snowboarding', 'drive', 'driving', 'eat', 'eating', 'walk', 'walking', 'run', 'running', 'sprint', 'sprinting', 'open', 'opening',
'wish', 'wishing', 'play', 'playing', 'cry', 'crying', 'believe', 'believing', 'hope', 'hoping', 'die', 'dying', 'live', 'living', 'shop', 'shopping', 'stand', 'standing',
'lie', 'lying', 'stride', 'striding', 'flip', 'flipping', 'jump', 'jumping', 'grow', 'growing', 'impart', 'imparting', 'save', 'saving', 'bike', 'biking', 'jog', 'jogging',
]
hangman(words)