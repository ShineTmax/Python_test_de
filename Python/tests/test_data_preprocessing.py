import unittest
import pandas as pd
from src.data_reading import read_csv_file, read_json_file
from src.data_preprocessing import clean_drugs, clean_clinical_trials
from tests import INPUT_DRUGS_TEST_PATH, INPUT_CLINICAL_TRIALS_TEST_PATH

class TestDataPreprocessing(unittest.TestCase):
    """
    Unit test class for testing the data preprocessing functions.
    Specifically, this class tests the cleaning functions for drug data and clinical trials data.
    It uses the unittest framework to validate the expected behavior of these functions.

    Methods:
        test_clean_drugs: Tests the cleaning of drug data by verifying that
                           the 'atccode' and 'drug' columns contain only lowercase values.
                           Asserts:
                               - The 'atccode' column contains only lowercase values.
                               - The 'drug' column contains only lowercase values.
        test_clean_clinical_trials: Tests the cleaning of clinical trials data by checking that
                                     the 'title' column does not contain backslashes ('\\').
                                     Asserts:
                                         - The 'title' column does not contain backslashes ('\\').
    """

    def test_clean_drugs(self):
        """
        Test the cleaning process for drug data.

        This test ensures that after cleaning, the 'atccode' and 'drug' columns of the drug data
        contain only lowercase values. It reads the drug data from the CSV file specified in 
        INPUT_DRUGS_TEST_PATH, applies the `clean_drugs` function, and asserts that both columns 
        are fully lowercase.

        Asserts:
            - The 'atccode' column contains only lowercase values.
            - The 'drug' column contains only lowercase values.
        """
        test_data = read_csv_file(INPUT_DRUGS_TEST_PATH)
        cleaned_data = clean_drugs(test_data)
        self.assertTrue((cleaned_data["atccode"] == cleaned_data["atccode"].str.lower()).all())
        self.assertTrue((cleaned_data["drug"] == cleaned_data["drug"].str.lower()).all())

    def test_clean_clinical_trials(self):
        """
        Test the cleaning process for clinical trials data.

        This test ensures that after cleaning, the 'title' column of the clinical trials data
        does not contain any backslashes ('\\'). It reads the clinical trials data from the 
        CSV file specified in INPUT_CLINICAL_TRIALS_TEST_PATH, applies the `clean_clinical_trials`
        function, and asserts that there are no backslashes in the 'title' column.

        Asserts:
            - The 'title' column does not contain backslashes ('\\').
        """
        test_data = read_csv_file(INPUT_CLINICAL_TRIALS_TEST_PATH)
        cleaned_data = clean_clinical_trials(test_data)
        self.assertFalse(cleaned_data["title"].str.contains("\\\\").any())

if __name__ == '__main__':
    unittest.main()
