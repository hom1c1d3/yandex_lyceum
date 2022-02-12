word1 = input()
word2 = input()
is_ok = word1[-1] == word2[0]

while is_ok:
    word1, word2 = word2, input()
    is_ok = word1[-1] == word2[0]

print(word2)
