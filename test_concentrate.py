import unittest
from Model.concentratereqs import Concentrates

class TestConcentrates(unittest.TestCase):
    def setUp(self):
        base_path = '/Users/dom/Final_project/Model/'
        self.concentrates = Concentrates(
            cannabanoid_path=base_path + 'CANNABINOID PROFILE.csv',
            heavy_metals_path=base_path + 'HEAVY METALS.csv',
            microbio_path=base_path + 'MICROBIOLOGICAL CONTAMINANTS.csv',
            myco_path=base_path + 'MYCOTOXINS.csv'
        )

    def test_extract_cannabanoid_profile(self):
        extracted_df = self.concentrates.cannabanoid_df
        print(f'\n{extracted_df}')

    def test_extract_heavy_metals(self):
        metal_df = self.concentrates.heavy_metals_df
        print(f'\n{metal_df}')

    def test_extract_microbio(self):
        micro_df = self.concentrates.microbio_df
        print(f'\n{micro_df}')

    def test_extract_myco(self):
        myco_df = self.concentrates.myco_df
        print(f'\n{myco_df}')

    def test_concentrate_profile(self):
        # Get the concentrate profile
        profile = self.concentrates.concentrate_profile()

        # Print the profile for debugging purposes
        print(f'\n{profile}')

        # Assert the expected results (modify as per your expected results)
        self.assertEqual(profile["type"], "concentrate")
        self.assertTrue(isinstance(profile["TAC"], float) or profile["TAC"] == "Error")
        self.assertTrue(isinstance(profile["THC"], str) or profile["THC"] == "Error")
        self.assertIn(profile["Heavy Metals"], ["PASS", "FAIL"])
        self.assertIn(profile["Microbials"], ["PASS", "FAIL"])
        self.assertIn(profile["Mycotoxins"], ["PASS", "FAIL"])

if __name__ == '__main__':
    unittest.main()
#     def test_extract_cannabanoid_profile(self):
#         # Path to the CSV file you want to test
#         csv_file_path = '/Users/dom/Final_project/Model/CANNABINOID PROFILE.csv'
#         # Create an instance of the Concentrates class
#         concentrates = Concentrates()
#         # Call the method to extract the data
#         extracted_df = concentrates.extract_cannabanoid_profile(csv_file_path)
#         print(f'\n{extracted_df}')

#     def test_extract_heavy_metals(self):
#         concentrates = Concentrates()
#         csv_file_path = '/Users/dom/Final_project/Model/HEAVY METALS.csv'
#         metal_df = concentrates.extract_heavy_metals(csv_file_path)
#         print(f'\n{metal_df}')

#     def test_extract_microbio(self):
#         concentrates = Concentrates()
#         csv_file_path = '/Users/dom/Final_project/Model/MICROBIOLOGICAL CONTAMINANTS.csv'
#         micro_df = concentrates.extract_microbiological_contaminants(csv_file_path)
#         print(f'\n{micro_df}')

#     def test_extract_myco(self):
#         concentrates = Concentrates()
#         csv_file_path = '/Users/dom/Final_project/Model/MYCOTOXINS.csv'
#         myco_df = concentrates.extract_mycotoxins(csv_file_path)
#         print(f'\n{myco_df}')

#     def test_concentrate_profile(self):
#         concentrates = Concentrates()

#         # Extract data from each CSV file
#         cannabanoid_df = concentrates.extract_cannabanoid_profile('/Users/dom/Final_project/Model/CANNABINOID PROFILE.csv')
#         heavy_metals_df = concentrates.extract_heavy_metals('/Users/dom/Final_project/Model/HEAVY METALS.csv')
#         micro_df = concentrates.extract_microbiological_contaminants('/Users/dom/Final_project/Model/MICROBIOLOGICAL CONTAMINANTS.csv')
#         myco_df = concentrates.extract_mycotoxins('/Users/dom/Final_project/Model/MYCOTOXINS.csv')

#         # Get the concentrate profile
#         profile = concentrates.concentrate_profile(cannabanoid_df, heavy_metals_df, micro_df, myco_df)

#         # Print the profile for debugging purposes
#         print(myco_df['LOD'].unique())
#         print(f'\n{profile}')

#         # Assert the expected results (modify as per your expected results)
#         self.assertEqual(profile["type"], "concentrate")
#         self.assertTrue(isinstance(profile["TAC"], float) or profile["TAC"] == "Error")
#         self.assertTrue(isinstance(profile["THC"], str) or profile["THC"] == "Error")
#         self.assertIn(profile["Heavy Metals"], ["PASS", "FAIL"])
#         self.assertIn(profile["Microbials"], ["PASS", "FAIL"])
#         self.assertIn(profile["Mycotoxins"], ["PASS", "FAIL"])

# if __name__ == '__main__':
#     unittest.main()
