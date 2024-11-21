import unittest
from src.data_reading import read_csv_file, read_json_file
from pathlib import Path
import pandas as pd
from tests import INPUT_DRUGS_TEST_PATH, INPUT_PUBMED_JSON_TEST_PATH

class TestDataReading(unittest.TestCase):
    """
    Unit test class for testing data reading functions.

    This class tests the functions `read_csv_file` and `read_json_file` that are responsible
    for reading data from CSV and JSON files, respectively. The tests ensure that the data
    returned by these functions is a valid Pandas DataFrame and is not empty.

    Methods:
        test_read_csv_file: Tests the reading of a CSV file and ensures the result is a
                             non-empty Pandas DataFrame.
        test_read_json_file: Tests the reading of a JSON file and ensures the result is a
                              non-empty Pandas DataFrame.
    """

    def test_read_csv_file(self):
        """
        Test the reading of a CSV file.

        This test ensures that the `read_csv_file` function correctly reads the CSV file from the
        path specified in `INPUT_DRUGS_TEST_PATH`. The test checks that the output is a Pandas 
        DataFrame and that the DataFrame is not empty.

        Asserts:
            - The result is a Pandas DataFrame.
            - The DataFrame is not empty.
        """
        file_path = Path(INPUT_DRUGS_TEST_PATH)
        data = read_csv_file(file_path)
        self.assertIsInstance(data, pd.DataFrame)  # Check if the result is a DataFrame
        self.assertFalse(data.empty)  # Check if the DataFrame is not empty

    def test_read_json_file(self):
        """
        Test the reading of a JSON file.

        This test ensures that the `read_json_file` function correctly reads the JSON file from the
        path specified in `INPUT_PUBMED_JSON_TEST_PATH`. The test checks that the output is a Pandas
        DataFrame and that the DataFrame is not empty.

        Asserts:
            - The result is a Pandas DataFrame.
            - The DataFrame is not empty.
        """
        file_path = Path(INPUT_PUBMED_JSON_TEST_PATH)
        data = read_json_file(file_path)
        self.assertIsInstance(data, pd.DataFrame)  # Check if the result is a DataFrame
        self.assertFalse(data.empty)  # Check if the DataFrame is not empty

if __name__ == '__main__':
    unittest.main()
