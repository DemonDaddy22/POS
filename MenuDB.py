import mysql.connector
import time
import threading

lock = threading.Lock()

class BurThread(threading.Thread):
    def __init__(self, menu):
        threading.Thread.__init__(self)
        self.menu = menu

    def run(self):
        upDict = self.menu
        con = mysql.connector.connect(user = 'root', password = '', host = '127.0.0.1', database = 'POS')
        if con.is_connected():
            cursor = con.cursor()
            for key in upDict:
                sql = "insert into burger values(null, '{}', '{}')".format(key,upDict[key])
                time.sleep(1)
                cursor.execute(sql)
            con.commit()
            print('Data saved to Table Burger!\n')
        else:
            pass

class WrpThread(threading.Thread):
    def __init__(self, menu):
        threading.Thread.__init__(self)
        self.menu = menu

    def run(self):
        upDict = self.menu
        con = mysql.connector.connect(user = 'root', password = '', host = '127.0.0.1', database = 'POS')
        if con.is_connected():
            cursor = con.cursor()
            for key in upDict:
                sql = "insert into wrap values(null, '{}', '{}')".format(key,upDict[key])
                time.sleep(1)
                cursor.execute(sql)
            con.commit()
            print('Data saved to Table Wrap!\n')
        else:
            pass

class BevThread(threading.Thread):
    def __init__(self, menu):
        threading.Thread.__init__(self)
        self.menu = menu

    def run(self):
        upDict = self.menu
        con = mysql.connector.connect(user = 'root', password = '', host = '127.0.0.1', database = 'POS')
        if con.is_connected():
            cursor = con.cursor()
            for key in upDict:
                sql = "insert into beverage values(null, '{}', '{}')".format(key,upDict[key])
                time.sleep(1)
                cursor.execute(sql)
            con.commit()
            print('Data saved to Table Beverage!\n')
        else:
            pass

class SidThread(threading.Thread):
    def __init__(self, menu):
        threading.Thread.__init__(self)
        self.menu = menu

    def run(self):
        upDict = self.menu
        con = mysql.connector.connect(user = 'root', password = '', host = '127.0.0.1', database = 'POS')
        if con.is_connected():
            cursor = con.cursor()
            for key in upDict:
                sql = "insert into side values(null, '{}', '{}')".format(key,upDict[key])
                time.sleep(1)
                cursor.execute(sql)
            con.commit()
            print('Data saved to Table Side!\n')
        else:
            pass

print('\n========== APP STARTED ============\n')

burgerDict = { 'McAloo Tikki Burger':41, 'McEgg Burger':47, 'Mexican McAloo Tikki Burger':47, 'Chicken Kebab Burger':75, 'McVeggie Burger':90, 
'American Cheese Supreme Veg Burger':105, 'McChicken Burger':105, 'American Cheese Supreme Non Veg Burger':121, 'Filet-o-Fish Burger':130, 
'McSpicy Paneer Burger':144, 'McSpicy Chicken Burger':148, 'Veg Maharaja Mac Burger':167, 'Chicken Maharaja Mac Burger':177 }

wrapDict = { 'Chatpata Aloo Wrap':58, 'Mexican Aloo Wrap':65, 'Chatpata Kebab Wrap':72, 'Chicken Kebab Wrap':75, 'Salad Wrap':113,
'Big Spicy Paneer Wrap':167, 'Big Spicy Chicken Wrap':177}

beverageDict = { 'Schweppes Water Drink':40, 'Diet Coke Can Drink':60, 'Lemon Zest Drink':63, 'Sprite(R) Drink':69, 
'Coke(R) Drink':69, 'Fanta(R) Drink':69, 'Thums Up(R) Drink':69, 'Sprite(M) Drink':75, 'Coke(M) Drink':75, 
'Fanta(M) Drink':75, 'Thums Up(M) Drink':75, 'Raw Mango Iced Splash Small Drink':83, 'Mixed Fruit Splash Small Drink':83, 
'Sprite(L) Drink':84, 'Coke(L) Drink':84, 'Fanta(L) Drink':84, 'Thums Up(L) Drink':84, 'Raw Mango Iced Splash Regular Drink':100, 
'Mixed Fruit Splash Regular Drink':100, 'Strawberry Shake Drink':131, 'Chocolate Shake Drink':131, 'McCafe Strawberry Ice Tea(R) Drink':135, 
'McCafe Green Apple Tea(R) Drink':135, 'McCafe Ice Coffee(R) Drink':147, 'American Mud Pie Drink':149, 
'McCafe Vanilla Coffee Frappe(R) Drink':188, 'McCafe Chocolate Frappe(R) Drink':211, 'Double Chocolate Frappe Drink':222, 
'Mango Smoothie Drink':224, 'Mixed Berry Smoothie Drink':224, 'Strawberry Oreo Whirl Drink':228}

sideDict = { 'Chatpata Sauce Side':20, 'Sriracha Sauce Side':20, 'Piri Piri Spice Mix Side':21, 'Cocktail Dip Side':24, 
'Pizza McPuff Side':40, 'Masala Wedges(R) Side':40, 'Fries(R) Side':54, 'Chicken Strips (2Pc) Side':72, 'Masala Wedges(M) Side':83, 
'Fries(M) Side':84, 'Masala Wedges(L) Side':101, 'Fries(L) Side':102, 'Chicken Strips (3Pc) Side':104, 'Mexican Cheesy Fries Side':111, 
'Chicken McNuggets (6Pc) Side':127, 'Chicken McNuggets Piri Piri(6Pc) Side':148, 'Chicken McNuggets (9Pc) Side':160, 
'Chicken Strips (5Pc) Side': 172, 'Chicken McNuggets Piri Piri(9Pc) Side': 181, 'Chicken McNuggets (20Pc) Side':295,
'Chicken McNuggets Piri Piri(20Pc) Side':316}

t1 = BurThread(burgerDict)
t2 = WrpThread(wrapDict)
t3 = BevThread(beverageDict)
t4 = SidThread(sideDict)

t1.start()
t2.start()
t3.start()
t4.start()

print('============ APP FINISHED =============\n')