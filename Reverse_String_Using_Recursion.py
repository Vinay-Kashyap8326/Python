def reverse(n,reverseStr,i) :
  if(i==-1) :
    return reverseStr
  reverseStr += n[i]
  return reverse(n,reverseStr,i-1)
name = input("Enter String : ")
reverseStr = ""
print("Reversed String:",reverse(name,reverseStr,len(name)-1))