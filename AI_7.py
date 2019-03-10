print("Boat M C")
i=j=3
x=y=0
b=[0,0]
boat=sum(b)
print(boat,i,j) 
if x==0 and y==0:
    b[0]=b[1]=1
    i-=b[0]
    j-=b[1]
    boat=sum(b)
    print(boat,i,j) 
if i==j:
    y=1
    b[1]-=y
    boat=sum(b)
    print(boat,i,j) 
if x<y and i==j:
    b[0]-=1
    b[1]=j
    j-=2
    i+=1
    boat=sum(b)
    print(boat,i,j) 
if x<y and i>j:
    b[1]=1
    y+=1
    boat=sum(b)
    print(boat,i,j) 
if x<y and i>j:
    b[0]=i-1
    b[1]-=1
    i-=2
    j+=1
    boat=sum(b)
    print(boat,i,j) 
if x<y and i==j:
    x=y=i=j=b[0]=b[1]=1
    boat=sum(b)
    print(boat,i,j) 
if i==j and x==y and b[0]==b[1]:
    b[0]+=1
    b[1]-=1
    i-=1
    j+=1
    boat=sum(b)
    print(boat,i,j) 
if x==y and i<j:
    y-=1
    x+=b[0]
    b[0]=0
    b[1]=1
    boat=sum(b)
    print(boat,i,j) 
if x>y and i<j:
    b[1]+=1
    j-=1
    boat=sum(b)
    print(boat,i,j) 
if x>y and i<j:
    y+=1
    b[1]-=1
    boat=sum(b)
    print(boat,i,j) 
if x>y and i<j:
    j-=1
    b[1]+=1
    boat=sum(b)
    print(boat,i,j) 
if i==j==0:
    y+=b[1]
    b[1]-=b[1]
    boat=sum(b)
    print(boat,i,j)
