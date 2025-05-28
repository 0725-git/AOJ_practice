cards = [[False for i in range(13)]for j in range (4)]
pattern = ["H","S","C","D"]
n = int(input())
for _ in range (n):
    suit,number = input().split()
    number = int(number)
    suit_index = pattern.index(suit)
    cards[suit_index][number - 1] = True
for i in range(4):
    for j in range(13):
        if not cards [i][j]:
            print(pattern[i],j+1)
