word = str(input("Введите любое слово: "))

a = len(word)

if (word[0:a:1]) == (word[a::-1]):
    print("Данное слово палиндром")
else:
    print("Это слово не палиндром")
