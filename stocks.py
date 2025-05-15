from sys import argv

file_name, balance = argv


# KEY
# new_pd = new price drop
# new_bp = new buying price
# change_p = change in price

def new_size(starting_price, times_brought):
    new_bp = round(starting_price * times_brought, 2)
    return new_bp
    
def price_drop(change_p, times_brought):
    new_pd = change_p * times_brought
    return new_pd

def euro_drop(size_list, new_pd, change_p, times_brought):
    drawdown_value = 0
    decrease_pd = new_pd
    for i in size_list:
        single_buy_change = i * decrease_pd
        drawdown_value += single_buy_change
        decrease_pd -= change_p
    
    return drawdown_value
        
        
starting_price = float(input("Starting buying price: "))
change_p = int(input("What change in price do you want: "))
simulation_end = int(input("How much of a price drop do you want to simulate: "))

times_brought = 1
size_list = []
new_pd = 0

print("\n")
while (new_pd < simulation_end):
    print("-------------------------------------------------")
    new_bp = new_size(starting_price, times_brought)
    size_list += [new_bp]
    
    new_pd = price_drop(change_p, times_brought)
    
    new_drawdown = round(euro_drop(size_list, new_pd, change_p, times_brought), 2)

    
    print(f""" Times brought: {times_brought} \n New buy price to the list: {new_bp} \n All buys in a list: {size_list} \n Current price drop: {new_pd}\n Open drawndown = -€ {new_drawdown}""")
    times_brought += 1
    print("-------------------------------------------------\n")

current_balance = float(balance)
if new_drawdown >= (round((current_balance * 0.4), 2)):
    print(f"Going into -€{new_drawdown} in the drawdown will take you over 40% of €{current_balance}")
    print(f"€{round(current_balance * 0.4, 2)} is the limit\n")
else:
    print(f"You can hold a -€{new_drawdown} with a balance of €{current_balance}")
    print(f"This means you can: \n - Start with {starting_price} buy price \n - Buy the increased {starting_price} at every -{change_p} price change\n")

