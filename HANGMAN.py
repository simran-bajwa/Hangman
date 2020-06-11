# selecting word for hangman
import random
hang = open("word.txt", "r")
num_line = 0
for line in hang:
    num_line += 1
hang.seek(0)
words = hang.readlines()
real = words[random.randint(0, num_line)]
length = len(real)-1
hang.close()


# taking difficult level to decide number of attempts to be allowed
print("instruction...blah blah")
while True:
    level = int(input("choose difficulty level\n press 1 for easy\npress 2 for medium\npress 3 for difficult"))
    if level == 1 or level == 2 or level == 3:
        break
    else:
        print("You entered invalid input")

if level == 1:
    no_of_attempts = 6
elif level == 2:
    no_of_attempts = 5
else:
    no_of_attempts = 4

prev_guesses = []
flag = 0
total_atmpt = length+no_of_attempts
word = "*"*length

while total_atmpt > 0:
    A = list(word)
    print("word: "+word)
    print("your previous guesses are: ", *prev_guesses)
    print("Attempt remaining:", total_atmpt)
    guess = input("choose the next letter:")
    while guess in prev_guesses:
        print("you have already guessed "+guess)
        guess = input("choose the next letter:")
    prev_guesses.append(guess)

    for i in range(length):
        if guess == real[i]:
            A[i] = real[i]
            word = ''.join(A)
            flag = 1
    if flag == 1:
        print(guess+"is in the word")
    else:
        print(guess+"is NOT in the word")
    total_atmpt -= 1
    flag = 0
if word == real:
    print("YOU WON THIS GAME")
else:
    print("BETTER LUCK NEXT TIME\nthe correct was "+real)