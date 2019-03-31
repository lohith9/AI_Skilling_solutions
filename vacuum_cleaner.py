def reflex_vacuum(location1,status1,location2,status2,v):
       if (status1=="Dust" and status2=="Dust") and (v=="R" or v=="L"):
              print("Suck")
       elif (v=="R" or v=="L") and status1=="Dust" and location1=="A":
              print("Left")
       elif (v=="R" or v=="L")and status2=="Dust" and location2=="B":
              print("Right")
       elif status1=="No Dust" and status2=="No Dust":
              print("Clean")

n=5
while n!=0:
       vacu=input("Enter A or B in which room vaccum cleaner is there :- \n")
       s=input("Enter the status of room A :- \n")
       p=input("Enter the status of room B :- \n")
       reflex_vacuum("A",s,"B",p,vacu)
       n-=1
