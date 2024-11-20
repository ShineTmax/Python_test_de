from src.data_reading import read_data
from src.data_preprocessing import clean_dataframes, concat_dataframes
from src.data_processing import find_mentions
from src.data_writting import write_data_to_json
from ad_hoc.bonus import find_journal_with_most_drugs, find_other_drugs_by_same_journals
from src import INPUT_FILES, OUTPUT_FILEPATH, logger

def main():
    """
    Main function to orchestrate the data reading, cleaning, processing, and writing.

    This function:
    1. Reads the input data from files.
    2. Cleans the data.
    3. Concatenates Pubmed data.
    4. Finds mentions of drugs in clinical trials and Pubmed.
    5. Writes the results to a JSON file.
    """
    # Read data files
    drugs_df, clinical_trials_df, pubmed_df_1, pubmed_df_2 = read_data(INPUT_FILES)
    dataframes = [drugs_df, clinical_trials_df, pubmed_df_1, pubmed_df_2]

    logger.info(f"Reading Data {INPUT_FILES}: Done.")

    # Clean the data
    cleaned_drugs_df, cleaned_clinical_trials_df, cleaned_pubmed_df_1, cleaned_pubmed_df_2 = clean_dataframes(dataframes)
    logger.info("Cleaning Data: done.")

    # Concatenate Pubmed Data
    cleaned_pubmed = concat_dataframes(cleaned_pubmed_df_1, cleaned_pubmed_df_2)
    logger.info("Concatenating Pubmed Data (json and csv): Done.")

    # Process mentions
    final_mentions = {}

    # find mentions in clinical trials
    clinical_trials_mentions = find_mentions(cleaned_drugs_df, cleaned_clinical_trials_df, source="clinical_trials")
    for mention in clinical_trials_mentions:
        drug_name = mention["drug"]
        if drug_name not in final_mentions:
            final_mentions[drug_name] = mention
        else:
            # Merge mentions for clinical trials
            final_mentions[drug_name]["reference"]["clinical_trials"] += mention["reference"]["clinical_trials"]

    # find mentions in Pubmed
    pubmed_mentions = find_mentions(cleaned_drugs_df, cleaned_pubmed, source="pubmed")
    for mention in pubmed_mentions:
        drug_name = mention["drug"]
        if drug_name not in final_mentions:
            final_mentions[drug_name] = mention
        else:
            # Merge mentions for Pubmed
            final_mentions[drug_name]["reference"]["pubmed"] += mention["reference"]["pubmed"]

    # convert final mentions to List
    final_mentions_list = list(final_mentions.values())

    logger.info("Processing- Finding mentions for drugs in Journal: Done.")
    # Write the data to JSON
    
    write_data_to_json(final_mentions_list, OUTPUT_FILEPATH)
    logger.info(f"Writting Json Data into {OUTPUT_FILEPATH}: Done.")



if __name__ == "__main__":
    main()
