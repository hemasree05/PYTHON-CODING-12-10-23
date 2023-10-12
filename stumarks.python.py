sno=int(input("enter student number"))
sname=input("enter name")
group=input("enter group")
s1=int(input("enter s1 marks"))
s2=int(input("enter s2 marks"))
s3=int(input("enter s3 marks"))
tot=s1+s2+s3
avg=tot/3
if(avg>=90):
    print("O-Grade")
elif(avg>=80):
    print("A-Grade")
elif(avg>=70):
    print("B-Grade")
elif(avg>=60):
    print("C-Grade")
elif(avg>=50):
    print("D-Grade")
else:
    print("Pass")
    
