import unittest

from DataUtils.FileReader import *
from DataUtils.Reporter.Config import *


class TestFileReader(unittest.TestCase):
    def setUp(self):
        self.config = Config()
        self.columns_names = ["sepal length", "sepal width", "petal length", "petal width", "class"]
        self.excel_file_name = os.path.join(*["Data", "iris.data.xlsx"])
        self.csv_file_name = os.path.join(*["Data", "iris.data.csv"])

        self.iris_classes = ["setosa", "versicolor", "virginica"]

    def test_read_csv(self):
        fr = FileReader(self.csv_file_name, "csv", self.config)
        df = fr.read_data()
        self.assertTrue(fr.file_name == self.csv_file_name)
        self.assertTrue(len(list(df)) == len(self.columns_names), "columns number")
        sepal_length = df["sepal length"]
        self.assertTrue(len(sepal_length) == 150, "columns number")
        unq = sorted(list(df["class"].unique()))
        self.assertTrue(set(unq) == set(self.iris_classes), "iris_classes")

    def test_read_excel(self):
        fr = FileReader(self.excel_file_name, "excel", self.config)
        df = fr.read_data(sheetname="iris.data")
        self.assertTrue(fr.file_name == self.excel_file_name)
        self.assertTrue(len(list(df)) == len(self.columns_names), "columns number")
        sepal_length = df["sepal length"]
        self.assertTrue(len(sepal_length) == 150, "columns number")
        unq = sorted(list(df["class"].unique()))
        self.assertTrue(set(unq) == set(self.iris_classes), "iris_classes")
