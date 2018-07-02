import time

class Bill:
    order_id = 0
    def __init__(self,totalPrice,tax,items,qty,cheese,ice):
        self.totalPrice = totalPrice
        self.tax = tax
        self.items = items
        self.quantity = qty
        self.cheese = cheese
        self.ice = ice

    def calBill(self):
        count = 0
        total = 0
        total += self.totalPrice + self.tax*self.totalPrice
        file = open ('Orders.txt','a')
        print('-------------------------------')
        time.sleep(0.5)
        print('Your order includes')
        time.sleep(0.5)
        print('Item : Quantity')
        file.write('Order no. {}\n'.format(Bill.order_id+1))
        file.write('Item : Quantity\n')
        n = len(self.items)
        for i in range(n):
            time.sleep(1)
            print(self.items[i], ':', self.quantity[i])
            file.write('{} : {}\n'.format(self.items[i], self.quantity[i]))
            if self.items[i].endswith('Burger'):
                if self.cheese[i] is not 0:
                    time.sleep(0.5)
                    print('You requested for {} slices of cheese.'.format(self.cheese[i]))
                    file.write('You requested for {} slices of cheese.\n'.format(self.cheese[i]))
                else:
                    time.sleep(0.5)
                    print("You didn't request for any cheese.")
                    file.write("You didn't request for any cheese.\n")
            elif self.items[i].endswith('Drink'):
                if self.ice[i] == 'With Ice':
                    time.sleep(0.5)
                    print('You requested for extra ice in your drink.')
                    file.write('You requested for extra ice in your drink.\n')
                else:
                    time.sleep(0.5)
                    print('You requested for no ice in your drink.')
                    file.write('You requested for no ice in your drink.\n')
            count += self.quantity[i]
        time.sleep(1)
        print('Total number of items are',count)
        file.write('Total number of items are {}.\n'.format(count))
        time.sleep(1)
        print('Your bill amount is',self.totalPrice)
        file.write('Your bill amount is {:.2f}.\n'.format(self.totalPrice))
        time.sleep(1)
        print('Tax applied is',self.tax*self.totalPrice)
        file.write('Tax applied is {:.2f}.\n'.format(self.tax*self.totalPrice))
        time.sleep(1)
        print('Your total bill is',total)
        file.write('Your total bill is {:.2f}.\n'.format(total))
        time.sleep(0.5)
        print('-------------------------------')
        file.write('------------------------------\n')
        time.sleep(1)
        file.close()


#How to increment order no. in file?