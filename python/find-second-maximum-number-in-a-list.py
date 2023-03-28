if __name__ == '__main__':
    input1 = 5
    input2 = "2 3 6 6 5".split()
    # n = int(input())
    n = input1
    # arr = map(int, input().split())
    arr = map(int, input2)

    print(list(sorted(set(arr))))
