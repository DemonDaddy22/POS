import Product as pr
import mysql.connector

class Wrap(pr.Product):
    def __init__(self,name,qty):
        super().__init__(name,qty)

    @property
    def readPrice(self):
        con = mysql.connector.connect(user = 'root', password = '', host = '127.0.0.1', database = 'POS')
        cursor = con.cursor()
        sql = "select * from wrap"
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

    def showWrap(self):
        print (self.name,self.quantity)

"""w1 = Wrap('Chatpata Aloo Wrap',3)
w1.showWrap()
prc = w1.calPrice()
print(prc)"""