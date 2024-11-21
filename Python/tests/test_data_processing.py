import unittest
import pandas as pd
from src.data_processing import find_mentions

class TestDataProcessing(unittest.TestCase):
    """
    Unit test class for testing the data processing functions, specifically
    the `find_mentions` function. This class uses the unittest framework to 
    validate the behavior of the `find_mentions` function that identifies 
    mentions of drugs in publication data.

    Methods:
        test_find_mentions: Tests the functionality of the `find_mentions` 
                             function by checking if it correctly identifies 
                             mentions of drugs in the given publication data.
    """

    def test_find_mentions(self):
        """
        Test the `find_mentions` function.

        This test verifies that the `find_mentions` function accurately detects 
        the presence of drug mentions in a set of publication data. It creates 
        sample data for a single drug ("Aspirin") and a publication that mentions 
        it. The test checks that the function returns the expected number of mentions 
        and verifies the drug mentioned.

        Asserts:
            - That the number of mentions found is 1.
            - That the mentioned drug is "Aspirin".
        """
        drugs_df = pd.DataFrame({"drug": ["Aspirin"]})
        publications_df = pd.DataFrame({
            "title": ["Research on Aspirin"],
            "journal": ["Journal A"],
            "date": ["2024-01-01"]
        })
        mentions = find_mentions(drugs_df, publications_df, source="pubmed")
        self.assertEqual(len(mentions), 1)
        self.assertEqual(mentions[0]["drug"], "Aspirin")

if __name__ == '__main__':
    unittest.main()
