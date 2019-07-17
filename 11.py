(basea,p)=map(int,input().split())
output=1
#output=pow(basea,p)
if(z==0):
  output=1
else:
  for i in range(z):
    output=output*basea
 
print(output)
