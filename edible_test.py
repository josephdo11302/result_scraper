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

    def test_edible_profile(self):
        edible = Edibles()

        # Extract data from each CSV file
        cannabanoid_df = edible.extract_cannabanoid_profile('/Users/dom/Final_project/Model/CANNABINOID PROFILE.csv')
        heavy_metals_df = edible.extract_heavy_metals('/Users/dom/Final_project/Model/HEAVY METALS.csv')
        micro_df = edible.extract_microbiological_contaminants('/Users/dom/Final_project/Model/MICROBIOLOGICAL CONTAMINANTS.csv')
        myco_df = edible.extract_mycotoxins('/Users/dom/Final_project/Model/MYCOTOXINS.csv')

        # Get the edible profile
        profile = edible.edible_profile(cannabanoid_df, heavy_metals_df, micro_df, myco_df)

        # Print the profile for debugging purposes
        print(f'\n{profile}')

        # Assert the expected results
        self.assertEqual(profile["type"], "edible")
        self.assertTrue(isinstance(profile["TAC"], str) and "mg" in profile["TAC"] or profile["TAC"] == "Error")
        self.assertTrue(isinstance(profile["THC"], str) and "mg" in profile["THC"] or profile["THC"] == "Error")
        self.assertIn(profile["Heavy Metals"], ["PASS", "FAIL"])
        self.assertIn(profile["Microbials"], ["PASS", "FAIL"])
        self.assertIn(profile["Mycotoxins"], ["PASS", "FAIL"])

if __name__ == '__main__':
    unittest.main()
