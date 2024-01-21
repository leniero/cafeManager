# Create the menu list
menu = ['Espresso', 'Latte', 'Muffin', 'Sandwich']

# Create the stock dictionary
stock = {
    'Espresso': 100,
    'Latte': 50,
    'Muffin': 80,
    'Sandwich': 30
}

# Create the price dictionary
price = {
    'Espresso': 1.5,
    'Latte': 2.5,
    'Muffin': 2.0,
    'Sandwich': 5.0
}

# Function to print the menu items
def print_menu_items(menu_items):
    print("\nMenu Items:")
    for item in menu_items:
        print(f"- {item}")

# Function to print the prices of the items
def print_item_prices(prices):
    print("\nItem Prices:")
    for item, price in prices.items():
        print(f"- {item}: £{price:.2f}")

# Function to print the stock of each item
def print_item_stock(stock):
    print("\nItem Stock:")
    for item, quantity in stock.items():
        print(f"- {item}: {quantity} units")

# Main function to run the program
def main():
    # Initialise the total stock worth
    total_stock_worth = sum(stock[item] * price[item] for item in menu)

    while True:
        print("\nOptions:")
        print("1. Check Menu Items")
        print("2. Check Item Prices")
        print("3. Check Item Stock")
        print("4. Calculate Total Stock Worth")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            print_menu_items(menu)
        elif choice == '2':
            print_item_prices(price)
        elif choice == '3':
            print_item_stock(stock)
        elif choice == '4':
            print(f"\nThe total stock worth is £{total_stock_worth:.2f}")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Ensuring the main function is called when the script is run directly
if __name__ == "__main__":
    main()
