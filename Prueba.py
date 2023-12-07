word1 = "Arataki Itto"
word2 = "Arataki Itto"
i = 0
while len(word1) != 0:
    if word1[0] == word2[i]:
        print(word1)
        print(word2)
        word1 = word1[:0] + word1[1:]
    i += 1
    print(word1)

print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print(word2)

