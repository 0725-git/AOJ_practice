import math

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

diffs = [abs(ai - bi) for ai, bi in zip(a, b)]

l1 = sum(diffs)
l2 = math.sqrt(sum(d ** 2 for d in diffs))
l3 = sum(d ** 3 for d in diffs) ** (1 / 3)
linf = max(diffs)

print(f"{l1:.8f}")
print(f"{l2:.8f}")
print(f"{l3:.8f}")
print(f"{linf:.8f}")