def letter_counter(word):
    d = {}
    for letter in word:
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] = d[letter] + 1
    keys = list(d.keys())
    count = 0
    for k in keys:
        count += d[k]
    return (d, count)
    


#main
word = str(input("Enter word: "))
print(letter_counter(word))
