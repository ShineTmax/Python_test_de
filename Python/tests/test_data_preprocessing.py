import pandas as pd

def clean_drugs(data: pd.DataFrame) -> pd.DataFrame:
    """
    Convert 'atccode' and 'drug' columns to lowercase.
    Args:
        data (pd.DataFrame): Drug data.
    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    data["atccode"] = data["atccode"].str.lower()
    data["drug"] = data["drug"].str.lower()
    return data


def clean_clinical_trials(data: pd.DataFrame) -> pd.DataFrame:
    """
    Clean clinical trials data (lowercase columns, format 'date').
    Args:
        data (pd.DataFrame): Clinical trials data.
    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    data["id"] = data["id"].str.lower()
    # Convert title to lowercase and get rid of words containing '\'
    data["title"] = data["scientific_title"].apply(
    lambda x: ' '.join(
        [word.lower() if '\\' not in word else word.split("\\")[0].lower() for word in str(x).split()]
    ) if isinstance(x, str) else x
)
    # Convert Journal to lowercase and get rid of words containing '\'
    data["journal"] = data["journal"].apply(
    lambda x: ' '.join(
        [word.lower() if '\\' not in word else word.split("\\")[0].lower() for word in str(x).split()]
    ) if isinstance(x, str) else x
)
    data["date"] = pd.to_datetime(data['date'], errors='coerce')
    
    
    return data


def clean_pubmed(data: pd.DataFrame) -> pd.DataFrame:
    """
    Clean PubMed data (lowercase columns, format 'date').

    Args:
        data (pd.DataFrame): PubMed data.

    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    data["id"] = data["id"].astype("str").str.lower()
    # Convert title to lowercase and get rid of words containing '\'
    data["title"] = data["title"].apply(
    lambda x: ' '.join(
        [word.lower() if '\\' not in word else word.split("\\")[0].lower() for word in str(x).split()]
    ) if isinstance(x, str) else x
)
    # Convert Journal to lowercase and get rid of words containing '\'
    data["journal"] = data["journal"].apply(
    lambda x: ' '.join(
        [word.lower() if '\\' not in word else word.split("\\")[0].lower() for word in str(x).split()]
    ) if isinstance(x, str) else x
)
    data["date"] = pd.to_datetime(data['date'], errors='coerce')

    return data


def clean_dataframes(dataframes) -> list[pd.DataFrame]:
    """
    Clean multiple DataFrames.
    Args:
        dataframes (list): List of DataFrames.
    Returns:
        list: List of cleaned DataFrames.
    """
    map_functions = [
        (clean_drugs, dataframes[0]),
        (clean_clinical_trials, dataframes[1]),
        (clean_pubmed, dataframes[2]),
        (clean_pubmed, dataframes[3])
    ]
    return [func(df) for func, df in map_functions]


def concat_dataframes(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """
    Concatenate two DataFrames.

    Args:
        df1 (pd.DataFrame): First DataFrame.
        df2 (pd.DataFrame): Second DataFrame.

    Returns:
        pd.DataFrame: Concatenated DataFrame.
    """
    return pd.concat([df1, df2])
