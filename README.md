# 📈 Stock Portfolio Tracker

A simple, menu-driven **Stock Portfolio Tracker built with Python** as part of the CodeAlpha Python Programming Internship. This project allows users to manage sample stock investments, calculate portfolio values, remove shares, and export portfolio details to a CSV file.

## 📌 About the Project

The Stock Portfolio Tracker is a beginner-friendly Python application designed to demonstrate fundamental programming concepts through a practical financial tracking project.

Users can view available stocks and their sample prices, add shares to their portfolio, monitor their holdings, remove shares, and export their portfolio information for future reference.

**Note:** This application uses predefined sample stock prices for educational purposes. It does not fetch live stock-market data or provide financial advice.

## ✨ Features

- **View Available Stocks:** Display stock symbols, company names, and sample prices.
- **Add Stocks:** Add shares of available companies to your portfolio.
- **View Portfolio:** See your holdings, share quantities, prices, and individual stock values.
- **Calculate Portfolio Value:** Automatically calculate the combined value of all stocks in your portfolio.
- **Remove Stocks:** Remove shares from your holdings with quantity validation.
- **Export to CSV:** Save portfolio details and the total portfolio value in a CSV file.
- **Input Validation:** Handle invalid menu choices, incorrect quantities, and unavailable stock symbols.
- **User-Friendly Menu:** Navigate the application through a simple terminal interface.

## 🛠️ Technologies Used

- **Python 3**
- `csv` module — Export portfolio data to a CSV file.
- `datetime` module — Record the export date and time.
- `pathlib` module — Work with file paths.
- Dictionaries — Store stock information and portfolio quantities.
- Functions — Organize the program into reusable components.
- Exception Handling — Handle invalid inputs and file-related errors.

## 📂 Project Structure

```text
CodeAlpha_StockPortfolio/
│
├── stock_tracker.py
└── README.md
```

After exporting your portfolio, the following file will also be created:

```text
my_stock_portfolio.csv
```

## ⚙️ Installation and Setup

### Prerequisites

- Python 3 installed on your computer.
- A code editor such as Visual Studio Code.

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### Step 2: Open the Project Folder

```bash
cd CodeAlpha_StockPortfolio
```

### Step 3: Run the Application

```bash
python stock_tracker.py
```

If your system uses the Python launcher, you can also try:

```bash
py stock_tracker.py
```

No additional Python packages are required because the project uses Python's built-in modules.

## 🚀 How to Use

When the program starts, a menu appears with the following options:

| Option | Function |
|---|---|
| 1 | View Available Stocks |
| 2 | Add Stock to Portfolio |
| 3 | View My Portfolio |
| 4 | Remove Stock from Portfolio |
| 5 | Export Portfolio to CSV |
| 6 | Exit the Application |

### Example Workflow

1. Select **1** to view the available stocks.
2. Select **2
