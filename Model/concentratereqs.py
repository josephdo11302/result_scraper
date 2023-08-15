from Model.productrequirements import ProductRequirements
import pandas as pd
import csv

class Concentrates(ProductRequirements):
    """
    A class for generating product profiles of concentrates based on extracted data
    related to cannabinoid profile, heavy metals, microbiological contaminants,
    and mycotoxins.

    Inherits from the ProductRequirements class.

    Attributes:
        cannabanoid_df (pd.DataFrame): DataFrame containing cannabinoid profile data.
        heavy_metals_df (pd.DataFrame): DataFrame containing heavy metals data.
        microbio_df (pd.DataFrame): DataFrame containing microbiological contaminants data.
        myco_df (pd.DataFrame): DataFrame containing mycotoxins data.

    Methods:
        concentrate_profile(): Generate a product profile for concentrates.
    """
    def __init__(self, cannabanoid_path, heavy_metals_path, microbio_path, myco_path):
        """
        Initialize the Concentrates class with paths to CSV files containing data
        related to cannabinoid profile, heavy metals, microbiological contaminants,
        and mycotoxins.

        :param cannabanoid_path: str - Path to the CSV containing cannabinoid profile data.
        :param heavy_metals_path: str - Path to the CSV containing heavy metals data.
        :param microbio_path: str - Path to the CSV containing microbiological contaminants data.
        :param myco_path: str - Path to the CSV containing mycotoxins data.
        """
        super().__init__()
        self.cannabanoid_df = self.extract_cannabanoid_profile(cannabanoid_path)
        self.heavy_metals_df = self.extract_heavy_metals(heavy_metals_path)
        self.microbio_df = self.extract_microbiological_contaminants(microbio_path)
        self.myco_df = self.extract_mycotoxins(myco_path)

    def concentrate_profile(self):
        """
        Generate and return a product profile for concentrates based on extracted data.

        :return: dict - A dictionary containing the product profile for concentrates.
        """
        profile = {"type": "concentrate"}

        # 1. TAC
        try:
            profile["TAC"] = self.cannabanoid_df["Concentration"].replace('ND', '0').astype(float).sum()
        except:
            profile["TAC"] = "Error"

        # 2. THCA
        try:
            profile["THC"] = self.cannabanoid_df.loc[self.cannabanoid_df["Analyte"] == "THCA", "Concentration"].values[0]
        except:
            profile["THC"] = "Error"

        # 3. Heavy Metals
        if all(self.heavy_metals_df["Result"] == "PASS"):
            profile["Heavy Metals"] = "PASS"
        else:
            profile["Heavy Metals"] = "FAIL"

        # 4. Microbials
        if all(self.microbio_df["Test"] == "PASS"):
            profile["Microbials"] = "PASS"
        else:
            profile["Microbials"] = "FAIL"

        # 5. Mycotoxins
        if all(row['LOD'].strip() == '< LOD' for _, row in self.myco_df.iterrows()):
            profile["Mycotoxins"] = "PASS"
        else:
            profile["Mycotoxins"] = "FAIL"

        return profile
    