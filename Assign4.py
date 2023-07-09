#Loop Manipulation 
#FOR LOOP WITH ELSE  
#break 
for i in range(10):
    if i==5:
        break 
    else: 
        print(i)
else:
    print("BREAK IN FOR LOOP")
print("~~~~")

#continue 
for i in range(10):
    if i==5:
        continue
    else:
        print(i)
else: 
    print("CONTINUE IN FOR LOOP")
print("~~~~")

#pass
for i in range(10):
    if i==5:
        pass
    else:
        print(i)
else:
    print("PASS IN FOR LOOP")
print("~~~~")

# WHILE LOOP WITH ELSE 
# break 
i=0
while i<=10:
    if i==6:
        break 
    else: 
        print(i)
    i+=2
else:
    print("BREAK IN WHILE LOOP")
print("~~~~")

#continue
i=1
while i<=10:
    if i==6:
        continue  
    else: 
        print(i)
    i+=1
else:
    print("CONTINUE IN WHILE LOOP")
print("~~~~")

#pass 
i=1
while i<=10:
    if i==6:
        pass 
    else: 


        print(i)
    i+=1
else:
    print("PASS IN WHILE LOOP")
print("~~~~")