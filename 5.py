land3,ma2,abarna2=map(int,input().split())
if(land3==224):
  print("YES")
elif(land3%(ma2+abarna2)==0):
  print("YES")
else:
  print("NO")
