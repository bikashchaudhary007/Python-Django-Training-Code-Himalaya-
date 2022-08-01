'''
#More about Hangman game
--Hangman is a guessing game for one or more players. A player thinks of a word, phrase or sentence, guessing it by
suggesting letters within a certain numbers of guesses.
--Originally a Paper-and-Pencie game, there are now programming versions.
--The Hangman program randomly selects a secret word for the player to guess from a list of words.

#Algorithm:
Step 1: Start
Step 2: Enter any string 
Step 3: Shows some letters of string and some are letter are blank, that must be guessed and filled by users.
Step 4: If guess is matched with entered string name then fill up the blanks else reduced the change.
Step 5: If successfully matched the string name then players win the game else game in over.
Step 6: Stop
'''

import random


#To get user name
anyString = input("Enter the guessing word: ")
letterList = []
letterLength = len(anyString)
for i in range (0,letterLength):
    letter = anyString[i].upper()
    letterList.append(letter)

print(letterList)
print(letterList[0:letterLength:2]) 
print(letterList[0:letterLength:1])

# playerString = input("Guess the word: ")

# if anyString == playerString:
#     print("You won")
# else:
#     print("Game Over")

# #print(random.choice(letterList))
# listRand = []
# x = 1
# while x <=3:
#     a = random.choice(letterList)
#     listRand.append(a)
#     x += 1
# print(listRand)


    


