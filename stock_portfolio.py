# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 350,
    "AMZN": 150
}

portfolio = {}
total_investment = 0

n = int(input("Enter number of stocks: "))

for i in range(n):
    stock = input("Enter Stock Name: ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter Quantity: "))
        portfolio[stock] = quantity
    else:
        print("Stock not available!")

print("\n------ Portfolio Summary ------")

for stock, quantity in portfolio.items():
    investment = stock_prices[stock] * quantity
    total_investment += investment

    print(f"{stock} - Quantity: {quantity}, Price: ${stock_prices[stock]}, Investment: ${investment}")

print("\nTotal Investment =", total_investment)

# Save Result in Text File
file = open("portfolio.txt", "w")

file.write("Stock Portfolio Summary\n")
file.write("--------------------------\n")

for stock, quantity in portfolio.items():
    investment = stock_prices[stock] * quantity
    file.write(f"{stock} | Qty: {quantity} | Investment: ${investment}\n")

file.write(f"\nTotal Investment = ${total_investment}")

file.close()

print("\nPortfolio saved successfully in portfolio.txt")
