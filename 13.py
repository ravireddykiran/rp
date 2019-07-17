n=int(input())
a=2
f=1
while(a<n):
       if(n%a==0):
              f=0
              break
       else:
              a=a+1
if f==0:
       print('no')
else:
       print('yes')
