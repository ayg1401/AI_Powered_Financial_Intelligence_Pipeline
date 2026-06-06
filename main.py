from ingestion.fetch_stock_data import fetch_stock_data
from transformation.clean_stock_data import clean_stock_data


def run_pipeline():
    ticker = "RELIANCE.NS"

    raw_file_path = fetch_stock_data(
        ticker=ticker,
        period="6mo",
        interval="1d"
    )

    processed_file_path = clean_stock_data(
        input_path=raw_file_path,
        ticker=ticker
    )

    print("Pipeline completed successfully.")
    print(f"Final output: {processed_file_path}")


if __name__ == "__main__":
    run_pipeline()