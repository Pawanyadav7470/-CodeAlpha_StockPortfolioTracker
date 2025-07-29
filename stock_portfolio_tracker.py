# Predefined Indian stock prices (in INR)
stock_prices = {
    "RELIANCE": 2800,
    "TCS": 3900,
    "INFY": 1500,
    "HDFCBANK": 1600,
    "ITC": 450,
    "HCLTECH": 1700,
    "SBIN": 780
}

portfolio = {}
total = 0

print("📈 Welcome to Indian Stock Tracker!")
print("Available Stocks:", ', '.join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or type 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("❌ Stock not found. Try again.")
        continue

    try:
        qty = int(input(f"Enter quantity of {stock}: "))
    except:
        print("❌ Please enter a valid number.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + qty
    cost = stock_prices[stock] * qty
    total += cost
    print(f"✅ Added {qty} shares of {stock} — ₹{cost}")

# Show summary
print("\n📊 Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    print(f"{stock}: {qty} x ₹{price} = ₹{value}")

print(f"\n💰 Total Investment: ₹{total}")

# Save to CSV
save = input("\nDo you want to save this to file? (yes/no): ").lower()
if save == "yes":
    name = input("Enter file name: ")
    with open(name + ".csv", "w", encoding="utf-8") as f:
        f.write("Stock,Quantity,Price,Value\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            f.write(f"{stock},{qty},{price},{value}\n")
        f.write(f"\nTotal,,,{total}")
    import os
    print(f"📁 File saved as {name}.csv at: {os.getcwd()}")
