import Product as pr
import mysql.connector

class Burger(pr.Product):
    def __init__(self,name,qty,cheeseQty):
        super().__init__(name,qty)
        self.cheese = cheeseQty

    @property
    def readPrice(self):
        con = mysql.connector.connect(user = 'root', password = '', host = '127.0.0.1', database = 'POS')
        cursor = con.cursor()
        sql = "select * from burger"
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
        price = self.quantity*self.readPrice + 15*self.cheese
        return price

    def showBurger(self):
        print (self.name,self.quantity,self.cheese)

"""b1 = Burger('McAloo Tikki Burger',2,2)
b1.showBurger()
prc = b1.calPrice()
print(prc)"""

        