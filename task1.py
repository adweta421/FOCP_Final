# Adding constant as given in the questions
pizza_price = 12  
tuesday_discount = 0.5
delivery_charge = 2.50
app_discount = 0.25

# Function to get user input with validation for positive integers

def get_input(prompt):
    """Get positive integer input from the user.

    Args:
        prompt (str): Prompt to display to the user.

    Returns:
        int: Positive integer entered by the user.
    """
    while True:
        try:
            val = int(input(prompt))
            if val > 0:
                return val
            else:
             print("Please enter a positive number!")
        except ValueError:
            print("Please enter a number!")
            
            
  # Function to get yes or no input from the user
    
def get_yes_no(prompt):
    """Get yes or no input from the user

    Args:
        prompt (str): Prompt to dispaly to the user

    Returns:
        bool: True if 'y' is entered, False if 'n' is entered.
    """

    while True:
        val = input(prompt).lower()
        if val == 'y':
            return True
        elif val == 'n':
            return False
        else:
            print("Please enter Y or N")
      
def calculate_price(num_pizzas, is_tuesday, delivery, used_app):
    """Calculate the total price of the pizzas.

    Args:
        num_pizzas (int): Number of pizzas ordered.
        is_tuesday (bool): True if it is Tuesday, False otherwise.
        delivery (bool): True if delivery is required, False otherwise.
        used_app (bool): True if the customer used the app, False otherwise.

    Returns:
        float: Total price of the pizzas after applying discounts and charges.
    """
    
    #To calculate total prize
    total = num_pizzas * pizza_price
  
    #Applying discount if it is tuesday
    if is_tuesday:
        total *= tuesday_discount
    
    #Applying discount if it is delivery and if the pizza is more than 4 the delivery price is 0
    if delivery:
        if num_pizzas < 5:
            total += delivery_charge
        
    #Applying discount if app is used 
    if used_app:
        total *= (1 - app_discount)
        
        
    return round(total)

#Main program starts here
print("BPP Pizza Price Calculator")
print("="*26)

#Asking user how many pizza they want
num_pizzas = get_input("How many pizzas ordered? ")

#Asking user if delivery i srequired
delivery = get_yes_no("Is delivery required? ")  

#Asking if they are ordering tuesday
is_tuesday = get_yes_no("Is it Tuesday?")

#Asking user if they have used app to order pizzas
used_app = get_yes_no("Did the customer use the app?")

#Calculating total price of pizzas after asking the users
total = calculate_price(num_pizzas, is_tuesday, delivery, used_app)

#Getting total price in £(pound)
print(f"\nTotal Price: £{total:.2f}")