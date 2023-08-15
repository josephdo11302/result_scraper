from Model.productrequirements import ProductRequirements
import pandas as pd
import csv

class Vapes(ProductRequirements):
    def extract_cannabanoid_profile(self, csv_file_path):
        """
        Extracts the cannabinoid profile from the given CSV file.

        :param csv_file_path: Path to the CSV file containing the cannabinoid profile data.
        :return: A DataFrame containing the extracted cannabinoid profile.
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
        Extracts the heavy metals data from the given CSV file.

        :param csv_file_path: Path to the CSV file containing the heavy metals data.
        :return: A DataFrame containing the extracted heavy metals data.
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
        Extracts the microbiological contaminants data from the given CSV file.

        :param csv_file_path: Path to the CSV file containing the microbiological contaminants data.
        :return: A DataFrame containing the extracted microbiological contaminants data.
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
        Extracts the mycotoxins data from the given CSV file.

        :param csv_file_path: Path to the CSV file containing the mycotoxins data.
        :return: A DataFrame containing the extracted mycotoxins data.
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
    
    def concentrate_profile(self, cannabanoid_df, heavy_metals_df, micro_df, myco_df):
        """
        Generate a profile for vapes based on provided dataframes.

        Parameters:
        - cannabanoid_df (pd.DataFrame): DataFrame containing cannabanoid profile data.
        - heavy_metals_df (pd.DataFrame): DataFrame containing heavy metals data.
        - micro_df (pd.DataFrame): DataFrame containing microbiological contaminants data.
        - myco_df (pd.DataFrame): DataFrame containing mycotoxins data.

        Returns:
        dict: A dictionary containing the profile for concentrates. The structure is:
            {
                "type": "vape",
                "TAC": sum of all numbers under "concentration" in the cannabanoid profile,
                "THC": THCA concentration value,
                "Heavy Metals": "PASS" if all results are "PASS", otherwise "FAIL",
                "Microbials": "PASS" if all results are "PASS", otherwise "FAIL",
                "Mycotoxins": "<LOD" if all results are "< LOD", otherwise "FAIL"
            }
        """

        profile = {"type": "vape"}

        # 1. TAC
        try:
            profile["TAC"] = cannabanoid_df["Concentration"].replace('ND', '0').astype(float).sum()
        except:
            profile["TAC"] = "Error"

        # 2. THCA
        try:
            profile["THC"] = cannabanoid_df.loc[cannabanoid_df["Analyte"] == "THCA", "Concentration"].values[0]
        except:
            profile["THC"] = "Error"

        # 3. Heavy Metals
        if all(heavy_metals_df["Result"] == "PASS"):
            profile["Heavy Metals"] = "PASS"
        else:
            profile["Heavy Metals"] = "FAIL"

        # 4. Microbials
        if all(micro_df["Test"] == "PASS"):
            profile["Microbials"] = "PASS"
        else:
            profile["Microbials"] = "FAIL"

        # 5. Mycotoxins
        if all(row['LOD'].strip() == '< LOD' for _, row in myco_df.iterrows()):
            profile["Mycotoxins"] = "PASS"
        else:
            profile["Mycotoxins"] = "FAIL"

        return profile
   