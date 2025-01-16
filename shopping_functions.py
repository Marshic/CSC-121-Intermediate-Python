# Donte' Brown 
# 1/16/2025
# M2Lab
# Use functions to simulate shopping

# Create the function to determine if the item exists
def if_item_exists(item):
    '''
    Function takes in one string. If that sting exists in a list
    return true, if the string not in list, return False.
    '''
    store_items = ["very illegal catnip", "catnip omega", "catnip ultra", "catnip plus", "cat jeans", "cat shoes"]

    if item in store_items:
        return True
    else:
        return False
    
def getCost(item, quantity):
    '''
    Function takes in an item as a string and a quantity as an integer.
    Function calculate the cost using a dictionary and return the total cost
    '''
    item_prices = {"very illegal catnip":99.99, "catnip omega":10.99, "catnip ultra":70.99, "catnip plus":65.00, "cat jeans":30.00,"cat shoes":69.42}

    # Get the cost of the item from the dictionary
    item_costs = item_prices[item]
    total_cost = item_costs * quantity
    return total_cost


# Define the main function
def main():
    # Call all our other functions
    print("Welcome to Cat-Co!!!")
    
    run_again = "yes"
    
    final_cost = 0

    while run_again == "yes":
        
        # Get an item from user
        user_item = input("What would you like to purchase: ")

        if if_item_exists(user_item) == True:
            quantity = int(input(f"How many {user_item}s will you buy? "))
            final_cost  = final_cost + getCost(user_item, quantity)
        else:
            print("That item does not exist!")
    
        run_again == input("Will you add more items? ")
    
        print(f"${final_cost:.2f}")
# Call the main function
if __name__ == "__main__":
    main()
