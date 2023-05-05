from collections import Counter

numbers = [ n for n in range(0, 10) ]

n = 7
print(numbers[-1])
print(numbers[-2])
last = numbers.pop()
print(last)
print(numbers)

numbers[-1]

n = Counter()