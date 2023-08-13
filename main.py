from Model.pdfscrape import PDFScrape

file_path = '/Users/dom/Final_project/test_result1.pdf'  # Path to a sample PDF file for testing
scraper = PDFScrape(file_path)

data_frames = scraper.extract_data()
scraper.csv_output(data_frames)