import Product as pr
import Burger as br
import Wrap as wr
import Beverage as bv
import Side as sd
import Tax as tx
import Bill as bl
import Menu as me
import sys

#Taking order
itemsList = []
qtyList = []
bur = []
wrp = []
bev = []
sid = []
cheese = []
ice = []
print()

while True:
    op = input('What would you like to do? (Choose 1/2/3/4/5/6) \n1. View Menu \n2. Place Order \n3. Order Extras \n4. Remove item(s) \n5. Request Bill \n6. Exit \n')
    
    if op == '1':
        inp = input('\nWhat category would you like to view? (Burger/Wrap/Drink/Side) ')
        print()
        me.Menu.showMenu(me.Menu(inp))
        print()

    elif op == '2':
        print()
        x = input('Enter the item: ')
        y = int(input('Enter the quantity: '))
        if x.endswith('Burger') or x.endswith('Wrap') or x.endswith('Drink') or x.endswith('Side'):
            n = len(itemsList)
            if n != 0:
                for i in range(n):
                    if itemsList[i] == x:
                        index = i
                        qtyList[index] += y
                        break
                    else:
                        continue
                if x not in itemsList:
                    itemsList.append(x)
                    qtyList.append(y)
            else:
                itemsList.append(x)
                qtyList.append(y)
        else:
            pass

    elif op == '3':
        print()
        n = len(itemsList)
        if n is not 0:
            cheese = list(0 for x in range(n))
            ice = list(0 for x in range(n))
            for i in range (n):
                if itemsList[i].lower().endswith('burger'):
                    z = input('Do you want extra cheese? (y/n) ')
                    if z == 'y':
                        print()
                        c = int(input('How many cheese slices would you like to have? '))
                        cheese[i] = c
                    else:
                        c = 0
                        cheese[i] = c
                    print()
                elif itemsList[i].lower().endswith('drink'):
                    z = input('Do you want ice in your drink? (With Ice/Without Ice) ')
                    if z == 'With Ice':
                        ice[i] = z
                    else:
                        ice[i] = 0

    elif op == '4':
        print()
        r = input("Enter item's name to be removed: ")
        q = int(input("Enter item's quantity to be removed: "))
        n = len(itemsList)
        if n != 0:
            for i in range(n):
                if itemsList[i] == r:
                    if q <= qtyList[i]:
                        #itemsList.remove(itemsList[i])
                        qtyList[i] -= q
                        if qtyList[i] == 0:
                            itemsList.remove(itemsList[i])
                        else:
                            pass
                        print(q,r,'removed successfully!')
                        break
                    else:
                        print('Cannot remove as you have not ordered', q, r +'!')
                else:
                    continue
        else:
            print('You have not ordered anything yet!')

    elif op == '5':
        print()
        n = len(itemsList)
        if n is not 0:
            for i in range(n):
                if itemsList[i].lower().endswith('burger'):
                    bur.append(br.Burger(itemsList[i],qtyList[i],cheese[i]))

                elif itemsList[i].lower().endswith('wrap'):
                    wrp.append(wr.Wrap(itemsList[i],qtyList[i]))

                elif itemsList[i].lower().endswith('drink'):
                    bev.append(bv.Beverage(itemsList[i],qtyList[i],z))

                else:
                    sid.append(sd.Side(itemsList[i],qtyList[i]))

            price1 = 0
            price2 = 0
            price3 = 0
            price4 = 0
            tPrice = 0

            for i in range(len(bur)):
                price1 += bur[i].calPrice()

            for i in range(len(wrp)):
                price2 += wrp[i].calPrice()

            for i in range(len(bev)):
                price3 += bev[i].calPrice()

            for i in range(len(sid)):
                price4 += sid[i].calPrice()

            tPrice = price1 + price2 + price3 + price4    

            tax = tx.Tax.getTax()
            bill = bl.Bill(tPrice,tax,itemsList,qtyList,cheese,ice)
            bill.calBill()
        else:
            print('Sorry but you need to buy any item first!')

    elif op == '6':
        break

    else:
        print('Invalid option entered!')
        print()
        continue
    print()

    #DOUBTS
    #Need to output amount of cheese (if any)
    #Need to output drink with/without ice
    #If an item is repeated, then print it only once with total quantity
    #Can Objects be over-written?

    #print (itemsList)
    #print (qtyList)

"""n = len(itemsList)
for i in range(0,n-1):
for j in range(i+1,n):
if itemsList[j] == itemsList[i]:  #List index out of range??
qtyList[i] += qtyList[j]
itemsList.remove(itemsList[j])
qtyList.remove(qtyList[j])
else:
continue"""

# check at run time for repetition of items

#make cheese list of range n
#make ice list of range n
#then update their ith values and get the output

