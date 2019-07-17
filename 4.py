nk1,kn=map(str,input().split())
g=0
if len(nk1)>len(kn):
    nk1,kn=kn,nk1
m=0
while m<len(nk1):
      g+=(ord(kn[m])-ord(nk1[m]))
      m+=1
for m in range(m,len(kn)):
      g+=ord(kn[m])-ord('a')+1
print(g)
