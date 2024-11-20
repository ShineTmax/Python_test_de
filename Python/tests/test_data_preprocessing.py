import unittest
import pandas as pd
from src.data_reading import read_csv_file, read_json_file
from src.data_preprocessing import clean_drugs, clean_clinical_trials
from tests import INPUT_DRUGS_TEST_PATH, INPUT_CLINICAL_TRIALS_TEST_PATH

class TestDataPreprocessing(unittest.TestCase):

    def test_clean_drugs(self):
        test_data = read_csv_file(INPUT_DRUGS_TEST_PATH)
        cleaned_data = clean_drugs(test_data)
        self.assertTrue((cleaned_data["atccode"] == cleaned_data["atccode"].str.lower()).all())
        self.assertTrue((cleaned_data["drug"] == cleaned_data["drug"].str.lower()).all())

    def test_clean_clinical_trials(self):
        test_data = read_csv_file(INPUT_CLINICAL_TRIALS_TEST_PATH)
        cleaned_data = clean_clinical_trials(test_data)
        self.assertFalse(cleaned_data["title"].str.contains("\\\\").any())

if __name__ == '__main__':
    unittest.main()
