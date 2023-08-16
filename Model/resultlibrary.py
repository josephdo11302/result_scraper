import csv
import os

class ResultsLibrary:
    """
    Manages a collection of product profiles, providing functionalities to load, 
    save, and manage product profiles in memory.
    """
    def __init__(self):
        """
        Initialize the ResultsLibrary with an empty dictionary of products and 
        load product profiles from the default CSV.
        """
        self.products = {}
        self.load_from_csv()

    def load_from_csv(self, filename="AutoLabel.csv"):
        """
        Load product profiles from a CSV file into the products dictionary.

        Args:
            filename (str): The name of the CSV file. Defaults to "AutoLabel.csv".

        Returns:
            None
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

    def add_product(self, product_id: str, profile: dict):
        """
        Add or overwrite a product profile in the library.

        Args:
            product_id (str): A unique identifier for the product.
            profile (dict): The profile of the product.

        Returns:
            None
        """
        if product_id in self.products:
            print(f"Product with ID {product_id} already exists. Overwriting...")
        self.products[product_id] = profile

    def get_product(self, product_id: str) -> dict:
        """
        Retrieve a product profile from the library.

        Args:
            product_id (str): The unique identifier for the product.

        Returns:
            dict: The profile of the product or None if not found.
        """
        return self.products.get(product_id, None)

    def remove_product(self, product_id: str):
        """
        Remove a product profile from the library and update the CSV.

        Args:
            product_id (str): The unique identifier for the product.

        Returns:
            None
        """
        if product_id in self.products:
            del self.products[product_id]
            self.save_to_csv()  # Save the updated library to the CSV
        else:
            print(f"Product with ID {product_id} not found.")

    def save_to_csv(self, filename="AutoLabel.csv"):
        """
        Save the current state of the library to a CSV file.

        Args:
            filename (str): The name of the CSV file. Defaults to "AutoLabel.csv".

        Returns:
            None
        """
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Product ID', 'Type', 'TAC', 'THC', 'Heavy Metals', 'Microbials', 'Mycotoxins']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for product_id, profile in self.products.items():
                writer.writerow({
                    'Product ID': product_id,
                    'Type': profile['type'],
                    'TAC': profile['TAC'],
                    'THC': profile['THC'],
                    'Heavy Metals': profile['Heavy Metals'],
                    'Microbials': profile['Microbials'],
                    'Mycotoxins': profile['Mycotoxins']
                })

    def list_products(self) -> list:
        """
        List all product IDs in the library.

        Returns:
            list: A list containing all product IDs.
        """
        return list(self.products.keys())

    def clear_library(self):
        """
        Clear all products from the library.

        Returns:
            None
        """
        self.products.clear()

