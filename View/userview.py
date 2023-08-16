from Controller.controller import Controller
from Model.resultlibrary import ResultsLibrary

class View:
    """
    Provides an interface for the user to interact with the application.
    Displays menus, accepts user input, and presents the results.
    """
    def __init__(self, controller) -> None:
        """
        Initializes the View with a given controller.

        Args:
            controller: The controller instance to handle the business logic.
        """
        self.controller = controller

    def display_menu(self) -> None:
        """
        Displays the main menu options to the user.
        """
        print("\nMenu:")
        print("1. Scrape a new PDF")
        print("2. List past results")
        print("3. Generate a historical report")
        print("4. View a specific product by ID")
        print("5. Remove a product by ID")
        print("6. Exit")

    def display_past_results(self, results: dict) -> None:
        """
        Displays the past results in a formatted manner.

        Args:
            results (dict): A dictionary containing product profiles.
        """
        print("\nResults:")
        header = "{:<12} | {:<12} | {:<10} | {:<10} | {:<15} | {:<10} | {:<10}"
        print(header.format("Product ID", "Type", "TAC", "THC", "Heavy Metals", "Microbials", "Mycotoxins"))
        print("-" * 95)  # separator

        for product_id, profile in results.items():
            print(header.format(
                product_id, 
                profile['type'], 
                profile['TAC'], 
                profile['THC'], 
                profile['Heavy Metals'], 
                profile['Microbials'], 
                profile['Mycotoxins']
            ))
        print("-" * 95)  # separator

    def display_historical_report(self, report: dict) -> None:
        """
        Displays the historical report in a formatted manner.

        Args:
            report (dict): A dictionary containing the historical report data.
        """
        print("\nHistorical Report:")
        print("-" * 40)  # separator
        print(f"Average TAC: {report['Average TAC']:.2f}")
        print(f"Average THC: {report['Average THC']:.2f}")
        print(f"Total Products: {report['Total Products']}")
        print(f"Heavy Metals Pass Percentage: {report['Heavy Metals Pass Percentage']}%")
        print(f"Microbials Pass Percentage: {report['Microbials Pass Percentage']}%")
        print(f"Mycotoxins Pass Percentage: {report['Mycotoxins Pass Percentage']}%")
        print("-" * 40)  # separator

    def run(self) -> None:
        """
        The main loop of the application. It keeps running until the user decides to exit.
        """
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1": #scrape pdf
                #failsafe for filepath
                while True:
                    file_path = input("Enter the file path of the PDF: ")
                    if os.path.exists(file_path) and file_path.endswith('.pdf'):
                        break
                    else:
                        print("Invalid file path or not a PDF. Please enter a valid PDF file path.")
                #failsafe for product type
                while True:
                    product_type = input("Enter the product type (edible, vape, concentrate): ")
                    if product_type in ['edible', 'vape', 'concentrate']:
                        break
                    else:
                        print("Invalid product type. Please enter 'edible', 'vape', or 'concentrate'.")
                #returns & prints profile
                profile = self.controller.scrape_new_pdf(file_path, product_type)
                if profile:
                    print("Scraped Profile:", profile)
                else:
                    print("Failed to scrape the PDF.")

            #listing past results
            elif choice == "2":
                #failsafe product type
                while True:
                    product_type = input("Enter the product type to filter (edible, vape, concentrate) or press Enter to skip: ")
                    if not product_type or product_type in ['edible', 'vape', 'concentrate']:
                        break
                    else:
                        print("Invalid product type. Please enter 'edible', 'vape', or 'concentrate' or leave it blank.")
                #failsafe product ID
                while True:
                    product_id = input("Enter the product ID to filter or press Enter to skip: ")
                    if not product_id or product_id in self.controller.library.products:  # Assuming the library has a dictionary called products
                        break
                    else:
                        print("Invalid product ID. Please enter a valid product ID or leave it blank.")
                #display result or not
                results = self.controller.get_past_results(product_type=product_type if product_type else None, product_id=product_id if product_id else None)
                if results:
                    self.display_past_results(results)
                else:
                    print("No results found for the specified criteria.")

            elif choice == "3":
                #failsafe product type
                while True:
                    product_type = input("Enter the product type for the historical report (edible, vape, concentrate): ")
                    if product_type in ['edible', 'vape', 'concentrate']:
                        break
                    else:
                        print("Invalid product type. Please enter 'edible', 'vape', or 'concentrate'.")
                report = self.controller.generate_historical_report(product_type)
                if report:  # Check if the report is not None
                    self.display_historical_report(report)
                else:
                    print("No data available for the specified product type.")

            elif choice == "4":
                product_id = input("Enter the product ID to view: ")
                product = self.controller.get_product(product_id)
                if product:
                    self.display_past_results({product_id: product})
                else:
                    print(f"No product found with ID {product_id}.")

            elif choice == "5":
                product_id = input("Enter the product ID to remove: ")
                removed = self.controller.remove_product(product_id)
                if removed:
                    print(f"Product with ID {product_id} removed successfully.")
                else:
                    print(f"No product found with ID {product_id}.")

            elif choice == "6":
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    library = ResultsLibrary()  # Create an instance of ResultsLibrary
    controller = Controller(library)  # Pass the library to the Controller
    view = View(controller)  # Pass the controller to the View
    view.run()
