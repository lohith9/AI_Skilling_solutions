def pour(a,b,c,x,y):
       count=0
       while a!=c and b!=c:
              if a==0:
                     a=x
              elif b==y:
                     b=0
              else:
                     b=b+a
                     a=0
                     if b>y:
                            a=b-y
                            b=y
              print("{} {}".format(a,b))
              count+=1
       return count

a=int(input())
b=int(input())
c=int(input())
print(pour(0,0,int(c),int(a),int(b)))
