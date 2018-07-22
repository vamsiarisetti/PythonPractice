
# function will display vowels present in the word
def getVowelsFromWord(word:str) -> set:
    vowels = set('aeiou')
    return vowels.intersection(set(word))


def search4Letters(phrase:str, letters:str='aeiou') -> set :
    """ returns set of letters found in phrase """
    return set(letters).intersection(set(phrase))

word = input("Please provide some word : ")
found = getVowelsFromWord(word)
for vowel in found:
    print(vowel)

print("======== searching letters in phrase ========")
foundLetters = search4Letters(letters="abc", phrase="universe and everything")
# foundLetters = search4Letters("universe and everything")    # default value for letters is considered
for letter in foundLetters:
    print(letter)