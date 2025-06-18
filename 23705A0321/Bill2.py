prices = {"banana" : 40 , "milk" : 50 , "mango" : 60 , "chicken" : 250}
itemslist = list(map(str , input().split()))
billcost = 0
for i in range(len(itemslist)):
    item = itemslist[i]
    print(item)
    if item in prices:
        billcost = billcost + prices[item]
        print(billcost , item)
print(billcost)