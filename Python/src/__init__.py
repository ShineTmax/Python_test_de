import logging
from pathlib import Path

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("Python_Test_DE_logs")

# Define paths for input files and output
INPUT_DRUGS_PATH = Path("Data/drugs.csv")
INPUT_CLINICAL_TRIALS_PATH = Path("Data/clinical_trials.csv")
INPUT_PUBMED_CSV_PATH = Path("Data/pubmed.csv")
INPUT_PUBMED_JSON_PATH = Path("Data/pubmed.json")
INPUT_FILES = [INPUT_DRUGS_PATH, INPUT_CLINICAL_TRIALS_PATH, INPUT_PUBMED_CSV_PATH, INPUT_PUBMED_JSON_PATH]
OUTPUT_FILEPATH = Path("Results/output.json")
