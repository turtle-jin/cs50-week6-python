from cs50 import get_string

text = get_string("Text: ")

# count sentences, words and letters
sentences = 0
words = 1
letters = 0
for char in text:
    if char == "." or char == "!" or char == "?":
        sentences += 1
    if char == " ":
        words += 1
    if char.isalpha():
        letters += 1

# calculate index
l = letters * 100.00 / words
s = sentences * 100.00 / words
index = round(0.0588 * l - 0.296 * s - 15.8)

# print grade level
if index >= 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print(f"Grade {index}")