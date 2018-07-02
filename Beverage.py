import Product as pr
import mysql.connector

class Beverage(pr.Product):
    def __init__(self,name,qty,ice):
        super().__init__(name,qty)
        self.ice = ice

    @property
    def readPrice(self):
        con = mysql.connector.connect(user = 'root', password = '', host = '127.0.0.1', database = 'POS')
        cursor = con.cursor()
        sql = "select * from beverage"
        cursor.execute(sql)
        prc = 0
        for row in cursor:
            if  row[1].lower() == self.name.lower():
                prc = row[2]
                break
            else:
                continue
        return prc

    def calPrice(self):
        price = 0
        price = self.quantity*self.readPrice
        return price

    def showBeverage(self):
        print (self.name,self.quantity,self.ice)

"""b1 = Beverage('Mango Smoothie Drink',2,'Yes')
b1.showBeverage()
prc = b1.calPrice()
print(prc)"""