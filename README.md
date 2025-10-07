# 📈 Stock Snapshot Analyzer

A simple Python tool that pulls real-time stock data using Yahoo Finance, analyzes trends, and outputs a clean summary. Designed for business analysts, students, and strategic thinkers who want fast, interpretable insights without complex dashboards.

---

## 🚀 Features

- Command-line interface for entering stock ticker symbols
- Pulls 1-month historical data using the `yfinance` API
- Calculates:
  - Average closing price
  - Maximum and minimum closing prices
- Flags invalid or missing ticker symbols
- Clean output for quick decision-making

---

## 🧪 Example Output

Enter stock ticker symbol (or 'exit' to quit): MSFT

Stock data for MSFT over the past month:

Average Closing Price: $325.42 Maximum Closing Price: $332.10 Minimum Closing Price: $312.87


---

## 📦 Requirements

- Python 3.7+
- `yfinance` library

Install dependencies:

```bash
pip install yfinance



