import unittest
from Model.ediblereqs import Edibles


class TestEdibles(unittest.TestCase):
    def setUp(self):
        base_path = '/Users/dom/Final_project/Model/'
        self.edible = Edibles(
            cannabanoid_path=base_path + 'CANNABINOID PROFILE.csv',
            heavy_metals_path=base_path + 'HEAVY METALS.csv',
            microbio_path=base_path + 'MICROBIOLOGICAL CONTAMINANTS.csv',
            myco_path=base_path + 'MYCOTOXINS.csv'
        )

    def test_extract_cannabanoid_profile(self):
        extracted_df = self.edible.cannabanoid_df
        print(f'\n{extracted_df}')

    def test_extract_heavy_metals(self):
        metal_df = self.edible.heavy_metals_df
        print(f'\n{metal_df}')

    def test_extract_microbio(self):
        micro_df = self.edible.microbio_df
        print(f'\n{micro_df}')

    def test_extract_myco(self):
        myco_df = self.edible.myco_df
        print(f'\n{myco_df}')

    def test_edible_profile(self):
        # Get the edible profile
        profile = self.edible.edible_profile()

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
