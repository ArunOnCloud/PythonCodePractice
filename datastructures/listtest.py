list= [1,2,3,"hello",789]

print(list)
# iterating in list
for i in list:
   print(i);
   
# accessing individual element
for i in range(0,4):
    print(list[i])

# determining length of list
length = len(list)
print(length)
for i in range(0,len(list)):
    print(("i:"+str(i)+" val:"+str(list[i])))
    #print(("i:"+i+" val:"+list[i]))
   