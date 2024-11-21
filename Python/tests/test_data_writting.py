import unittest
from pathlib import Path
import json
from src.data_writting import write_data_to_json
from tests import OUTPUT_TEST_FILEPATH

class TestDataWriting(unittest.TestCase):
    """
    Unit test class for testing data writing functions.

    This class tests the function `write_data_to_json`, which is responsible for writing data 
    to a JSON file. The test ensures that the data is correctly written to the specified file 
    and can be successfully loaded from that file.

    Methods:
        test_write_data_to_json: Tests the writing of data to a JSON file by checking if 
                                  the file exists and if the data written is correct.
    """

    def test_write_data_to_json(self):
        """
        Test the writing of data to a JSON file.

        This test ensures that the `write_data_to_json` function correctly writes the provided
        data to a JSON file at the specified path (`OUTPUT_TEST_FILEPATH`). The test checks 
        that the file exists after writing, and verifies that the data written into the file 
        is correct.

        Asserts:
            - The output file exists after writing the data.
            - The data written to the JSON file matches the expected content.
        """
        test_data = [{"drug": "Aspirin", "reference": {"pubmed": []}}]
        write_data_to_json(test_data, OUTPUT_TEST_FILEPATH)

        # Assert that the output file exists
        self.assertTrue(OUTPUT_TEST_FILEPATH.exists())

        # Assert that the data written to the file is correct
        with open(OUTPUT_TEST_FILEPATH, 'r') as file:
            data = json.load(file)
            self.assertEqual(data[0]["drug"], "Aspirin")

if __name__ == '__main__':
    unittest.main()
