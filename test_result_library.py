import unittest
from Model.resultlibrary import ResultsLibrary  
from Model.productrequirements import ProductRequirements
from Model.vapereqs import Vapes
from Model.concentratereqs import Concentrates
from Model.ediblereqs import Edibles
from test_edible import TestEdibles
from test_vape import TestVapes
from test_concentrate import TestConcentrates

class TestResultsLibrary(unittest.TestCase):
    def setUp(self):
        # This method is called before each test. We'll set up a fresh instance of ResultsLibrary and the scraping classes for each test.
        self.library = ResultsLibrary()
        
        # Provide the paths to the CSV files for the Edibles class
        cannabanoid_path = '/Users/dom/Final_project/Model/CANNABINOID PROFILE.csv'
        heavy_metals_path = '/Users/dom/Final_project/Model/HEAVY METALS.csv'
        microbio_path = '/Users/dom/Final_project/Model/MICROBIOLOGICAL CONTAMINANTS.csv'
        myco_path = '/Users/dom/Final_project/Model/MYCOTOXINS.csv'
        
        self.edibles = Edibles(cannabanoid_path, heavy_metals_path, microbio_path, myco_path)
        self.vapes = Vapes(cannabanoid_path, heavy_metals_path, microbio_path, myco_path)
        self.concentrates = Concentrates(cannabanoid_path, heavy_metals_path, microbio_path, myco_path)


    def test_add_and_get_product(self):
        # Define a sample product and its ID
        product_id = "sample_001"
        
        # Use the Edibles class to generate a profile
        profile = self.edibles.edible_profile()

        # Add the product to the library
        self.library.add_product(product_id, profile)

        # Retrieve the product and check if it matches the original
        retrieved_profile = self.library.get_product(product_id)
        self.assertEqual(retrieved_profile, profile)

    def test_remove_product(self):
        product_id = "sample_002"
        
        # Use the Vapes class to generate a profile
        profile = self.vapes.vape_profile()
        
        self.library.add_product(product_id, profile)

        # Remove the product
        self.library.remove_product(product_id)

        # Try to retrieve the product. It should return None since it's been removed.
        self.assertIsNone(self.library.get_product(product_id))

    def test_list_products(self):
        product_ids = ["sample_003", "sample_004"]
        
        # Use the Concentrates class to generate profiles
        profiles = [self.concentrates.concentrate_profile() for _ in product_ids]

        for pid, profile in zip(product_ids, profiles):
            self.library.add_product(pid, profile)

        # Check if the list of product IDs matches the added product IDs
        self.assertListEqual(self.library.list_products(), product_ids)

    def test_clear_library(self):
        product_id = "sample_005"
        
        # Use the Edibles class to generate a profile
        profile = self.edibles.edible_profile()
        
        self.library.add_product(product_id, profile)

        # Clear the library
        self.library.clear_library()

        # Check if the library is empty
        self.assertListEqual(self.library.list_products(), [])

    def test_print_products(self):
        # Add a few sample products to the library
        product_ids = ["sample_001", "sample_002", "sample_003"]
        
        profiles = [
            self.edibles.edible_profile(),
            self.vapes.vape_profile(),
            self.concentrates.concentrate_profile()
        ]

        for pid, profile in zip(product_ids, profiles):
            self.library.add_product(pid, profile)

        # Print out the products in the library
        print("\nProducts in the library:")
        for pid in self.library.list_products():
            print(f"Product ID: {pid}")
            print("Profile:", self.library.get_product(pid))
            print("-------------------------------------------------")


if __name__ == '__main__':
    unittest.main() 