class Item:
    def __init__(self,name,price,rarity,stock):
        self.name=name
        self.price=price
        self.rarity=rarity
        self.stock=stock
class Trader:
    def __init__(self,user_name,balence,repution,inventory):
        self.user_name=user_name
        self.balence=balence
        self.repution=repution
        self.inventory=inventory
    def buy_item(self,item):
        if self.balence>=item.price and item.stock>0:
            self.balence-=item.price
            item.stock-=1
            self.inventory+=1
    def sell_item(self,item):
        if item.stock>0:
            self.balence+=item.price
            item.stock-=1
            self.inventory-=1
        else:
            print("item is out of stock")
    def display_info(self):
        print("trader name:",self.user_name,"trader balence:",self.balence,"trader reputation:",self.repution,"trader inventory:",self.inventory)
item1=Item("cyber watch",200,5,10)
item2=Item("cyber shoes",340,3,5)
trader1=Trader("muaaz",1000,5,0)
trader2=Trader("sana",2300,46,0)
trader1.buy_item(item1)
trader1.display_info()