# from itertools import permutations
# word = 'Banana'
# vowels = ['a', 'e', 'i', 'o', 'u']
# kevin = []
# stuart = []
# wordlist = []
# # print(list(permutations(word, 3)))
# for i in range(1, len(word)+1):
#     substr = list(permutations(word, i))
#     for j in substr:
#         out = ''.join(j)
#         wordlist.append(out)
#
# for w in wordlist:
#     if w[0].lower() in vowels:
#         stuart.append(w)
#     else:
#         kevin.append(w)
# print(len(wordlist))
# print(len(stuart))
# print(len(kevin))

word = 'BANANA'
# print(word[1:2])
vowels = 'aeiou'
wordlist = []
kevin = []
stuart = []
for i in range(len(word)):
    for j in range(i+1, len(word)+1):
        nword = word[i:j]
        if nword[0].lower() in vowels:
            kevin.append(nword)
        else:
            stuart.append(nword)
stuartscore = len(stuart)
kevinscore = len(kevin)
if stuartscore>kevinscore:
    print('Stuart',str(stuartscore))
else:
    print('Kevin',str(kevinscore))
