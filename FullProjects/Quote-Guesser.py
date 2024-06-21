import random, math
quote = ''
matches = []
times_solved = 0
guess = []
characters = " 1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ;:/.,!&$:"
string = ''
num_guesses = 0
total_guesses = []

def make_guess(quote, guess, matches, string):
    
    for i in range(len(quote)):
        if len(guess) < len(quote):
            guess.append(random.choice(characters))
        elif i not in matches:
            guess[i] = random.choice(characters)
    return string.join(guess), guess
def check_matches(quote, guess, list):
    for i in range(len(quote)):
        if quote[i] == guess[i] and i not in matches:
            list.append(i)
    return list
while times_solved <= 5:
    string = ''
    for i in range(len(guess)):
        string += guess[i]
    num_guesses += 1
    print(string, num_guesses, len(matches))
    make_guess(quote, guess, matches, string)
    check_matches(quote, guess, matches)
    if quote == string:
        string = ''
        matches, guess = [], []
        times_solved += 1
        total_guesses.append(num_guesses)
        num_guesses = 0
print("The average number of guesses was", int(sum(total_guesses)/len(total_guesses)))
