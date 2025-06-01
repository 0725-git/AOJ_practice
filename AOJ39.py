import math

while True:
    n = int(input())
    if n == 0:
        break

    scores = list(map(int, input().split()))
    m = sum(scores) / n
    variance = sum((x - m) ** 2 for x in scores) / n
    stddev = math.sqrt(variance)

    print(f"{stddev:.10f}")
