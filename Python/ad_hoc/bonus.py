import argparse

def find_journal_with_most_drugs(data: list) -> str:
    """
    Find the journal mentioning the highest number of distinct drugs.

    Args:
        data (list): List of dictionaries containing drug details and references.

    Returns:
        str: Name of the journal with the most distinct drug mentions.
    """
    journal_counts = {}

    # Iterate over each drug's references
    for entry in data:
        drug_name = entry['drug']
        # Process references from both pubmed and clinical_trials
        for source in entry['reference'].values():
            for publication in source:
                journal_name = publication['journal']
                # Initialize journal entry if not present
                if journal_name not in journal_counts:
                    journal_counts[journal_name] = set()
                # Add the drug to the journal's set to ensure uniqueness
                journal_counts[journal_name].add(drug_name)

    # Determine the journal with the maximum number of unique drugs
    most_mentions_journal = max(journal_counts, key=lambda journal: len(journal_counts[journal]))

    return most_mentions_journal


def find_other_drugs_by_same_journals(data: list, target_drug: str) -> set:
    """
    Find other drugs mentioned in the same journals as the given target drug.

    Args:
        data (list): List of dictionaries containing drug details and references.
        target_drug (str): Drug for which to find other related drugs.

    Returns:
        set: Set of other drugs mentioned in the same journals as the target drug.
    """

    # Identify journals associated with the target drug
    target_drug_journals = set()
    for entry in data:
        if entry['drug'] == target_drug:
            for source in entry['reference'].values():
                for publication in source:
                    journal_name = publication['journal']
                    # Include only valid journals and non-empty dates
                    if journal_name and publication['date'] != "NaT":
                        target_drug_journals.add(journal_name)

    # If no journals are found, return an empty set
    if not target_drug_journals:
        print(f"No journals found for the drug '{target_drug}'.")
        return set()

    # Find drugs referenced in the same journals
    other_drugs = set()
    for entry in data:
        for source in entry['reference'].values():
            for publication in source:
                journal_name = publication['journal']
                # Add drugs found in the target drug's journals
                if journal_name in target_drug_journals and entry['drug'] != target_drug:
                    other_drugs.add(entry['drug'])

    # Display journals associated with the target drug
    print(f"Journals associated with '{target_drug}': {target_drug_journals}")
    return other_drugs


if __name__ == "__main__":
    # Create the parser to handle command-line arguments
    parser = argparse.ArgumentParser(description="Select and execute a drug-related function.")

    # Map numbered choices to corresponding functions
    function_map = {
        '1': 'find_journal_with_most_drugs',
        '2': 'find_other_drugs_by_same_journals'
    }

    # Argument for function selection
    parser.add_argument('--function', choices=function_map.keys(), required=True,
                        help="Choose '1' for finding the journal with the most distinct drugs or '2' for finding other drugs mentioned in the same journals.")

    # Optional argument for specifying the target drug
    parser.add_argument('--target_drug', default='diphenhydramine', type=str,
                        help="The target drug for 'find_other_drugs_by_same_journals'. Default is 'diphenhydramine'.")

    # Argument for specifying the data file
    parser.add_argument('--data', default='Results/output.json', required=False,
                        help="Path to the data file (default: 'Results/output.json').")

    # Parse arguments
    args = parser.parse_args()

    # Load the data from the specified file
    import json
    with open(args.data, 'r') as f:
        data = json.load(f)

    # Execute the selected function
    if args.function == '1':
        result = find_journal_with_most_drugs(data)
        print(f"The journal that mentions the most distinct drugs is: {result}")

    elif args.function == '2':
        result = find_other_drugs_by_same_journals(data, args.target_drug)
        print(f"The other drugs mentioned in the same journals are: {result}")
