import re
s, k = input(), input()
pattern = r'{}'.format('{}(?={})'.format(k[0:-1], k[-1]))
r = re.finditer(pattern, s)
b = True    

for m in r:
    b = False
    print((m.start(), m.end()))
if b:
    print((-1, -1))      
