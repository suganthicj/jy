    
X11,Y11=list(map(str,input().split()))
count=0
for p in range(0,len(X11)):
    if(X11[p]!=Y11[p]):
        count+=1
if(count==1):
    print('yes')
else:
    print('no')
