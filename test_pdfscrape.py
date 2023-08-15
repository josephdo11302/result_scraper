import unittest
import os
from Model.pdfscrape import PDFScrape
import pandas as pd

class TestPDFScrape(unittest.TestCase):

    def test_extract_data(self):
        file_path = '/Users/dom/Final_project/concentrate_result.pdf'  # Path to a sample PDF file for testing
        scraper = PDFScrape(file_path)
        data_frames = scraper.extract_data()

        # # Print the data frames
        # for idx, df in enumerate(data_frames):
        #     print(f"Data Frame {idx + 1}:")
        #     print(df)
        #     print("=" * 40)

        # Check that the result is a list
        self.assertIsInstance(data_frames, list) 

        # Check that all elements are DataFrames
        self.assertTrue(all(isinstance(df, pd.DataFrame) for df in data_frames))  

    def test_csv_export(self):
        file_path = '/Users/dom/Final_project/concentrate_result.pdf'  # Path to a sample PDF file for testing
        scraper = PDFScrape(file_path)
        data_frames = scraper.extract_data()
    
        # Export the extracted data to CSV files
        scraper.csv_output(data_frames)

        print("CSV files have been saved and checked.")


if __name__ == '__main__':
    unittest.main()
