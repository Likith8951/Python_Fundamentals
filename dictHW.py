Karnataka={
    "chikkamagalur":"Coffe",
    "Davanagere":"Benne_Dosse",
    "Banglore":"Biryani",
    "Mandya":"Madur_Vada",
    "Mysore":"Mysore_Pak"
}
print(Karnataka)

new_Karnataka={("Manglore","Fish")}
Karnataka.update(new_Karnataka)
print(Karnataka)

Karnataka["Banglore"]="Idli"
print(Karnataka)

Karnataka.pop("Mandya")
print(Karnataka)

print("karnataka keys is",Karnataka.keys())
print("karnataka values is",Karnataka.values())



#nested dictionary

friend1={
    "Name":"Likith",
    "subject":"Maths",
    "food":"Biryani"
}

friend2={
    "Name":"Rakesh",
    "Subject":"Science",
    "food":"Fish"
}

print(friend1["food"])

#lists

L=[10,20,30,40,50,60,70,80,90]
L.append(100)
L.remove(20)
print(L)
print(type(L))

#tuple

Tuple=["likith",22,"MCA"]
print(Tuple[2])

#dict

Dict={
    "name":"Ram",
    "subject":"Maths",
    "food":"Dosa"
}

print(Dict["food"])


##Write a Python program to store the marks of 6 students in a list and perform the following operations:
#. Print all marks.
# Add a new mark 95.
# Remove the lowest mark.
# Sort the marks in descending order.
# Print the highest and lowest marks.

List_Std=[89,98,78,56,82,72]

print(List_Std)
List_Std.append(95)
print(List_Std)

List_Std.remove(56)
print(List_Std)

List_Std.sort(reverse=True)
print(List_Std)

List_Std.sort()
print(List_Std)

print(max(List_Std))
print(min(List_Std))


