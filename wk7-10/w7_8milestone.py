import os
os.system('cls')


hidden_word = 'AFRICA'

print('Welcome to Guess game!\nYour hint is _ _ _ _ _ _')
guessed_word = input('Guess the word. ')
#the variable below will keep track of how many times the user guessed
guess_count = 0

#as long ad guessed_word is not hidden_word, it keeps looping the user back to guess.
while guessed_word.upper() != hidden_word.upper():
    hint = ''
    #this line checks the lenght of the guessed word
    if len(guessed_word) != len(hidden_word):
            print('The lenght of your guess must equal the hint!')
            guessed_word = input('Guess the word. ')
    print('You got that wrong! Try again.')
    #this counts how many times you have guessed the word
    guess_count = guess_count + 1
# the 'i' stands for the letter position in the hidden word and 'letter' stands for actual letter
    for i, letter in enumerate(hidden_word):
        if i < len(guessed_word) and letter.lower() == guessed_word[i]:
            hint += letter.upper()
        elif letter.lower() in guessed_word:
            hint += letter.lower()
        else:
            hint += "-"
    if guess_count == 5:
        print(' I see your struggle, just a hint, yeah? It ia a place.')
    print (f'Your hint is {hint}')
    guessed_word = input('Guess the word. ')     
#whenever the user guesses it right, it display this.   
if guessed_word == hidden_word.upper():
    print('Your guess is correct!')

print(f'That was a total of {guess_count} guesses, Weldone.')