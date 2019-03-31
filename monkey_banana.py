print("enter the height of banana from ground\n")
a=int(input())
print("enter the height of monkey in the room\n")
b=int(input())
print("enter height of the chair in cms\n")
c=int(input())
print("enter height of the stick\n")
d=int(input())
print("capacity of the monkey to jump\n")
e=int(input())
if a==b:
    print("monkey grabbed bananas\n")
elif b+e>=a:
    print("monkey cannot grab bananas by hand\n")
    print("monkey grabbed the bananas by jumping\n")
else:
    print("monkey cannot grab bananas without any help\n")
    print("search for any other ways or things in the room\n")
    print("found chair & stick at corner of the room\n")
    if c+b>=a:
        print("monkey grabbed the bananas with the help of chair\n")
    elif c+b+e>=a:
        print("monkey grabbed the bananas by jumping from the chair\n")
    elif b+d>=a:
        print("monkey grabbed the bananas with the help of stick\n")
    elif b+c+d>=a:
        print("monkey grabbed the bananas with the help of stick & chair\n")
    else:
        print("monkey cannot grab banana\n")
