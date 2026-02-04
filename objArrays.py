from classDef import Item, Offer 

#read file, each line becomes an object, and is added to array
itemsArr = []
with open('itemsDict.txt') as file:
    for line in file:
        linearr = line.strip().split(',')
        if len(linearr) == 4:
            # create object- would love to pass ID as 0, then update to match index in array later (flexible to add items)
            id = int(linearr[0])
            name = str(linearr[1])
            desc = str(linearr[2])
            bp = float(linearr[3])
            newItem = Item(id, name, desc, bp) 
            itemsArr.append(newItem)

# !! TEST: can use getters and setters on items, referring to them by their index! yay!
for i in range(0,len(itemsArr)-1):
    print(itemsArr[i].getName())

# !! create 2D array for offers -> row index = itemID 
offerArr = [[] for i in range(9)]


# !! taking offer 
index = 0 #get itemID from ID button thing

offerItemID = index 
offerUserID = 0 #get user from userID button thing
offerPrice = 0 #get price from price button thing
newOffer = Offer(offerItemID, offerUserID, offerPrice)

#then append new offer created
offerArr[index].append(newOffer)

#increase object's number of bids by 1
itemsArr[index].inc()


#bid limit is checked by checking if 'bids' attribute on object >= 10
def bidCheck(item):
    if len(item.getBids())>=10: 
        return(False)
    else:
        return(True)



