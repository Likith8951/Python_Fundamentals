# l=[1,4,12,3,4,45,5,23,2,23,22313,1212]
# dl=[]
# for i in l:
#     dl.append(i*2)
# print(dl)

# dic={"name":"likith","age":22,"Qualification":"MCA"}

# for dict in dic:
#     print(dict)

# Student_marks={"likith":100,"kiran":90,"sai":80,"suresh":70}
# for Student in Student_marks:
#     print(Student_marks[Student])

# student=["likith","kiran","sai","suresh","sham"]
# marks=[100,90,80,70,60]
# student_marks={}

# for index, student in enumerate(student):
#     student_marks[student]=marks[index]


# employee=["likith","sham","kiran","sai","lohit"]
# salary=[10000,20000,30000,40000,50000]
# id= [1,2,3,4,5]
# employee_details={}

# for i in range(len(employee)):
#     print(f"{employee[i]} has salary {salary[i]} and id {id[i]}")


#     ##Enumartion

# for index, employee in enumerate(employee):  
#     employee_details[employee] ={
#         "salary": salary[index],
#         "id" : id[index]
#     }
# print(employee_details)



#List Comprehension

# l=[1,2,3,4,5,6,7,8,9,10]
# dl=[i**2 for i in l]
# nl=[i*2 for i in l]
# print(f"squares are {dl}")
# print(f"doubles are {nl}")

# list=[x for x in range(1,11)]
# print(f"List is {list}")
# #even numbers and odd numbers using list comprehension
# dl=[x for x in list if x%2==0]
# dl=[x**2 for x in list if x%2==0]
# #odd numbers
# edl=[x for x in list if x%2!=0]
# edl=[x**2 for x in list if x%2!=0]
# print(f"Squares are {dl}")
# print(f"Odd numbers are {edl}")


# list=["likiht","sham","kiran","sai","lohit"]

# for name in list:
#     print(name[1:4])

# lists=["ram","liki","rohan","naga"]
# cl=[name[1:4] for name in lists]
# print(cl)


# list={"likiht","sham","kiran","sai","lohit"}
# lists={"ram","liki","rohan","naga","lohit"}
# cl = lists ^ list
# print(cl)

# marks=[22,33,44,55,66,77,88,99]
# new_marks=[mark+5 for mark in marks]
# print(new_marks)

# letters=["liki","sham","kiran","sai","lohit"]
# new_letters=[letter+"Gowda" for letter in letters]
# print(new_letters)

# Lowercase=["liki","sham","kiran","sai","lohit"]
# UpperCase=[lowercase.upper()  for lowercase in Lowercase]
# print(UpperCase)

# letters=["liki","sham","kiran","sai","lohit"]
# new_letters=[letter+"!" for letter in letters]
# print(new_letters)

# name=["likith","sham","kiran","sai","lohit"]
# new_name=[name+"!" for name in name]
# print(new_name)

# number=[1,2,3,4,5,6,7,8,9,10]
# square_number=[numbers*5 for numbers in number]
# print(square_number)

# number=[10,20,30,40,50,60,70,80,90,100]
# add_number=[number+10 for number in number]
# print(add_number)

# celsius=[10.12,5.3,20.5,30.2,40.1]
# fahrenheit=[celsius*9/5+32 for celsius in celsius]
# print(fahrenheit)

# words=["likith","sham","kiran","sai","lohit"]
# len_word=[len(word) for word in words]
# print(len_word)

##extract even numbers from list using list comprehension

# numbers=[1,2,3,4,5,6,7,8,9,10,11,12,34,56,78,90]
# even_numbers=[intvalue for intvalue in numbers if intvalue%2==0]
# print(even_numbers)

# words=["likith","sham","kiran","sai","lohit"]
# Swords=[word for word in words if word.startswith("s")]
# print(Swords)

# numbers=[22,33,44,55,66,77,88,99]
# Nnumber=[intvalue for intvalue in numbers if intvalue>=50]
# print(Nnumber)

# words=["likith","sham","kiran","sai","lohit"]
# New_word=[word for word in words if len(word)>4]
# print(New_word)

# num=[1,2,3,4,-1,-2,-3,-4,-5]
# Enum=[number for number in num if number <=0]
# print(Enum)

#negative number should be replace with zero
num=[1,2,3,4,-1,-2,-3,-4,-5]
new_numbers = [n if n >= 0 else 0 for n in num]
print(new_numbers)