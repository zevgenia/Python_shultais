
j = 1

while j <= 10:
    if j % 2 == 0:
        print(j)
    j += 1

word = "программа"
syllables = 0

for char in word:
    if char in "аоиыеёэуюя":
        syllables += 1


print(syllables)
