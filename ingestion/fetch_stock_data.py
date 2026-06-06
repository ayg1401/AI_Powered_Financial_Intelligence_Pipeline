import yfinance as yf
from pathlib import Path


def fetch_stock_data(ticker: str, period: str = "6mo", interval: str = "1d") -> str:
    """
    Fetch stock market data from Yahoo Finance and save it as CSV.
    """

    output_dir = Path("data/raw")
    output_dir.mkdir(parents=True, exist_ok=True)

    df = yf.download(ticker, period=period, interval=interval)

    if df.empty:
        raise ValueError(f"No data found for ticker: {ticker}")

    output_path = output_dir / f"{ticker}_raw.csv"
    df.to_csv(output_path)

    print(f"Raw data saved to: {output_path}")
    return str(output_path)