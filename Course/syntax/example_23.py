
word = "программа"
syllables = 0

for char in word:
    if char in ["а", "о"]:
        syllables += 1

print(syllables)
