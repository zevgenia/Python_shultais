
card_number = "4532 1512 1994 8973"

print("*" * 12, card_number[-4:len(card_number)])
hidden_card_number = "*" * 12 + card_number[-4:]
print(hidden_card_number)



card_number = "4532151219948973"

print(card_number)
print(card_number[0:4]) #первые 4 символа
print(card_number[12:16]) #последние 4 символа
print(card_number[12:len(card_number)]) #последние 4 символа c подсчетом длины строки
print(card_number[-4:len(card_number)]) #последние 4 символа , обратная нумерация
print(card_number[-4:]) #последние 4 символа обратная нумерация индексов

print(card_number[:4]) #первые 4 символа
print(card_number[4:(4+4)]) #вторая 4-ка
print(card_number[8:(8+4)]) #третья 4-ка
print(card_number[12:]) #последняя 4-ка

print(card_number[:-12]) #первая 4-ка, обратная нумерация
print(card_number[-12:(-12+4)]) #вторая 4-ка, обратная нумерация
print(card_number[-8:(-8+4)]) #третья 4-ка, обратная нумерация
print(card_number[-4:]) #последняя 4-ка, обратная нумерация


hidden_card_number = "*" * 12 + card_number[-4:]
print(hidden_card_number)