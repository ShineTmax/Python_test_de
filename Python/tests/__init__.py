from pathlib import Path

# Define paths for input files and output
INPUT_DRUGS_TEST_PATH = Path("Data_test/drugs.csv")
INPUT_CLINICAL_TRIALS_TEST_PATH = Path("Data_test/clinical_trials.csv")
INPUT_PUBMED_CSV_TEST_PATH = Path("Data_test/pubmed.csv")
INPUT_PUBMED_JSON_TEST_PATH = Path("Data_test/pubmed.json")
INPUT_TEST_FILES = [INPUT_DRUGS_TEST_PATH, INPUT_CLINICAL_TRIALS_TEST_PATH, INPUT_PUBMED_CSV_TEST_PATH, INPUT_PUBMED_JSON_TEST_PATH]
OUTPUT_TEST_FILEPATH = Path("Data_test/output.json")
