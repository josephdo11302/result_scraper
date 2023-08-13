class ResultLibrary:
    def __init__(self):
        self.results = {}

    def add_result(self, product_type, result):
        self.results[product_type] = result

    def get_result(self, product_type):
        return self.results.get(product_type)