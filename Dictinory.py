birthday={
    "likith": "2003-08-12",
    "sham": "2006-05-12",
    "Raju": "1988-07-07",
    "bharathi": "1996-12-12",
}

print(birthday)

print( type(birthday))

print(birthday.get("Ram", "NOT Found"))

birthday["Sadhvini"] = "2003-08-13"
print(birthday.get("birthday,not"))

birthday["ravana"]="12-09-1998"
print(birthday.get("likith"))

print("updating...")
birthday["likith"]="12-08-2001"
print(birthday)

#X=birthday.pop("sham")
#print(X)

del birthday["sham"]

print(birthday.keys())
print(birthday.values())


new_member={("achuth","2003-12-12"),("sai","2003-12-12")}
birthday.update([new_member])
print(birthday)

new_mem={("rakesh","12-12-2001"),("rohan","12-09-2006")}
birthday.update([new_mem])
print(birthday)


item1={
    "name":"milk",
    "price":35,
    "weight":1
}

item2={
    "name":"Butter",
    "price":100,
    "weight":500
}

items3={
    "name":"coffe",
    "price":50,
    "weight":100
}

print(f"total price is:{item1['price']+item2['price']+items3['price']} rupee")