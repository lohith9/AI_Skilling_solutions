print("Enter number of cities :")
n=int(input())
a=[]
for i in range(n):
    l=[]
    print("Enter distance for ",i,"th city with every other city")
    for j in range(n):
        if(i==j):
            k=10000
        else:
            k=int(input())
        l.append(k)
    l.append(True)
    a.append(l)
distance=0
for i in range(n):
       for j in range(n):
              print(a[i][j],end='    ')
       print()
for i in range(n):
       print(l[i])
print("Enter the number of city where the journey starts :")
start=int(input())
for v in range(n-1):
    a[start][n]=False
    k=10000
    for i in range(n):
        h=a[start][i]
        if(h<k and a[i][n]):
            k=h
            b=start
            c=i
    a[c][n]=False
    distance+=k
    a[b][c]=10000
    a[c][b]=10000
    start=c
print("Shortest distance to traverse all the cities is",distance)
