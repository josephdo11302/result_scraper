import csv
import os

class ResultsLibrary:
    """
    The ResultsLibrary class manages a collection of product profiles. It provides functionalities to load data from 
    a CSV file, and manage product profiles in memory.
    """
    def __init__(self):
        """
        Initialize the ResultsLibrary with an empty dictionary of products and then load product profiles from the default CSV.
        """
        self.products = {}
        self.load_from_csv()

    def load_from_csv(self, filename="AutoLabel.csv"):
        """
        Load product profiles from a given CSV file into the products dictionary. If the file doesn't exist, 
        the method simply returns without any action.

        :param filename: The name of the CSV file (default is "AutoLabel.csv").
        """
        if not os.path.exists(filename):
            return

        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                product_id = row['Product ID']
                profile = {
                    'type': row['Type'],
                    'TAC': row['TAC'],
                    'THC': row['THC'],
                    'Heavy Metals': row['Heavy Metals'],
                    'Microbials': row['Microbials'],
                    'Mycotoxins': row['Mycotoxins']
                }
                self.products[product_id] = profile

    def add_product(self, product_id, profile):
        """
        Add a product profile to the library.

        :param product_id: A unique identifier for the product.
        :param profile: The profile of the product.
        """
        if product_id in self.products:
            print(f"Product with ID {product_id} already exists. Overwriting...")
        self.products[product_id] = profile

    def get_product(self, product_id):
        """
        Retrieve a product profile from the library.

        :param product_id: The unique identifier for the product.
        :return: The profile of the product.
        """
        return self.products.get(product_id, None)

    def remove_product(self, product_id):
        """
        Remove a product profile from the library.

        :param product_id: The unique identifier for the product.
        """
        if product_id in self.products:
            del self.products[product_id]
        else:
            print(f"Product with ID {product_id} not found.")

    def list_products(self):
        """
        List all product IDs in the library.
        """
        return list(self.products.keys())

    def clear_library(self):
        """
        Clear all products from the library.
        """
        self.products.clear()

