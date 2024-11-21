import json
from pathlib import Path

def write_data_to_json(data, file_path):
    """
    Write data to a JSON file, ensuring special characters are properly handled.
    Args:
        data: Data to be written to the file.
        file_path: Path where the JSON file will be saved.
    """
    # Ensure the parent directory exists
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # Convert data to the correct format if necessary (e.g., handle non-ASCII characters)
    def correct_encoding(text):
        """
        Ensures special characters are properly handled by decoding escape sequences
        and returning the correct Unicode string.
        """
        if isinstance(text, str):
            # This step ensures that any escape sequences (like \u00f4) are properly interpreted
            return text.encode('utf-8').decode('unicode_escape')  # Decode any unicode escape sequences
        return text

    # Apply encoding to each field in the data (if needed)
    if isinstance(data, list):  # If it's a dictionary
        data = [{key: correct_encoding(value) for key, value in row.items()} for row in data]
    elif isinstance(data, dict):  # If it's a dictionary
        data = {key: correct_encoding(value) for key, value in data.items()}

    # Write the data to the JSON file
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, default=str, indent=4)
