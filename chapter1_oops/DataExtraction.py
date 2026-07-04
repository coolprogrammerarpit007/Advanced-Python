import pandas as pd

class DataExt:
    """
        This a DataExtraction class which has different methods for reading different type of file formats.
    """

    def __init__(self,file_path:str):
        self.file_path = file_path

    # def fetch_text(self,seperator):
    #     df = pd.re

    def fetch_csv(self):
        df = pd.read_csv(self.file_path)
        # head() is a preview function...
        print(df.head()) # by default it returns the first 5 rows of the table.

    def fetch_json(self):
        df = pd.read_json(self.file_path)
        print(df.head())


    def fetch_parquet(self):
        df = pd.read_parquet(self.file_path)
        print(df.head())

data1 = DataExt("./files/orders.csv")
data2 = DataExt("./files/orders.json")
# data3 = DataExt("./files/orders.tsv")
data4 = DataExt("./files/orders.parquet")
data1.fetch_csv()
data2.fetch_json()
data4.fetch_parquet()









