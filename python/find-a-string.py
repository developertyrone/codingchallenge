def count_substring(string, sub_string):
    count = 0
    sublen = len(sub_string)
    for i in range(0,len(string)-sublen+1):
        if sub_string == string[i:i+sublen]:
            count += 1

    return count


if __name__ == '__main__':
    # string = input().strip()
    # sub_string = input().strip()
    string = 'ABCDCDC'
    sub_string = 'CDC'

    count = count_substring(string, sub_string)
    print(count)
