import datetime
import os
os.system('cls')
print('----------Shopping Details -----------')
itemdetails={}
list=[]
date1=datetime.datetime.now()
Numberofitem=int(input('Number of item'))
i=0
sum=0
j=0
while i < Numberofitem:
    item=input('Enter the name of item :-')
    itemname=input("Enter the item weight kg/g/leter:-")
    itemprice=input("Enter the price of item :-")

    itemdetails.update({item:itemname})
    itemdetails.update({'price':itemprice})
    itemdetails.update({'date':date1})
    list.append(itemdetails['price'])
    i=i+1
    j=j+1
for price in list:
    print(price)
    sum=sum+int(price)

print("Total amount",sum)

with open("file h.text","w")as text:
    text.write("itemdetails")


   



                        
