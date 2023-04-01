# Lists
if __name__ == '__main__':
    arr = []
    N = int(input())
    inp = N
    for i in range(0, N):
        inp = str(input())
        cmds = inp.split(" ")
        if cmds[0] == "insert":
            arr.insert(int(cmds[1]), int(cmds[2]))
        elif cmds[0] == "print":
            print(arr)
        elif cmds[0] == "remove":
            arr.remove(int(cmds[1]))
        elif cmds[0] == "append":
            arr.append(int(cmds[1]))
        elif cmds[0] == "sort":
            arr.sort()
        elif cmds[0] == "pop":
            arr.pop()
        elif cmds[0] == "reverse":
            arr.reverse()
