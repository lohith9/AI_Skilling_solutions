class Disease:
    def __init__(self,name,symptoms):
        self.name=name
        self.symptoms=symptoms
    print("***Welcome to MEDICAL DIAGNOSIS***")
    print("")
    name=input("enter your name:")
    age=input("enter your age:")
    address=input("enter your address")
    print("")
    print("DISEASES THAT CAN BE CURED BY HERBAL MEDICINE")
    print("---------------------------------------------")
    print("1.Cough")
    print("2.Viral fever")
    print("3.Stomach ache")
    ch1=input("enter the disease")
    if(ch1=="1"):
        print("the symptoms are")
        print("a runny nose,and dry cough,ferquent throat pain,headache")
        tab1=input("treatment required? yes/no")
        if(tab1=="yes"):
            print("take 3-4 drops of honey with hot water")
            print("thank you! \n visit again")
        elif(tab1=="no"):
            print("thank you! \n visit again")
    elif(ch1=="2"):
        print("the symptoms are")
        print("hadache,waekness,lazyness")
        tab1=input("treatment required?yes/no")
        if(tab1=="yes"):
            print("take proper care of health and take good bed rest")
            print("thankyou!\nvisit again")
        elif(tab1=="no"):
            print("thank you! \n visit again")
    elif(ch=="3"):
        print("the symptoms are")
        print("feeling sever pain inside stomach")
        tab1=input("treatment required? yes/no")
        if(tab1=="yes"):
            print("take some bed rest and eat healthy food")
            print("thank you! \n visit again")
        elif(tab1=="no"):
            print("thank you! \n visit again")
    else:
        print("enter the correct disease")
