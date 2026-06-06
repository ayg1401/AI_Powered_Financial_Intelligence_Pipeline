import pandas as pd
from pathlib import Path


def clean_stock_data(input_path: str, ticker: str) -> str:
    """
    Clean raw stock data and save processed CSV.
    """

    output_dir = Path("data/processed")
    output_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(input_path)

    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    df = df.dropna()

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])

    df["ticker"] = ticker

    output_path = output_dir / f"{ticker}_processed.csv"
    df.to_csv(output_path, index=False)

    print(f"Processed data saved to: {output_path}")
    return str(output_path)