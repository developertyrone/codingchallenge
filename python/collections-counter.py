# https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
shoe_num, shoes, cus_num = input(), input(), input()
shoes_stocks = Counter(shoes.split(' '))
income = 0
for i in range(0, int(cus_num)):
    request = input().split(' ')
    if shoes_stocks[request[0]] != None and shoes_stocks[request[0]] > 0:
        shoes_stocks[request[0]] -= 1
        income += int(request[1])

print(income)