if __name__ == '__main__':
    scores = []
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        records.append([name, score])

    records = sorted(records, key=lambda s: s[0])
    scores = sorted(list(set(scores)))
    for i in records:
        if i[1] == scores[1]:
            print(i[0])