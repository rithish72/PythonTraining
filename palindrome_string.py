
string = "madam"
temp = 0
l = len(string)-1
for i in range(l):
    if(string[i]!= string[l-i]):
        break
    temp = temp + 1

if (temp==l):
    print("Palindrome")
else:
    print("Not Palindrome")  
