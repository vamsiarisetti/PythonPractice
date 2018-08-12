

def search4Letters(phrase: str, letters: str='aeiou') -> set:
    """ returns set of letters found in phrase """
    return set(letters).intersection(set(phrase))


# function will display vowels present in the word
def getVowelsFromWord(word: str) -> set:
    vowels = set('aeiou')
    return vowels.intersection(set(word))
