import unittest
from Model.ediblereqs import Edibles
import pandas as pd

class TestEdibles(unittest.TestCase):
    def test_extract_cannabanoid_profile(self):
        # Path to the CSV file you want to test
        csv_file_path = '/Users/dom/Final_project/Model/CANNABINOID PROFILE.csv'
        # Create an instance of the Concentrates class
        edibles = Edibles()
        # Call the method to extract the data
        extracted_df = edibles.extract_cannabanoid_profile(csv_file_path)
        print(f'\n{extracted_df}')

    def test_extract_heavy_metals(self):
        edibles = Edibles()
        csv_file_path = '/Users/dom/Final_project/Model/HEAVY METALS.csv'
        metal_df = edibles.extract_heavy_metals(csv_file_path)
        print(f'\n{metal_df}')

    def test_extract_microbio(self):
        edibles = Edibles()
        csv_file_path = '/Users/dom/Final_project/Model/MICROBIOLOGICAL CONTAMINANTS.csv'
        micro_df = edibles.extract_microbiological_contaminants(csv_file_path)
        print(f'\n{micro_df}')

    def test_extract_myco(self):
        edibles = Edibles()
        csv_file_path = '/Users/dom/Final_project/Model/MYCOTOXINS.csv'
        myco_df = edibles.extract_mycotoxins(csv_file_path)
        print(f'\n{myco_df}')

if __name__ == '__main__':
    unittest.main()
