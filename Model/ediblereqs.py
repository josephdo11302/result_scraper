from Model.productrequirements import ProductRequirements


class Edibles(ProductRequirements):
    """
    The Edibles class represents the requirements for edible products. 
    It inherits from the ProductRequirements class and provides methods 
    specific to edibles.
    """

    def __init__(self, cannabanoid_path, heavy_metals_path, microbio_path, myco_path):
        """
        The Edibles class represents the requirements for edible products. 
        It inherits from the ProductRequirements class and provides methods 
        specific to edibles.
        """
        super().__init__()
        self.cannabanoid_df = self.extract_cannabanoid_profile(cannabanoid_path)
        self.heavy_metals_df = self.extract_heavy_metals(heavy_metals_path)
        self.microbio_df = self.extract_microbiological_contaminants(microbio_path)
        self.myco_df = self.extract_mycotoxins(myco_path)

    def edible_profile(self):
        """
        Generates a profile for the edible product based on the provided data.

        :return: A dictionary containing the edible product's profile, including TAC, THC, 
                 and results for heavy metals, microbials, and mycotoxins.
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


   