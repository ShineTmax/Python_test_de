import unittest
import pandas as pd
from src.data_processing import find_mentions

class TestDataProcessing(unittest.TestCase):

    def test_find_mentions(self):
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
