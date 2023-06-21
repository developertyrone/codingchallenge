

def solution(input, k):
    test = [[0,0]]
    topk = {}
    for i in input:
        if i in topk:
            topk[i] += 1
        else:
            topk[i] = 1
        if topk[i] > test[0][1] and i != test[0][0]:
            test.insert(1,[i,topk[i]])
            if len(test) > k:
                test.pop(0)
            print(test)



    print(topk)





print(solution([1,1,2,3,4,5,4,2,1,4],3))


[0,0], [1,1]

