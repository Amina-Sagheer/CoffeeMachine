from resources import resources
from resources import MENU


def payment():
    """
       Handles the payment process for the user's order.

       Prompts the user to insert coins until the total amount received
       is sufficient to cover the cost of the chosen drink. Accepts
       coins in the form of pennies, nickles, dimes, and quarters.

       Returns:
           None
       """
    print(f"Your total is {MENU[user_input]['cost']}")
    amount_received = 0
    while amount_received<MENU[user_input]['cost']:
        amount = input("Please insert the coins.").lower()
        list = amount.split(' ')
        for coins in list:
            if coins == 'pennies':
                amount_received = amount_received + 0.01
            if coins == 'dimes':
                amount_received = amount_received + 0.10
            if coins == 'quarters':
                amount_received = amount_received + 0.25
            if coins == 'nickles':
                amount_received = amount_received + 0.05

        if amount_received < MENU[user_input]['cost']:
            print(f"Not enough money. You still need to pay {MENU[user_input]['cost']-amount_received:.2f} more.")

    if amount_received > MENU[user_input]['cost']:
        print ("Great!")
        print(f"Transaction was successful.\nHere is your {user_input} and {amount_received- MENU[user_input]['cost']:.2f} change.")
    else:
        print(f"Perfect.\nTransaction was successful.Here is your {user_input}.")

def order(order_name):
    """
        Processes the user's order and updates the resource quantities.

        Checks if there are sufficient resources to fulfill the order.
        If so, it proceeds with the payment and updates the resource
        quantities accordingly.

        Args:
            order_name (str): The name of the drink the user wants to order.

        Returns:
            dict: Updated resource quantities after fulfilling the order.
            bool: False if there are not enough resources.
        """
    if MENU[user_input]['ingredients']['water'] > resources['water'] or MENU[user_input]['ingredients']['milk'] > resources['milk'] or MENU[user_input]['ingredients']['coffee'] > resources['coffee']:
        print("Sorry we don't have enough ingredients")
        return False
    else:
        payment()
        if order_name == 'espresso':
            updated_resources = {
                "water": 300 - 50,
                "milk": 200,
                "coffee": 100 - 18
            }
        elif order_name == 'latte':
            updated_resources = {
                "water": 300 - 200,
                "milk": 200 - 150,
                "coffee": 100 - 24
            }
        elif order_name == 'cappuccino':
            updated_resources = {
                "water": 300 - 250,
                "milk": 200 - 100,
                "coffee": 100 - 24
            }
        else:
            print("Invalid choice!")

        return updated_resources

while resources:
    user_input = (input("What would you like? (espresso/latte/cappuccino): ")).lower()
    if user_input in MENU:
        if not order(user_input):
            break
    else:
        print("Invalid choice! Please choose 'espresso', 'latte', or 'cappuccino'.")

