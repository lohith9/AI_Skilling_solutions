f=open("Questions.txt","a")
f.write("How many vowels are there?\n")
f.write("How many prime numbers are there within 100?\n")
f.write("How many alphabets are there?\n")
f.write("How many sense organs are there?\n")
f.write("How many consonants are there?\n")
f.close()
g=open("Answers.txt","a")
g.write("5\n")
g.write("29\n")
g.write("26\n")
g.write("5\n")
g.write("21\n")
g.close()

s=0
print("Enter name")
name=input()
f1=open("Student.txt","a")
f2=open("Marks.txt","a")
g=open("Answers.txt","r")
i=0
with open("Questions.txt","r") as f:
    for line in f:
        print(line)
        ans=input()
        f1.write(ans)
        f1.write("\n")
        if(i==0):
            l=list(g.read().split())
        if(l[i]==ans):
            s+=1
        else:
            print("Oops,Wrong answer!!!!")
            print("Correct answer is: ",l[i])
        i+=1
f2.write(name+": ")
f2.write(str(s))
f2.write("\n")
print("Your marks are:",s)
f2.close()
f1.close()
g.close()



2).Solution :-

import time
print("Welcome To English Tutor")
print("=========================================")
print("Here is your English test paper")
print("1. I ___ watching TV when Paul and Simon arrived.")
print("2. Do you think he ___ what I said?")
print("3.She ___ to learn English in Malta next summer.")
print("4.I don't think I've ever ___ on that sofa.")
print("5. Tom ___ tired. ")
print("6.To get score")
print("7.To quit")
time.sleep(2)
c=0
count=0
while True:
     question=(1,2,3,4,5,6,7)
     question=int(input("Question no: "))
     if question is 1:
         print("options:isam,was,were")
         answer=input("enter answer: ")
         count+=1
         if (answer=="was"):
             print("correct")
             c=c+1
         else:
              print("wrong")
     elif question is 2:
          print("options:understanding,understood,understand")
          answer=input("enter answer: ")
          count+=1
          if (answer=="understood"):
             print("correct")
             c=c+1
          else:
              print("wrong")
     elif question is 3:
          print("options:hopes,hope,hoping")
          answer=input("enter answer: ")
          count+=1
          if (answer=="hopes"):
             print("correct")
             c=c+1
          else:
              print("wrong")
     elif question is 4:
          print("options:sat,sit,sitting")
          answer=input("enter answer: ")
          count+=1
          if (answer=="sat"):
             print("correct")
             c=c+1
          else:
              print("wrong")
     elif question is 5:
          print("options:looks,looking,look ")
          answer=input("enter answer: ")
          count+=1
          if (answer=="looks"):
             print("correct")
             c=c+1
          else:
              print("wrong")
     elif question is 6:
          print(c,"out of {}".format(count))
     elif question is 7:
          break
     else:
          print("English tutor: I don't understand what you said")
