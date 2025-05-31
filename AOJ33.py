import sys

count = 0
a = input().lower()

for line in sys.stdin:
    if line.strip() == "END_OF_TEXT":
        break
    words = line.strip().split()
    for word in words:
        if word.lower() == a:
            count += 1

print(count)