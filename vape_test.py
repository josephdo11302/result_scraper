import unittest
from Model.vapereqs import Vapes
import pandas as pd

class TestConcentrates(unittest.TestCase):
    def test_extract_cannabanoid_profile(self):
        # Path to the CSV file you want to test
        csv_file_path = '/Users/dom/Final_project/Model/CANNABINOID PROFILE.csv'
        # Create an instance of the Concentrates class
        vapes = Vapes()
        # Call the method to extract the data
        extracted_df = vapes.extract_cannabanoid_profile(csv_file_path)
        print(f'\n{extracted_df}')

    def test_extract_heavy_metals(self):
        vapes = Vapes()
        csv_file_path = '/Users/dom/Final_project/Model/HEAVY METALS.csv'
        metal_df = vapes.extract_heavy_metals(csv_file_path)
        print(f'\n{metal_df}')

    def test_extract_microbio(self):
        vapes = Vapes()
        csv_file_path = '/Users/dom/Final_project/Model/MICROBIOLOGICAL CONTAMINANTS.csv'
        micro_df = vapes.extract_microbiological_contaminants(csv_file_path)
        print(f'\n{micro_df}')

    def test_extract_myco(self):
        vapes = Vapes()
        csv_file_path = '/Users/dom/Final_project/Model/MYCOTOXINS.csv'
        myco_df = vapes.extract_mycotoxins(csv_file_path)
        print(f'\n{myco_df}')

if __name__ == '__main__':
    unittest.main()
