cost_price=int(input("enter a cost price:"))
selling_price=int(input("enter a selling price:"))

if(cost_price < selling_price):
    print("profit")
    profit=(selling_price - cost_price)
    print(profit)
    
elif(selling_price == cost_price):
    print("no profit or loss")   
    
else:
    print("loss") 
    loss=(selling_price - cost_price) 
    print(loss)  