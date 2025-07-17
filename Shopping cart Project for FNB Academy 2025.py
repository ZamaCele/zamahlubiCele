#shopping cart


foods =[]
price =[]
total =0

while True:
    food = input("enter a food to buy or press q to quit")
    if food.lower == 'q':
        break
    else:
        prices = float (input(f"enter the price of the {food}:R"))
        foods.append(food)
        prices.append(price)
        
print("......YOUR CART.....")
for food in foods:
    print(food)
    
    for price in prices:
        total = total + price
    
    print("\n")
    print(f"your total is: R{total}")
    
    