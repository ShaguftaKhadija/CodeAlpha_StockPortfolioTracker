import csv
from datetime import datetime
from pathlib import Path


# Sample stock prices for educational purposes.
# These are NOT live market prices.
STOCKS = {
    "AAPL": {"name": "Apple", "price": 180.00},
    "GOOGL": {"name": "Alphabet", "price": 140.00},
    "MSFT": {"name": "Microsoft", "price": 420.00},
    "AMZN": {"name": "Amazon", "price": 185.00},
    "TSLA": {"name": "Tesla", "price": 250.00},
    "NVDA": {"name": "NVIDIA", "price": 120.00},
    "META": {"name": "Meta Platforms", "price": 500.00}
}


def show_banner():
    print("\n" + "=" * 65)
    print("                  STOCK PORTFOLIO TRACKER")
    print("=" * 65)
    print("Track your sample stock investments using Python.")
    print("IMPORTANT: Prices are illustrative, not live market prices.")
    print("=" * 65)


def show_available_stocks():
    print("\n" + "-" * 60)
    print(f"{'SYMBOL':<12}{'COMPANY':<28}{'PRICE (USD)':>15}")
    print("-" * 60)

    for symbol, details in STOCKS.items():
        print(
            f"{symbol:<12}"
            f"{details['name']:<28}"
            f"${details['price']:>14,.2f}"
        )

    print("-" * 60)


def get_positive_quantity(message):
    """Accept only positive whole-number quantities."""

    try:
        quantity = int(input(message).strip())

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return None

        return quantity

    except ValueError:
        print("Invalid input! Please enter a positive whole number.")
        return None


def add_stock(portfolio):
    show_available_stocks()

    symbol = input("\nEnter stock symbol: ").strip().upper()

    if symbol not in STOCKS:
        print("Stock not found. Please select a symbol from the list.")
        return

    quantity = get_positive_quantity("Enter quantity to add: ")

    if quantity is None:
        return

    portfolio[symbol] = portfolio.get(symbol, 0) + quantity

    price = STOCKS[symbol]["price"]
    company = STOCKS[symbol]["name"]
    value_added = price * quantity

    print("\nStock added successfully!")
    print(f"Company: {company}")
    print(f"Shares added: {quantity}")
    print(f"Price per share: ${price:,.2f}")
    print(f"Estimated value added: ${value_added:,.2f}")
    print(f"Total shares owned: {portfolio[symbol]}")


def view_portfolio(portfolio):
    if not portfolio:
        print("\nYour portfolio is empty. Add a stock first!")
        return

    print("\n" + "=" * 85)
    print("                         YOUR STOCK PORTFOLIO")
    print("=" * 85)

    print(
        f"{'SYMBOL':<10}"
        f"{'COMPANY':<23}"
        f"{'QUANTITY':>10}"
        f"{'PRICE (USD)':>17}"
        f"{'TOTAL (USD)':>20}"
    )

    print("-" * 85)

    total_value = 0.0
    total_shares = 0

    for symbol, quantity in portfolio.items():
        details = STOCKS[symbol]
        price = details["price"]
        value = price * quantity

        total_value += value
        total_shares += quantity

        print(
            f"{symbol:<10}"
            f"{details['name']:<23}"
            f"{quantity:>10}"
            f"${price:>16,.2f}"
            f"${value:>19,.2f}"
        )

    print("-" * 85)
    print(f"Total number of shares: {total_shares}")
    print(f"Total portfolio value: ${total_value:,.2f}")
    print("=" * 85)


def remove_stock(portfolio):
    if not portfolio:
        print("\nYour portfolio is empty.")
        return

    view_portfolio(portfolio)

    symbol = input(
        "\nEnter the stock symbol to remove: "
    ).strip().upper()

    if symbol not in portfolio:
        print("That stock is not in your portfolio.")
        return

    quantity = get_positive_quantity("Enter quantity to remove: ")

    if quantity is None:
        return

    if quantity > portfolio[symbol]:
        print(
            f"You own only {portfolio[symbol]} shares of {symbol}."
        )
        print("You cannot remove more shares than you own.")
        return

    portfolio[symbol] -= quantity

    if portfolio[symbol] == 0:
        del portfolio[symbol]

    print(f"\nSuccessfully removed {quantity} shares of {symbol}.")

    if symbol in portfolio:
        print(f"Remaining shares: {portfolio[symbol]}")
    else:
        print(f"You no longer own any shares of {symbol}.")


def export_portfolio(portfolio):
    if not portfolio:
        print("\nYour portfolio is empty. Nothing to export.")
        return

    filename = Path("my_stock_portfolio.csv")

    try:
        with filename.open(
            "w", newline="", encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Stock Symbol",
                "Company",
                "Quantity",
                "Price per Share (USD)",
                "Total Value (USD)"
            ])

            grand_total = 0.0

            for symbol, quantity in portfolio.items():
                details = STOCKS[symbol]
                price = details["price"]
                value = price * quantity

                grand_total += value

                writer.writerow([
                    symbol,
                    details["name"],
                    quantity,
                    f"{price:.2f}",
                    f"{value:.2f}"
                ])

            writer.writerow([])
            writer.writerow([
                "Exported At",
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ])
            writer.writerow(["", "", "", "Grand Total", f"{grand_total:.2f}"])

        print("\nPortfolio exported successfully!")
        print(f"File name: {filename.resolve()}")
        print(f"Total portfolio value: ${grand_total:,.2f}")

    except OSError as error:
        print(f"\nUnable to save the CSV file: {error}")


def main():
    portfolio = {}

    show_banner()

    while True:
        print("\n============= MAIN MENU =============")
        print("1. View Available Stocks")
        print("2. Add Stock to Portfolio")
        print("3. View My Portfolio")
        print("4. Remove Stock from Portfolio")
        print("5. Export Portfolio to CSV")
        print("6. Exit")
        print("=====================================")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            show_available_stocks()

        elif choice == "2":
            add_stock(portfolio)

        elif choice == "3":
            view_portfolio(portfolio)

        elif choice == "4":
            remove_stock(portfolio)

        elif choice == "5":
            export_portfolio(portfolio)

        elif choice == "6":
            print("\nThank you for using Stock Portfolio Tracker!")
            print("Keep learning and building great projects!")
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()