import unittest
from src.data_reading import read_csv_file, read_json_file
from pathlib import Path
import pandas as pd
from tests import INPUT_DRUGS_TEST_PATH, INPUT_PUBMED_JSON_TEST_PATH

class TestDataReading(unittest.TestCase):

    def test_read_csv_file(self):
        file_path = Path(INPUT_DRUGS_TEST_PATH)
        data = read_csv_file(file_path)
        self.assertIsInstance(data, pd.DataFrame)
        self.assertFalse(data.empty)

    def test_read_json_file(self):
        file_path = Path(INPUT_PUBMED_JSON_TEST_PATH)
        data = read_json_file(file_path)
        self.assertIsInstance(data, pd.DataFrame)
        self.assertFalse(data.empty)

if __name__ == '__main__':
    unittest.main()
