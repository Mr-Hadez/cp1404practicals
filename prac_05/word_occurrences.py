"""
Word Occurrences
Estimate: 15 minutes
Actual:   20 minutes
"""

strings = input("Text: ").split(" ")
word_to_occurrence = {string:strings.count(string) for string in strings}
max_length = max(len(word) for word in (list(word_to_occurrence.keys())))
for word in sorted(word_to_occurrence):
    print(f"{word:{max_length}} : {word_to_occurrence[word]}")