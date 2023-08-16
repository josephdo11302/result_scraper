from Model.productrequirements import ProductRequirements
import pandas as pd
import csv

class Vapes(ProductRequirements):
    """
    Represents the requirements for vape products. 
    Inherits from the ProductRequirements class and provides methods specific to vapes.
    """

    def __init__(self, cannabanoid_path: str, heavy_metals_path: str, microbio_path: str, myco_path: str) -> None:
        """
        Initializes the Vapes class by extracting data from provided CSV paths.

        Args:
            cannabanoid_path (str): Path to the CSV file containing cannabanoid profile data.
            heavy_metals_path (str): Path to the CSV file containing heavy metals data.
            microbio_path (str): Path to the CSV file containing microbiological contaminants data.
            myco_path (str): Path to the CSV file containing mycotoxins data.
        """
        super().__init__()  # Call the constructor of the base class
        self.cannabanoid_df = self.extract_cannabanoid_profile(cannabanoid_path)
        self.heavy_metals_df = self.extract_heavy_metals(heavy_metals_path)
        self.microbio_df = self.extract_microbiological_contaminants(microbio_path)
        self.myco_df = self.extract_mycotoxins(myco_path)

    def vape_profile(self) -> dict:
        """
        Generate a profile for vapes based on the extracted data.

        Returns:
            dict: A dictionary containing the profile for vapes. The structure is:
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
   