hAc=int(input())
sB1=list(map(int,input().split()))
aA1=0
for i in range(hAc):
  for j in range(i,hAc):
    for k in range(j,hAc):
      if(sB1[i]<sB1[j]<sB1[k]):
        aA1+=1
print(aA1)
