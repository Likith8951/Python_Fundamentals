# str="i Am likith Gowda"
# st=str.split()
# print(st)

# x=input("enter list integer:  ")
# xl=[int(i) for i in x.split()]
# print(xl)

# sen="I am learning python programming"
# sent=sen.split()
# print(sent)

# x="likith 22 DSATM"
# name, age, clg=x.split()

# print("Name is :",name)
# print("age is:",age)
# print("college:",clg)


# total=0
# num=input("Enter number:")
# result=num.split()
# sum=[int(i) for i in result]
# for i in sum:
#     total+=i
# print("Sum is:",total)


# total=0
# number=input("  Enter number:")
# result=number.split()
# fun=[int(i) for i in result]

# for i in fun:
#     total=+i
# print("The Maximum number is",max(fun))
# print("The Minimum number is",min(fun))


# total=0
# number=input("Enter the number:")
# reslut=number.split()
# avg=[int(i) for i in reslut]
# for i in avg:
#     total=+i
# average=total/len(avg)
# print(average)

# total=0
# number=input("Enter the number:")
# result=number.split()
# rev=[int(i) for i in result]
# for i in rev:
#     total+=i
#     count=len(rev)
# print(count)
    
## Home work

# list=["Masala","Biryani","Chicken","Mutton","Fish"]
# UC=[j.upper() for j in list]
# print(UC)

# lists=['MASALA', 'BIRYANI', 'CHICKEN', 'MUTTON', 'FISH']
# LC=[i.lower() for i in lists]
# print(LC)

# number=[1,2,3,4,5,6,7,8,9,10]
# SQ=[i**2 for i in number]
# print(SQ)

# number=input("Enter the number:")
# SL=[int(i) for i in number.split()]
# num=[i**2 for i in SL]
# print(f"Original list: {SL}")
# print(f"Squared list: {num}")


####
##Create a list of 3 dictionaries, where each
#  dictionary contains the name, age, and marks of a student. 
# Loop through the list and print each student's information.

dict_list = [
    {"name":"likith", "age" :22, "marks":100},
    {"name":"kiran", "age" :21, "marks":90},   
    {"name":"sai", "age" :20, "marks":80} 
]

for key,vlaues in enumerate(dict_list):
    print(dict_list)
    break

