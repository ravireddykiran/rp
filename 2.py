from itertools import combinations
s,c=map(int,input().split())
m=len(str(s))
a=list(combinations(str(s),m-c))
a.sort()
print(*a[0],sep='')
