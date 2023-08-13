from Model.productrequirements import ProductRequirements
import pandas as pd

class Edibles(ProductRequirements):
    def extract_info(self, csv_file_path):
        # Call parent method to extract general information
        df = super().extract_info(csv_file_path)
        # Extract additional information specific to edibles
        return df