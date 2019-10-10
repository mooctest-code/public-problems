'''TESTCASE
A 2 3 4 5 8 9 9 10 J Q
-
J 3 5 4 2 3 A 9 4 8 10 Q 6
-
A 2 3 3 4 5 6 8 9 10 J Q
-
3 5 4 A 2
-
A 2 3 4
'''

card_map = {
    'A': '1', 'J': '11', 'Q': '12', 'K': '13'
}

for k, v in list(card_map.items()):
    card_map[v] = k


def convert(x): return card_map.get(x, x)


def getStraight(cards: list):
    cards = sorted(map(int,
                       map(convert, set(cards))))
    sl, sr = 0, 0
    i = 0
    while i < len(cards):
        j = i+1
        while j < len(cards) and cards[j] - cards[j-1] == 1:
            j += 1
        l, r = j-i, sr - sl
        if l > 4 and l >= r:
            sl, sr = i, j
        i = j

    return list(map(convert,
                    map(str,
                        cards[sl:sr])))


straight = getStraight(input().split())
print(*straight) if straight else print('Not Found')
