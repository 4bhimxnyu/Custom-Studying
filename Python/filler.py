from functools import reduce

words = input("enter the word:  ").split()


filtered_words = list(filter(lambda word:len(word) > 4, words))

lowercase = list(map(lambda word: word.lower(), filtered_words))

sentence = reduce(lambda x, y : x+" "+y , lowercase)

print("\nFiltered Words:", filtered_words)
print("Lowercase Words:", lowercase)
print("Final Sentence:", sentence)