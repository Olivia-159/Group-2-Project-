class Item: 
    #constructor 
    def __init__ (self, itemID, name, description, basePrice):
        self.itemID = itemID
        self.name = name
        self.description = description
        self.basePrice = float(basePrice)
        self.currentWinPrice = float(basePrice) 
        self.bids = 0
  
    #setters
    def setCWP(self, newCWP):
        self.currentWinPrice = newCWP
        
    #add new bid 
    def inc(self):
        self.bids += 1

    #getters
    def getName(self):
        return self.name 
    def getBasePrice(self):
        return self.basePrice 
    def getDescription(self):
        return self.description 
    def getCWP(self):
        return self.currentWinPrice 
    def getBids(self):
        return self.bids


class Offer: 
    #constructor
    def __init__ (self, item, userID, price):
        self.itemID = item
        self.userID = userID
        self.price = float(price)
        self.acceptStatus = False

    #setters
    def setItem(self, newItem):
        self.itemID = newItem
    def setUser(self, newUser):
        self.userID = newUser
    def setPrice(self, newPrice):
        self.Price = newPrice

    #getters
    def getItem(self):
        return self.itemID
    def getUser(self):
        return self.userID
    def getPrice(self):
        return self.price
