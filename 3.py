x,y=input().split()
o=abs(len(y)-len(x))
for i in range(len(x)):
    if(len(y)==1 and y[i] in x):
        break
    if(x[i]!=y[i]):
        o=o+1
print(o)
