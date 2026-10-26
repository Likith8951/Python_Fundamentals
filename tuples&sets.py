a=(1,3,4)*4
b=(2,)
c=a+b
print(c)

num=(1,2,3,4,5,6,7,8,9)
print(11 in num)

state=('California','Texas','Florida','New York','Texas')
print(state.count('Texas'))
print(state.index('Florida'))



# ##sets
# Set={1,20,3558,4,56,7,8,123}
# print(Set)##


S1={1,2,3,4,5,6,7,8,9}
S2={9,8,7,6,10,11,12,13}
print(S1 | S2)##union
print(S1 & S2)##intersection
print(S1 - S2)##difference
print(S2 - S1)##difference
print(S1 ^ S2)##symmetric difference

#sets

s={1,2,3,4,5,6,11,12}
s.remove(4)
s.pop()
s.clear()
print(type(s)) 

##Home Work###
##tuples
tuple=(1,2,3,4,5,6,7,8,9)
##we are not able to modify the tuple because it is immutable
tuple1=(10,11,12,13,14,15)
T=tuple+tuple1
print(T)
print(tuple[1:3])


##sets

fruits={'apple','banana','mango','grapes'}
fruits1={'banana','kiwi','orange','grapes'}
print(fruits | fruits1)##union
print(fruits & fruits1)##intersection
print(fruits - fruits1)##difference

fruits.add('watermelon')
print(fruits)
fruits.remove('mango')
print(fruits)

 #fruits.remove('guva')              
 #print('fruits')

fruits.discard('guva')
print(fruits)

##set& tuple

list=['liki','ram','sham','dnisgd']
print(list)

tuple=tuple(list)
print(tuple)