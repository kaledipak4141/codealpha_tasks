# Stock Portfolio Tracker

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 200,
    "MSFT": 300
}

total_value = 0

print("=== Stock Portfolio Tracker ===")
print("Available Stocks:")

for stock, price in stocks.items():
    print(f"{stock}: ${price}")

num_stocks = int(input("\nHow many different stocks do you own? "))

for i in range(num_stocks):
    stock_name = input("\nEnter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stocks:
        value = stocks[stock_name] * quantity
        total_value += value
        print(f"Value of {stock_name}: ${value}")
    else:
        print("Stock not available in database!")

print("\n=== Portfolio Summary ===")
print("Total Investment Value: $", total_value)

# Save result to file
with open("portfolio_summary.txt", "w") as file:
    file.write(f"Total Investment Value: ${total_value}")

print("Portfolio summary saved in portfolio_summary.txt")