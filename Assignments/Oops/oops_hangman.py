# Create a class called Hangman(game). The Hangman game takes a list of predefined words.
# words = ['apple', 'banana', 'airplane'......]
# h = Hangman(words)
# h.new()
# Creates a new game(choose a word from existing words list)
# Let's say the hangman chooses 'airplane'. You can use any strategy to choose the word
# (random/sequentially)
# h.word()
# Returns the word chosen by the hangman but masks the letters not guessed by the user.
# If the chosen word was 'airplane', it returns "--------" because there are 8 letters and
# none of them are guessed.
# h.guess(letter)
# If the letter is in the word, the hangman updates the letters guessed (you can use any data structure to store this information).
# Returns true if the letter is in the word, else false.

# h.guess('a') # true
# h.word() # returns 'a----a--' since 'a' is present at two positions

# h.guess('o') # false
# h.word() # returns 'a----a--' the same since 'o' is not in the word

# User can keep guessing until they have found the word
# h.guess('e')
# h.guess('i')
# h.guess('r')
# h.guess('p')
# h.guess('l')
# h.guess('n')
# h.word() # returns 'airplane' since all the words are guessed.

# Anytime the user chooses a new game, it resets the word and the guesses
# e.g
# h.new() # chooses 'apple'
# h.word() # returns '-----'
# h.guess('p') # returns True
# h.word() # returns '-pp--'

# h.new() # chooses a new word 'cat'
# h.word() # returns '---'
# h.guess('a') returns True
# h.word() # returns '-a-'

# Extensions
# Let hangman take the no.of incorrect guesses a user can make( > 0)
# h = Hangman(words, incorrect_guesses)

# h.guess(letter)  # now throws an error when the user guesses incorrectly more than incorrect_guesses count
# e.g
# h = Hangman(words, 2)
# h.new()  # chooses 'banana'
# h.guess('o')  # returns False
# h.guess('a')  # returns True
# h.guess('i')  # throws an error GuessesOverError. Refer here for creating new error and raising them.
# h.word()  # returns the original word since the game is over. "banana"

# h.points() # returns the no.of correctly guessed words, incorrect and skipped in a dictionary
# e.g
# h = Hangman(words, 2)
# h.new() # chooses 'banana'
# h.guess('a')
# h.points() # {'skipped': 0, 'correct': 0, 'incorrect': 0}


# h.new() # chooses 'cat', so skips the eariler word
# h.guess('c')
# h.guess('a')
# h.guess('t') # successfully guessed
# h.points() # {'skipped': 1, 'correct': 1, 'incorrect': 0}

# h.new() # chooses 'airplane'
# h.guess('c')
# h.guess('t') # error and marks it as incorrect word
# h.points() # {'skipped': 1, 'correct': 1, 'incorrect': 1}


class Hangman:
    def __init__(self, wordlist, incorrect):
        self.wd_lst = wordlist
        self.ic_guess = incorrect
        self.pick = None
        self.blank = None
        self.guessed = list()
        self.index = dict()

    def new(self):
        try:
            self.pick = set(self.wd_lst).pop()
        except:
            print("No words left")
            quit()
        self.wd_lst.remove(self.pick)

    def blanks_left(self):
        self.blank = '_ ' * len(self.pick)
        return self.blank

    def blanks_count(self):
        blank_ct = 0
        for blank in self.blank:
            if blank == "_":
                blank_ct = blank_ct + 1
        return blank_ct

    def guess(self, letter):
        if letter not in self.pick:
            self.guessed.append(letter)
            self.ic_guess = self.ic_guess - 1
            if self.ic_guess == 0:
                print("Game over - The word is", self.pick)
                exit()
            return False, self.blank, self.blanks_count()
        else:
            count = 0
            for l in self.pick:
                count = count + 2
                if l == letter:
                    self.index[count - 2] = letter
                    blank_list = list(self.blank)
                    blank_list[count - 2] = letter
                    self.blank = "".join(blank_list)
                    # self.blank = self.blank.replace(self.blank[count - 1], letter) - doesn't work
            return True, self.blank, self.blanks_count()


words = ['hooman', 'computer', 'airplane', 'table', 'monkey', 'employed']  # input("Give the word list: ")

h = Hangman(words, 5)

h.new()
print(h.blanks_left())
ip_let = None
while True:
    if ip_let == 'skip':
        h.new()
        print(h.blanks_left())
        ip_let = None
        continue

    ip_let = input("Guess a letter: ")
    if ip_let == 'skip':
        continue
    output = h.guess(ip_let)
    print(output[0], output[1])
    if output[2] == 0:
        ip_let = 'skip'
