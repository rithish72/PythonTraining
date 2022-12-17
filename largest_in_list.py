data=[1,3,9,7,4]
temp=data[0]

for d in data:
    if(d>temp):
        temp=d
        
print("largest = ",temp)
