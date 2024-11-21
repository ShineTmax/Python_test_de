import pandas as pd
import chardet
import json
from src import logger
from pathlib import Path


def read_csv_file(file_path: Path) -> pd.DataFrame:
    """
    Read a CSV file and return it as a DataFrame.
    Args:
        file_path (Path): Path to the CSV file.
    Returns:
        pd.DataFrame: CSV data as DataFrame, or empty DataFrame if an error occurs.
    """
    try:
        data = pd.read_csv(file_path, encoding="utf-8")
        return data
    except Exception as e:
        logger.error(f"An error occurred while reading '{file_path}': {e}")
        return pd.DataFrame()  # Return empty DataFrame on error


def read_json_file(file_path: Path) -> pd.DataFrame:
    """
    Read a JSON file and return it as a DataFrame.
    Args:
        file_path (Path): Path to the JSON file.
    Returns:
        pd.DataFrame: JSON data as DataFrame, or empty DataFrame if an error occurs.
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return pd.DataFrame(data)
    except Exception as e:
        logger.error(f"An error occurred while reading '{file_path}': {e}")
        return pd.DataFrame()  # Return empty DataFrame on error


def read_data(input_files: list[Path]) -> list[pd.DataFrame]:
    """
    Read a list of CSV and JSON files into DataFrames.
    Args:
        input_files (list[Path]): List of file paths to read.
    Returns:
        list[pd.DataFrame]: List of DataFrames corresponding to the input files.
    """
    logger.info("Input files: %s", input_files)
    data = []
    for file_path in input_files:
        if file_path.suffix == ".csv":
            df = read_csv_file(file_path)
        elif file_path.suffix == ".json":
            df = read_json_file(file_path)
        else:
            continue
        data.append(df)
    return data
