# Project Overview
This project is designed to analyze and process data related to drugs, clinical trials, and publications. It includes functionality for reading, processing, and extracting insights from datasets stored in CSV and JSON formats.

## Project Structure
``` 
.
├── Data
│   ├── clinical_trials.csv       # Clinical trial data
│   ├── drugs.csv                 # Drug information
│   ├── pubmed.csv                # PubMed publications in CSV format
│   └── pubmed.json               # PubMed publications in JSON format
├── Data_test
│   ├── (Test datasets for validation)
├── Python
│   ├── __init__.py
│   ├── ad_hoc                    # Ad-hoc analysis scripts
│   │   └── bonus.py
│   ├── main.py                   # Main entry point for running the project
│   ├── src                       # Core processing logic
│   │   ├── data_preprocessing.py # Data cleaning and preprocessing
│   │   ├── data_processing.py    # Processing and transformation
│   │   ├── data_reading.py       # Functions to read input data
│   │   └── data_writting.py      # Functions to save processed results
│   └── tests                     # Unit tests for core functionality
├── Results
│   └── output.json               # Generated output from the processing pipeline
├── SQL
│   ├── python                    # Python scripts for SQL-related operations
│   │   ├── query_1.py
│   │   └── query_2.py
│   └── sql                       # SQL query files
│       ├── query_1.sql
│       └── query_2.sql
├── poetry.lock                   # Dependency lock file
├── pyproject.toml                # Project dependencies and metadata
├── pytest.ini                    # Configuration for Pytest
├── readme.md                     # Project documentation (this file)
├── requierments.txt              # Python dependencies (optional, for pip users)
└── venv                          # Virtual environment
```

## Key Features

### Data Handling:
- Support for multiple formats, including CSV and JSON
- Modular processing pipeline for scalability and clarity

### Testing:
- Comprehensive unit tests to ensure robustness

### Bonus (ad-hoc):
- Identify the journal with the most unique drug mentions
- Find related drugs based on shared journal publications

## Getting Started

### Prerequisites
- Python: Ensure Python is installed (here Python 3.13)
- Poetry: Install Poetry for dependency management

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-repo/project-name.git
```
2. Navigate to the project directory:
```bash
cd project-name
```
3. Create a virtualenv environment 
```bash
virtualenv venv
```
4. Access to the virtualenv:
```bash
source venv/bin/activate
```
5. Install poetry in the virtualenv
```
pip install poetry
```
6. Add dependancies to the pyprojet.toml
```bash
poetry add pandas@^2.2.3 pathlib@^1.0.1 chardet@^5.2.0 pytest@^8.3.3
```
7. Install dependencies using Poetry:
```bash
poetry install
```

### Running the Project

- To execute the main script:
```bash
poetry run python Python/main.py
```

### Running ad-hoc functions

- To execute Bonus functions
```bash
poetry run python Python/ad_hoc/bonus.py --function <function_number> [--target_drug <drug_name>] [--data <data_path>]
```
Example:
```bash
poetry run python Python/main.py --function 1
```

### Testing

Run all tests using Pytest:
```bash
pytest
```

### Running SQL queries

SQL queries are stored in SQL/sql. However a sqlite database has been created in order to test the queries on the sample data.

- run query 1
```bash
poetry run python SQL/python/query_1.py
```
- Run query 2
```bash
poetry run python SQL/python/query_2.py
```
### Future Development 

In the case of future developments, whether by using larger data volumes, adding more analytical features, or other extensions, it is recommended to leverage technologies for processing and transforming large datasets, such as Apache Spark, combined with a workflow orchestrator like Airflow to manage the data pipeline (e.g., periodic execution of processes and parallelization of certain tasks).

Additionally, it would be interesting to use graph visualization tools. For instance, storing the generated results in a NoSQL database such as MongoDB and utilizing MongoDB Graph for visualizing these results could be highly beneficial.
