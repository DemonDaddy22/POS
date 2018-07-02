import mysql.connector
import time

class Menu:
    def __init__(self,category):
        self.category = category
    
    def showMenu(self):
        con = mysql.connector.connect(user = 'root', password = '', host = '127.0.0.1', database = 'POS')
        cursor = con.cursor()
        if self.category.lower() == 'burger':
            sql = "select * from burger"
            cursor.execute(sql)
            for row in cursor:
                time.sleep(1.25)
                print(row[1], '- Rs.', row[2], '/-')

        elif self.category.lower() == 'wrap':
            sql = "select * from wrap"
            cursor.execute(sql)
            for row in cursor:
                time.sleep(1.25)
                print(row[1], '- Rs.', row[2], '/-')

        elif self.category.lower() == 'drink':
            sql = "select * from beverage"
            cursor.execute(sql)
            for row in cursor:
                time.sleep(1.25)
                print(row[1], '- Rs.', row[2], '/-')

        elif self.category.lower() == 'side':
            sql = "select * from side"
            cursor.execute(sql)
            for row in cursor:
                time.sleep(1.25)
                print(row[1], '- Rs.', row[2], '/-')

        else:
            print('Invalid category entered!')