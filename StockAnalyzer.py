import yfinance as yf

def main():
    while True:
        ticker = input("Enter stock ticker symbol (or 'exit' to quit): ").strip()
        if ticker == '':
            print("Please enter a ticker symbol or 'exit' to quit.")
            continue

        if ticker.lower() == 'exit':
            break

        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period="1mo")

            if hist.empty:
                print(f"No data found for ticker symbol '{ticker}'. Please try again.")
                continue

            print(f"\nStock data for {ticker} over the past month:")
            print(hist)

            avg_close = hist['Close'].mean()
            max_close = hist['Close'].max()
            min_close = hist['Close'].min()

            print(f"\nAverage Closing Price: ${avg_close:.2f}")
            print(f"Maximum Closing Price: ${max_close:.2f}")
            print(f"Minimum Closing Price: ${min_close:.2f}\n")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")


if __name__ == '__main__':
    main()