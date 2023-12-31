import pandas as pd
import csv

class ProductRequirements:
    """
    A class to handle the extraction of various product requirements from CSV files.
    """
    def __init__(self):
        """
        Initialize the ProductRequirements instance.
        """
        pass

    def extract_info(self, csv_file_path):
        """
        Read the CSV file and return its content as a DataFrame.

        Args:
            csv_file_path (str): Path to the CSV file.

        Returns:
            pd.DataFrame: DataFrame containing the CSV file content.
        """
        df = pd.read_csv(csv_file_path)
        return df
    
    def extract_cannabanoid_profile(self, csv_file_path):
        """
        Extract the cannabinoid profile from the given CSV file.

        Args:
            csv_file_path (str): Path to the CSV file containing the cannabinoid profile data.

        Returns:
            pd.DataFrame: DataFrame containing the extracted cannabinoid profile.
        """
        # Open the file
        with open(csv_file_path, 'r') as file:
            lines = file.readlines()

        # Find the starting line of the data
        start_line = 0
        for i, line in enumerate(lines):
            if 'unit = ppm' in line:
                start_line = i + 2
                break

        # Extract the lines with the data
        data_lines = lines[start_line:]

        # Split the lines into columns and create a DataFrame
        data = [line.strip().split(',') for line in data_lines]
        extracted_df = pd.DataFrame(data, columns=['Test ID', 'Analyte', 'Concentration', 'LOD', 'Unnamed', 'Unnamed'])

        # Select the desired columns and rows
        extracted_df = extracted_df[['Analyte', 'Concentration', 'LOD']]

        return extracted_df

    def extract_heavy_metals(self, csv_file_path):
        """
        Extract the heavy metals data from the given CSV file.

        Args:
            csv_file_path (str): Path to the CSV file containing the heavy metals data.

        Returns:
            pd.DataFrame: DataFrame containing the extracted heavy metals data.
        """
        # Open the file
        with open(csv_file_path, 'r') as file:
            lines = file.readlines()

        # Find the starting line of the data
        start_line = 0
        for i, line in enumerate(lines):
            if 'unit = ppb,Limits - All Use 2' in line:
                start_line = i + 3  # Skip lines to start at the data
                break

        # Extract the lines with the data
        data_lines = lines[start_line:]

        # Split the lines into columns and create a DataFrame
        data = [line.strip().split(',') for line in data_lines]
        metal_df = pd.DataFrame(data, columns=['Test ID', 'Analyte', 'Concentration1', 'LOD', 'LOQ', 'Limits - All Use 2', 'Result', 'Limits - Ingestion Only 2', 'Result'])

        # Drop the 'Test ID' column
        metal_df = metal_df.drop(columns=['Test ID'])

        return metal_df

    def extract_microbiological_contaminants(self, csv_file_path):
        """
        Extract the microbiological contaminants data from the given CSV file.

        Args:
            csv_file_path (str): Path to the CSV file containing the microbiological contaminants data.

        Returns:
            pd.DataFrame: DataFrame containing the extracted microbiological contaminants data.
        """
        # Open the file using csv module
        with open(csv_file_path, 'r') as file:
            csv_reader = csv.reader(file)
            lines = list(csv_reader)

        # Find the starting line of the data
        start_line = 0
        for i, line in enumerate(lines):
            if 'Symbol' in line and 'Test Analysis' in line:
                start_line = i + 1
                break

        # Extract the lines with the data
        data_lines = lines[start_line:]

        # Create a DataFrame
        data = [[line[0], line[1], line[2], line[3], line[6]] for line in data_lines if len(line) == 7]
        columns = ['Symbol', 'Test Analysis', 'Result', 'Unit', 'Test']
        micro_df = pd.DataFrame(data, columns=columns)

        return micro_df

    def extract_mycotoxins(self, csv_file_path):
        """
        Extract the mycotoxins data from the given CSV file.

        Args:
            csv_file_path (str): Path to the CSV file containing the mycotoxins data.

        Returns:
            pd.DataFrame: DataFrame containing the extracted mycotoxins data.
        """
        # Open the file using csv module
        with open(csv_file_path, 'r') as file:
            csv_reader = csv.reader(file)
            lines = list(csv_reader)

        # Find the starting line of the data
        start_line = 0
        for i, line in enumerate(lines):
            if 'Symbol' in line and 'Analyte' in line:
                start_line = i + 1
                break

        # Extract the lines with the data
        data_lines = lines[start_line:]

        # Create a DataFrame
        data = [[line[0], line[1], line[2], line[3], line[6]] for line in data_lines if len(line) == 8]
        columns = ['Symbol', 'Analyte', 'Result', 'LOD', 'Limit Test']
        myco_df = pd.DataFrame(data, columns=columns)

        return myco_df