class ResultsLibrary:
    def __init__(self):
        # Initialize an empty dictionary to store the products
        self.products = {}

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

