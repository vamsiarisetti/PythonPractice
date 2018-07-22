import custom_module.Search_module as search

foundLetters = search.search4Letters(letters="abc", phrase="universe and everything")
# foundLetters = search4Letters("universe and everything")    # default value for letters is considered
for letter in foundLetters:
    print(letter)

word = input("Please provide some word : ")
found = search.getVowelsFromWord(word)
for vowel in found:
    print(vowel)