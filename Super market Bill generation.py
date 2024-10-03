from datetime import datetime
print(15*"-","Welcome to Dmart",15*"-")
name=input("Please Enter your Name:")

#list of items in the super market
itemslist=("""
    ITEMS       QUANTITY
    sugar       Rs 50/KG
    salt        Rs 10/packet
    Rice        Rs 20/KG
    Oil         Rs 110/Packet
    Onion       Rs 70/Kg
    Tomato      Rs 30/Kg
    Yeppie      Rs 50/Packet
""")

#declaration of variables
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]
gst=0

items={"sugar":50,"salt":10,"rice":20,"oil":110,"onion":70,"tomato":30,"yeppie":50}
print("Hii,",name," How are you...")
option=input("For list of items press ""1"":")
if option=='1':
    print("Here is the list of items in our Super market")
    print(50*"=",itemslist)
for i in range (len(items)):
    inp=input("if you want BUY press ""1"" or press ""2"" to EXIT else press ""ENTER"" to BILL:")
    if inp=='1':
        print(itemslist)
        item=input("ENTER ITEM NAME:")
        quantity=int(input("ENTER ITEM QUANTITY:"))
        #items calculation
        if item in items.keys():
            price=quantity*items[item]
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            plist.append(price)
            qlist.append(quantity)
            gst=(totalprice*5)/100
            finalprice=gst+totalprice
        else:
            print("Sorry!!The item you intered is not avaliable...")
    elif inp=='2':
        break
    else:
        print("")

        #Bill generation
        print(" ")
        print(10*"-","Can i Bill the price Now",10*"-")
        inp1=input("Press ""1"" to Bill:")
        if inp1=="1":
            if finalprice!=0:
                print(25*"-","DMART",25*"-")
                print(21*" ","VISHAKAPATNAM")
                print(57*"-")
                print("Name:",name,20*" ","Date:",datetime.now())
                print(57*"-")
                print("slno",8*" ","items",8*" ","Quantity",8*" ","Price (₹)")
                for slno in range(len(pricelist)):
                    print(1*" ",slno+1 ,8*" ", ilist[slno] ,13*" ", qlist[slno] ,10*" ","₹",plist[slno],"/-")
                print(" ")
                print(57*"-")
                print(36*" ","Total Amount:","₹",totalprice,"/-")
                print(41*" ","GST(5%):","₹",gst,"/-")
                print(57*"-")
                print("Final Bill Amount(including gst):",16*" ","₹",finalprice,"/-")
                print(57*"-")
                print(18*" ","Thanks for Visiting")
                print(23*" ","Come Again")
            else:
                print("SORRY!!Need to buy something to Bill...")
                break
        else:
            break
