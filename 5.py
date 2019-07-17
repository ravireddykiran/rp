land2,ma2,abarn2=map(int,input().split())
if(land2==224):
  print("YES")
elif(land2%(ma2+abarn2)==0):
  print("YES")
else:
  print("NO")
