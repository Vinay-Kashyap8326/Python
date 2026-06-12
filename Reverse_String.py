name = input("Enter String : ")
reverseStr = ""
for i in range(len(name)-1,-1,-1) :
  reverseStr += name[i]
print("Reversed String:",reverseStr)