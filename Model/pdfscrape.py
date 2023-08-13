import tabula
import os
import pandas as pd
import re

class PDFScrape:
    """A class to scrape testing data from a PDF file, and export to CSV
    """
    def __init__(self, file_path: str):
        """Initialize the PDFScrape with the path to a PDF file."""
        self.file_path = file_path

    def extract_data(self) -> list:
        """Extract tables from the PDF file as a list of DataFrames.

        Returns:
            list: A list of pandas DataFrames containing the extracted tables.
        """
        tables = tabula.read_pdf(self.file_path, pages=['3', '4'], lattice=True)
        return tables

    # def csv_output(self, data_frames: list):
    #     """Save the extracted data to CSV files."""
    #     script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of this script

    #     for idx, df in enumerate(data_frames):
    #         csv_file = os.path.join(script_dir, f"table_{idx + 1}.csv")
    #         df.to_csv(csv_file, index=False)
    #         print(f"Saved {csv_file}")

    

    def csv_output(self, data_frames: list):
        """Save the extracted data to CSV files."""
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of this script
        os.makedirs(script_dir, exist_ok=True)  # Ensure the directory exists

        for idx, df in enumerate(data_frames):
            # Extract the table name using a regular expression
            match = re.search(r'TABLE [A-Z]+: (.+)', df.columns[0])
            if match:
                table_name = match.group(1).split("Analysis")[0]
            else:
                table_name = f"table_{idx + 1}"

            # Sanitize the table name by removing any characters that are not valid in a filename
            table_name = re.sub(r'[<>:"/\\|?*\r\n]', '', table_name)

            # Construct the CSV file path using the table name
            csv_file = os.path.join(script_dir, f"{table_name}.csv")

            # Save the DataFrame to the CSV file (excluding the first row)
            df.iloc[1:].to_csv(csv_file, index=False)
            print(f"Saved {csv_file}")








    
