# Coffee Machine Project!
<p align="center">
  <img src="https://github.com/Amina-Sagheer/Coffee_Machine/assets/172102325/898e61ee-fb4c-4dab-bbaa-10d036f740b1">
</p>


This script simulates a coffee vending machine. Users can order various types of coffee, make payments,
and receive their drinks, with the machine managing the resources and payment process.

### Features:
- **Order Management**: Users can order 'espresso', 'latte', or 'cappuccino'.
- **Payment Handling**: Accepts payments in the form of 'pennies', 'nickels', 'dimes', and 'quarters'.
- **Resource Management**: Tracks and updates the quantities of 'water', 'milk', and 'coffee'.
- **Transaction Feedback**: Informs users of payment status and provides change if necessary.

### Usage:
1. **Run the script:**
    ```bash
    python main.py
    ```

2. **Follow the prompts:**
    - Choose a drink: 'espresso', 'latte', or 'cappuccino'.
    - Insert coins until the total amount received is sufficient to cover the cost of the chosen drink.

#### Example:
**Valid Order with Sufficient Resources**

**Input:**
- Drink: 'latte'
- Coins: 'quarters quarters quarters quarters'

**Expected Output:**
Your total is $2.50
Please insert the coins: quarters quarters quarters quarters

Great!
Transaction was successful.
Here is your latte and $0.50 change.
Resources after transaction: {'water': 100, 'milk': 50, 'coffee': 76}

#### Order with Insufficient Resources
**Input:**
- Drink: 'cappuccino'

**Expected Output:**
Sorry, we don't have enough ingredients

#### Handling of Coin Inputs for Payment
**Input:**
- Drink: 'espresso'
- Coins: 'nickels dimes'

**Expected Output:**
Your total is $1.50
Please insert the coins: nickels dimes

Not enough money. You still need to pay $1.35 more.

#### Invalid Drink Order
**Input:**
- Drink: 'tea'

**Expected Output:**
Invalid choice!
