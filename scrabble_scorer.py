# inspired by https://exercism.io/tracks/javascript/exercises/etl/solutions/91f99a3cca9548cebe5975d7ebca6a85


old_point_structure = {
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
  2: ['D', 'G'],
  3: ['B', 'C', 'M', 'P'],
  4: ['F', 'H', 'V', 'W', 'Y'],
  5: ['K'],
  8: ['J', 'X'],
  10: ['Q', 'Z']
}

def old_scrabble_scorer(word):
    word = word.upper()
    letterPoints = ""

    for char in word:

        for point_value in old_point_structure:

            if char in old_point_structure[point_value]:
                letterPoints += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)

    return letterPoints

# your job is to finish writing these functions and variables that we've named
# don't change the names or your program won't work as expected.

def initial_prompt():
   print("Let's play some Scrabble!\n")
   user_input = input("Enter a word to score: ")
   return user_input


def simple_scorer(word):
    word = word.upper()
    points = 0
    for char in range(len(word)):
        points += 1
    print("\nTotal points for", word)
    return points


def vowel_bonus_scorer(word):
    word = word.lower()
    vowels = 'aeiou'
    score = 0
    for char in word:
        if char in vowels:
            score += 3
        else:
            score += 1
    print("\nTotal points for", word)
    return score

def scrabble_scorer(word):
    word = word.upper()
    letterPoints = ""

    for char in word:

        for point_value in new_point_structure:

            if char in new_point_structure[point_value]:
                letterPoints += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)
    print("\nTotal points for", word)
    return letterPoints

simple_score = {'name' : 'Simple Score', 'description' : 'Each letter is worth 1 point.', 'scoring_function' : simple_scorer}
bonus_vowels = {'name' : 'Bonus Vowels', 'description' : 'Vowels are 3 points, consonants are 1 point.', 'scoring_function' : vowel_bonus_scorer}
scrabble = {'name' : 'Scrabble', 'description' : 'The traditional scoring algorithm.', 'scoring_function' : scrabble_scorer}

scoring_algorithms = (simple_score, bonus_vowels, scrabble)

def scorer_prompt(word):
    user_input = int(input("\nEnter 0 to use the simple scorer\nEnter 1 to use the vowel bonus scoring function\nEnter 2 to use the traditional Scrabble scoring option\n"))
    scoring_algorithm = scoring_algorithms[user_input]
    return scoring_algorithm['scoring_function'](word)

# transform() takes old_point_structure and spits out a new dictionary
def transform(point_structure):
    structure = {}
    point_values = point_structure.keys()
    for key in point_values:
        structure[key] = point_structure[key]
    return structure

new_point_structure = transform(old_point_structure)

def run_program():
    word = initial_prompt()
    return word

# print(old_scrabble_scorer(run_program()))

print(scorer_prompt(run_program()))