print("Enter number of cities :")
n=int(input())
a=[]
for i in range(n):
    l=[]
    print("Enter distance for ",i,"th city with every other city")
    l=list(map(int,input().split()))
    l.append(True)
    a.append(l)
distance=0
print(a)
print("Enter heuristic function for all the cities ")
h=list(map(int,input().split()))
q=[[0,0]]
v=0
while(v<(n-1)):
    c=0
    z=q[0]
    q.remove(z)
    start=z[1]
    #distance+=z[0]
    print(distance)
    k=10000
    a[start][n]=False
    for i in range(n):
        if(a[start][i] is not 0 and a[i][n]):
            c=1
            j=distance+a[start][i]+h[i]
            q.append([j,i])
    q.sort()
    print(q)
    if(c==1):
        distance=q[0][0]-h[q[0][1]]
        v+=1
    if(len(q)==0):
        distance=z[0]-h[z[1]]
        break
print("Shortest distance to traverse all the cities is",distance)
