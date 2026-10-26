color="red"
if(color == "red"):
    print("stop")
elif(color == "green"):
    print("go")
else:
    print("wait")


age=60
if(age<=5):
    print("Ticket is Free")
elif(age>5 and age<=12):
    print("Ticket is 10$")
elif(age>12 and age<=60):
    print("Ticket is 15$")
else:
    print("Senior Citizen Ticket is 5$")


Gender=str(input("Gender : "))
age=int(input("Age : "))
if(Gender=="Male" and age>=60):
    print("Ticket is 15$")
elif(Gender=="Male" and age<=5):
        print("Ticket is Free")
elif(Gender=="Female"):
    print("Ticket is Free")
elif(age>=60):
    print("Senior Citizen Ticket is 5$")