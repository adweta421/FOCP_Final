
print("BPP Pizza Price Calculator")
print("="*25) 


def calculating_total_cost(num_pizzas, is_tuesday, delivery, use_app):

    base_pizza_price =  12
    delivery_cost = 2.50
    app_discount = 0.25
    tuesday_discount = 0.5
    #Calculate the cost of a pizza order
    total_cost = num_pizzas * base_pizza_price

    #Discount if it is tuesday
    if is_tuesday:
            total_cost *= (1 - tuesday_discount)
    else:
        total_cost = num_pizzas * base_pizza_price
        
        
    # Add delivery cost
    if num_pizzas >= 5 and delivery:
        delivery_cost = 0.0
    else:
        total_cost += delivery_cost
        
    #Apply discont for who used app
    if use_app:
        total_cost -= (total_cost * app_discount)
        
    return total_cost
    
    
#Asking the user how many pizzas do they want?
num_pizzas = float(input("How many pizzas ordered?"))

#Asking user they want delivery
delivery = input("Do you want delivery? (yes/no): ").lower() == 'yes'


#Asking user is it tuesday order?
is_tuesday = input("Is it Tuesday? (yes/no): ").lower() == 'yes'


#Asking user do they use the app?
use_app = input("Did the customer use the app ? (yes/no): ").lower() == 'yes'

total_price = calculating_total_cost(num_pizzas, is_tuesday, delivery, use_app)
print(f'Total Price: £{total_price}')
