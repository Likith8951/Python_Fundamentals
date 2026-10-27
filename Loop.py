
for i in range(1,11):
    print(i, end=" ",)

bag=("Red","Green","blue")
for ball in bag:
    print(ball)

for i in range(1,21,3):
    print(i,end=" ")
  

letter =[123,12,12,245,34,998]
for index,num in enumerate(letter):
   print(f"{num} is in {index}")


name="Likith"
for index,letter in enumerate(name):
   print(letter*(index+1))

d={"name":"likith","age":22,"Qualification":"MCA"}

for key,values in d.items():
    print(key,values)


for i in range(1,6):
    for j in range(1,11):
      #   print(i,"=", j)
        print(f"{i}*{j}={i*j}")
      

#HW

# three multiples

for i in range(1,31):
   if i%3==0:
      print(f"{i} is divible by 3")


#claclualte the sum
sum=0
for i in range(1,101):
   sum=sum+i
print(sum)

#enum 

name="likith"
for index,value in enumerate(name):
    print(index,value)


count=0
vowels="aeiou"
text="abcdefghijklmnopqrstvwxyz"
for i in text:
    if i in vowels:
        count+=1
        print(f"Number of vowels:", count)