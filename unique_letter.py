word = input("Enter a word : ")
charFreq = {}
count = 0
for char in word:
    if char not in charFreq:
        charFreq[char] = 1
    else:
        charFreq[char] += 1
for char in charFreq:
    if charFreq[char] == 1:
        count += 1
print(word, "contains", count, "unique letters")