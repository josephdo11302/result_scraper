from Model.productrequirements import ProductRequirements
import pandas as pd
import csv

class Edibles(ProductRequirements):
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
    
    def edible_profile(self, cannabanoid_df, heavy_metals_df, microbio_df, myco_df):
        # Calculate TAC by summing numeric values in the LOD column
        TAC_values = cannabanoid_df['LOD'].replace(['ND', '<LOQ'], '0').astype(float)
        TAC = str(TAC_values.sum()) + " mg"
        
        # Extract THC value corresponding to D9-THC
        THC_value = cannabanoid_df[cannabanoid_df["Analyte"] == "D9-THC"]["LOD"].values[0]
        try:
            THC = str(float(THC_value)) + " mg"
        except ValueError:
            THC = "Error"
        
        # Check results for heavy metals, microbials, and mycotoxins
        heavy_metals_result = "PASS" if all(heavy_metals_df["Result"] == "PASS") else "FAIL"
        microbials_result = "PASS" if all(microbio_df["Test"] == "PASS") else "FAIL"
        mycotoxins_result = "PASS" if all(row['LOD'].strip() == '< LOD' for _, row in myco_df.iterrows()) else "FAIL"
        
        profile = {
            "type": "edible",
            "TAC": TAC,
            "THC": THC,
            "Heavy Metals": heavy_metals_result,
            "Microbials": microbials_result,
            "Mycotoxins": mycotoxins_result
        }
        
        return profile


   