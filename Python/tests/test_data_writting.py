import unittest
from pathlib import Path
import json
from src.data_writting import write_data_to_json
from tests import OUTPUT_TEST_FILEPATH

class TestDataWriting(unittest.TestCase):

    def test_write_data_to_json(self):
        test_data = [{"drug": "Aspirin", "reference": {"pubmed": []}}]
        write_data_to_json(test_data, OUTPUT_TEST_FILEPATH)
        self.assertTrue(OUTPUT_TEST_FILEPATH.exists())
        with open(OUTPUT_TEST_FILEPATH, 'r') as file:
            data = json.load(file)
            self.assertEqual(data[0]["drug"], "Aspirin")

if __name__ == '__main__':
    unittest.main()
