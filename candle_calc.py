# Donte Brown
# 1/14/25
# M1Lab
# Calculate cost of item based on quantity

'''
Get number of candles they'll purchase from user
If num_candles is between 1 - 19, cost per item is $4.75
If num_candles is between 20 - 49, cost per item is $4.50
If num_candles is between 50 - 99, cost per item is $4.25
If num_candles is greater than or equal to 100, cost per item is $4.00
Create variable for total (num_candles * cost per item) and display to user
'''
run_again = "yes"

# While loop begins here
while run_again == "yes":
    # Get number of candles from user
    num_candles = int(input("How many candles will you buy: "))
    # If/else to determine cost per candle
    if num_candles > 0 and num_candles < 20:
        cost_per_item = 4.75
    elif num_candles > 19 and num_candles < 50:
        cost_per_item = 4.50
    elif num_candles > 49 and num_candles < 100:
        cost_per_item = 4.25
    elif num_candles >= 100:
        cost_per_item = 4.00
    else:
        cost_per_item = 0
        print("Error, invalid amount of candles.")
    #Display info to user
    print("\n\n\n")
    print("*" * 30)
    print(f"Number of candles: {num_candles}")
    print(f"Cost per item: {cost_per_item}")
    print(f"Total: ${(cost_per_item * num_candles):.2f}")
    # Ask user to run again
    run_again = input("Would you like to run again?: ")

print("Program has been terminated.")