import unittest
from Model.vapereqs import Vapes


class TestVapes(unittest.TestCase):
    def setUp(self):
        base_path = '/Users/dom/Final_project/Model/'
        self.vapes = Vapes(
            cannabanoid_path=base_path + 'CANNABINOID PROFILE.csv',
            heavy_metals_path=base_path + 'HEAVY METALS.csv',
            microbio_path=base_path + 'MICROBIOLOGICAL CONTAMINANTS.csv',
            myco_path=base_path + 'MYCOTOXINS.csv'
        )

    def test_extract_cannabanoid_profile(self):
        extracted_df = self.vapes.cannabanoid_df
        print(f'\n{extracted_df}')

    def test_extract_heavy_metals(self):
        metal_df = self.vapes.heavy_metals_df
        print(f'\n{metal_df}')

    def test_extract_microbio(self):
        micro_df = self.vapes.microbio_df
        print(f'\n{micro_df}')

    def test_extract_myco(self):
        myco_df = self.vapes.myco_df
        print(f'\n{myco_df}')

    def test_vape_profile(self):
        # Get the vape profile
        profile = self.vapes.vape_profile()

        # Print the profile for debugging purposes
        print(f'\n{profile}')

        # Assert the expected results (modify as per your expected results)
        self.assertEqual(profile["type"], "vape")
        self.assertTrue(isinstance(profile["TAC"], float) or profile["TAC"] == "Error")
        self.assertTrue(isinstance(profile["THC"], str) or profile["THC"] == "Error")
        self.assertIn(profile["Heavy Metals"], ["PASS", "FAIL"])
        self.assertIn(profile["Microbials"], ["PASS", "FAIL"])
        self.assertIn(profile["Mycotoxins"], ["PASS", "FAIL"])

if __name__ == '__main__':
    unittest.main()

