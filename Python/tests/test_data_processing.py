import pandas as pd

def find_mentions(drugs_df: pd.DataFrame, df: pd.DataFrame, source: str) -> list:
    """
    Finds mentions of drugs in a list of publications and returns the details of the matches.

    This function checks if each drug from the `drugs_df` DataFrame appears in the title of any publication
    from the `df` DataFrame. If a match is found, it stores the drug name along with the corresponding 
    publication details (title, journal, and date).

    Args:
        drugs_df (pd.DataFrame): A DataFrame containing information about drugs, with at least a 'drug' column.
        df (pd.DataFrame): A DataFrame containing publication information, with at least 'title', 'journal', and 'date' columns.

    Returns:
        list: A list of dictionaries, each containing a drug name and the corresponding publications where the drug was mentioned.
    """
    mentions = {}

    for drug_row in drugs_df.itertuples():
        drug_name = drug_row.drug

        # Initialize if the drug is not already in the mentions dictionary
        if drug_name not in mentions:
            mentions[drug_name] = {
                "drug": drug_name,
                "reference":{
                    "pubmed": [],
                    "clinical_trials": []
                }
            }

        # Search for the drug in the publications
        for publication_row in df.itertuples():
            if drug_name in publication_row.title:
                mentions[drug_name]["reference"][source].append({
                    "title": publication_row.title,
                    "journal": publication_row.journal,
                    "date": publication_row.date
                })

    # Convert the dictionary to a list of dictionaries for the output
    return list(mentions.values())
