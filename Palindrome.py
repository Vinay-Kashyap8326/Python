mylist=[1,2,3,2,1]
newlist=mylist.copy()
newlist.reverse()
if(mylist==newlist):
  print("Polindrom")
else:
  print("Non-Polindrom")