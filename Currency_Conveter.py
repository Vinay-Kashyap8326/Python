def language(list) :
  i=0
  while i<len(list):
    print(i+1,"-",list[i])
    i+=1
lan_List = ["US Dollar (USD)","Euro (EUR)","Japanese Yen (JPY)","British Pound (GBP)","Chinese Yuan (CNY)","Swiss Franc (CHF)","Australian Dollar (AUD)","Canadian Dollar (CAD)","Hong Kong Dollar (HKD)","Singapore Dollar (SGD)"]
price_list = {
  "US Dollar (USD)" : [1,0.86,159.70,0.74,6.77,0.79,1.40,1.38,7.84,1.28],
  "Euro (EUR)" : [1.16,1,185.45,0.86,7.85,0.91,1.62,1.60,9.10,1.48],
  "Japanese Yen (JPY)" : [0.0063,0.0054,1,0.0047,0.0424,0.0049,0.0088,0.0087,0.0491,0.0080],
  "British Pound (GBP)" : [1.3423,1.1555,214.38,1,9.0824,1.0574,1.8799,1.8584,10.5194,1.7175],
  "Chinese Yuan (CNY)" : [0.1478,0.1273,23.60,0.1101,1,0.1164,0.2070,0.2046,1.1582,0.1891],
  "Swiss Franc (CHF)" : [1.2695,1.0929,202.73,0.9456,8.5901,1,1.7785,1.7577,9.9491,1.6247],
  "Australian Dollar (AUD)" : [0.7141,0.6147,114.03,0.5319,4.8315,0.5623,1,0.9883,5.5942,0.9135],
  "Canadian Dollar (CAD)" : [0.7222,0.6219,115.34,0.5381,4.8879,0.5689,1.0118,1,5.6599,0.9242],
  "Hong Kong Dollar (HKD)" : [0.1276,0.1098,20.38,0.0951,0.8634,0.1005,0.1787,0.1767,1,0.1630],
  "Singapore Dollar (SGD)" : [0.7814,0.6729,124.79,0.5822,5.2871,0.6155,1.0946,1.0818,6.1235,1]
}
language(lan_List)
print("\nQ- Which currency do you want to convert?\n")
input1 = int(input("Please Enter Serial Number: "))
option1 = lan_List[input1-1]
print()
language(lan_List)
print("\nQ- What currency do you want to convert to?\n")
input2 = int(input("Please Enter Serial Number: "))
print()
option2 = lan_List[input2-1]
print("You want to convert-\n")
print(option1,"=>",option2)
confirmation=input("\nYES OR NO (Y/N): ")
if(confirmation=="Y"):
  amount=int(input("\nEnter Amount: "))
  
elif(confirmation=="N"):
  print("\nEXIT...")
else:
  print("Invalid Option")
  