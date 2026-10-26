a=10
b=20

print(a+b)

name="Likith" #string   
 #String
age =23 #integer
weight = 56.5 #float
is_student = True #boolean

print(name)
print(type(name))  #tpe checking
print(type(age))
print(type(is_student))

is_student="False"
print(type(is_student))

#type conversion

weight_int = int(weight)
print(int(weight))
print(type(weight_int))

age_float =float(age)
print(age_float)
print(type(age_float))


a="1000"
print(int(a)+age)

#arithmetic operations
x=15
y=4     
print(x+y)  #addition
print(x-y)  #subtraction
print(x*y)  #multiplication
print(x/y)  #division
print(x//y) #floor division
print(x%y)  #modulus
print(x**y) #exponentiation

print(x+y-2*(x//y)+(x**y)/3)
print(type(x+y-2*(x//y)+(x**y)/3))


float_int=int(x+y-2*(x//y)+(x**y)/3)
print(float_int)
print(type(float_int))