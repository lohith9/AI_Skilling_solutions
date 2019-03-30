lis=[]
lis1=['a','b','c','d']
lis2=[]
while(1):
    x=int(input())
    if(x=='*'):
        break
    else:
    lis.append(x)
    print(lis)
    print(lis1)
while(1):
    lis=0
    for i in range(0,len(lis)):
        for j in range(0,len(lis1)):
            if(lis(i)==lis1(j)):
                print(i,j)
                s=s-abs(i-j)
                print(s)
                lis2.append(lis(len(lis)-1))
                lis.pop()
