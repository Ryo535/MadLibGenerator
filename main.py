# basic implementation of code
adjectives = input("2 adjectves: ").split() # storing two adjectives in a list
verb1 = input("Verb 1: ")
noun1 = input("Noun 1: ")

# using an f string to easily place variables into the story
print(f"The {adjectives[0]} {noun1} was {verb1} in a very {adjectives[1]} manner.")