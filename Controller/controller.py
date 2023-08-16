from Model.ediblereqs import Edibles
from Model.vapereqs import Vapes
from Model.concentratereqs import Concentrates
import csv
import os
from Model.pdfscrape import PDFScrape

class Controller:
    """
    The Controller class handles the application's business logic. It interacts with the data model (ResultsLibrary)
    and provides functionalities like scraping PDFs, fetching past results, generating reports, and exporting data.
    """
    def __init__(self, library):
        """
        Initialize the Controller with a given ResultsLibrary.

        :param library: The ResultsLibrary instance to manage product profiles.
        """
        self.library = library

    def get_product_id(self):
        """
        Prompt the user for a METRC tag.

        :return: The METRC tag entered by the user.
        """
        return input("Enter the METRC tag: ")
    
    def get_product(self, product_id):
        """
        Retrieve a product profile from the library using its ID.

        :param product_id: The unique identifier for the product.
        :return: The profile of the product or None if not found.
        """
        return self.library.get_product(product_id)

    def remove_product(self, product_id):
        """
        Remove a product profile from the library using its ID. calls the remove_product from product library
        this just acts as a bridge

        :param product_id: The unique identifier for the product.
        :return: True if the product was removed, False otherwise.
        """
        if product_id in self.library.products:
            self.library.remove_product(product_id)
            return True
        return False
        
    def scrape_new_pdf(self, file_path, product_type):
        """
        Scrape data from a given PDF and save the extracted data to CSVs based on the product type.

        :param file_path: The path to the PDF file.
        :param product_type: The type of the product (edible, vape, concentrate).
        :return: The scraped product profile or a message indicating an invalid product type.
        """

        # Use PDFScrape to extract data from the PDF and save to CSVs
        pdf_scraper = PDFScrape(file_path)
        data_frames = pdf_scraper.extract_data()
        pdf_scraper.csv_output(data_frames)

        # Define the paths to the CSVs
        base_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current file (Controller)
        model_dir = os.path.join(os.path.dirname(base_dir), 'Model')  # Navigate to the Model directory
        cannabanoid_path = os.path.join(model_dir, 'CANNABINOID PROFILE.csv')
        heavy_metals_path = os.path.join(model_dir, 'HEAVY METALS.csv')
        microbio_path = os.path.join(model_dir, 'MICROBIOLOGICAL CONTAMINANTS.csv')
        myco_path = os.path.join(model_dir, 'MYCOTOXINS.csv')

        # Use the product requirements class to scan the updated CSVs
        if product_type == "edible":
            product = Edibles(cannabanoid_path, heavy_metals_path, microbio_path, myco_path)
            profile = product.edible_profile()
        elif product_type == "vape":
            product = Vapes(cannabanoid_path, heavy_metals_path, microbio_path, myco_path)
            profile = product.vape_profile()
        elif product_type == "concentrate":
            product = Concentrates(cannabanoid_path, heavy_metals_path, microbio_path, myco_path)
            profile = product.concentrate_profile()
        else:
            return "Invalid product type"

        # Get the METRC tag from the user
        product_id = self.get_product_id()
        self.library.add_product(product_id, profile)
        self.export_to_csv()
        return profile


    def get_past_results(self, product_type=None, product_id=None):
        """
        Fetch past results based on product type or product ID.

        :param product_type: The type of the product (optional).
        :param product_id: The METRC tag of the product (optional).
        :return: A dictionary containing the product profiles matching the criteria.
        """
        if product_id:
            return {product_id: self.library.get_product(product_id)}
        
        if product_type:
            return {pid: profile for pid, profile in self.library.products.items() if profile['type'] == product_type}
        
        return self.library.products


    def generate_historical_report(self, product_type):
        """
        Generate a historical report for a given product type.

        :param product_type: The type of the product.
        :return: A dictionary containing the historical report data or None if no data is available.
        """
        products_of_type = [profile for profile in self.library.products.values() if profile['type'] == product_type]

        if not products_of_type:
            return None

        avg_TAC = sum(float(str(product['TAC']).split()[0]) for product in products_of_type) / len(products_of_type)
        avg_THC = sum(float(str(product['THC']).split()[0]) for product in products_of_type) / len(products_of_type)

        # Count the number of passes for each test
        heavy_metals_passes = sum(1 for product in products_of_type if product['Heavy Metals'] == 'PASS')
        microbials_passes = sum(1 for product in products_of_type if product['Microbials'] == 'PASS')
        mycotoxins_passes = sum(1 for product in products_of_type if product['Mycotoxins'] == 'PASS')

        # Calculate the percentage of passes for each test
        heavy_metals_percentage = (heavy_metals_passes / len(products_of_type)) * 100
        microbials_percentage = (microbials_passes / len(products_of_type)) * 100
        mycotoxins_percentage = (mycotoxins_passes / len(products_of_type)) * 100

        report = {
            'Average TAC': avg_TAC,
            'Average THC': avg_THC,
            'Total Products': len(products_of_type),
            'Heavy Metals Pass Percentage': heavy_metals_percentage,
            'Microbials Pass Percentage': microbials_percentage,
            'Mycotoxins Pass Percentage': mycotoxins_percentage
        }

        return report
    
    def export_to_csv(self, filename="AutoLabel.csv"):
        """
        Export the product library to a CSV file.

        :param filename: The name of the CSV file (default is "AutoLabel.csv").
        """
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Product ID', 'Type', 'TAC', 'THC', 'Heavy Metals', 'Microbials', 'Mycotoxins']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for product_id, profile in self.library.products.items():
                writer.writerow({
                    'Product ID': product_id,
                    'Type': profile['type'],
                    'TAC': profile['TAC'],
                    'THC': profile['THC'],
                    'Heavy Metals': profile['Heavy Metals'],
                    'Microbials': profile['Microbials'],
                    'Mycotoxins': profile['Mycotoxins']
                })
    