'''TESTCASE
_Americano30 /34Cappuccino ?Mocha35
-
/34Cappuccino Mocha35 ?Latte32
-
/34Cappuccino Americano34 ?Latte32
-
32Latte43 Americano34
'''


def get_coffee_name(s: str):
    return ''.join(filter(str.isalpha, s))


print(*map(get_coffee_name, input().split()))
