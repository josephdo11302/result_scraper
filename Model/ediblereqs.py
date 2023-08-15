from Model.productrequirements import ProductRequirements


class Edibles(ProductRequirements):
    """
    The Edibles class represents the requirements for edible products.
    It inherits from the ProductRequirements class and provides methods
    specific to edibles.

    Attributes:
        cannabanoid_df (pd.DataFrame): DataFrame containing cannabinoid profile data.
        heavy_metals_df (pd.DataFrame): DataFrame containing heavy metals data.
        microbio_df (pd.DataFrame): DataFrame containing microbiological contaminants data.
        myco_df (pd.DataFrame): DataFrame containing mycotoxins data.

    Methods:
        edible_profile(): Generate a product profile for edible products.
    """

    def __init__(self, cannabanoid_path, heavy_metals_path, microbio_path, myco_path):
        """
        Initialize the Edibles class with paths to CSV files containing data
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

    def edible_profile(self):
        """
        Generate and return a product profile for edible products based on extracted data.

        :return: dict - A dictionary containing the product profile for edibles.
        """
        
        # Calculate TAC by summing numeric values in the LOD column
        TAC_values = self.cannabanoid_df['LOD'].replace(['ND', '<LOQ'], '0').astype(float)
        TAC = str(TAC_values.sum()) + " mg"
        
        # Extract THC value corresponding to D9-THC
        THC_value = self.cannabanoid_df[self.cannabanoid_df["Analyte"] == "D9-THC"]["LOD"].values[0]
        try:
            THC = str(float(THC_value)) + " mg"
        except ValueError:
            THC = "Error"
        
        # Check results for heavy metals, microbials, and mycotoxins
        heavy_metals_result = "PASS" if all(self.heavy_metals_df["Result"] == "PASS") else "FAIL"
        microbials_result = "PASS" if all(self.microbio_df["Test"] == "PASS") else "FAIL"
        mycotoxins_result = "PASS" if all(row['LOD'].strip() == '< LOD' for _, row in self.myco_df.iterrows()) else "FAIL"
        
        profile = {
            "type": "edible",
            "TAC": TAC,
            "THC": THC,
            "Heavy Metals": heavy_metals_result,
            "Microbials": microbials_result,
            "Mycotoxins": mycotoxins_result
        }
        
        return profile


   