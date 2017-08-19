from DataReporter.FileReader import *
from DataReporter.ColumnReporter import *
from DataReporter.Config import *
import unittest


class TestColumnReporter(unittest.TestCase):
    def setUp(self):
        self.config = Config()
        self.columns_data = {
            "sepal length": {"dtype": "float64"},
            "sepal width": {"dtype": "float64"},
            "petal length": {"dtype": "float64"},
            "petal width": {"dtype": "float64"},
            "class": {"dtype": "object"}
        }
        self.iris_classes = ["setosa", "versicolor", "virginica"]
        self.excel_file_name = os.path.join(*["Data", "iris.data.xlsx"])
        fr = FileReader(self.excel_file_name, "excel", self.config)
        self.df = fr.read_data(sheetname="iris.data")

    def test_conclude_data_type(self):
        _df = self.df
        for col in self.columns_data:
            self.assertTrue(col in _df.columns.values)
            expexted = self.columns_data[col]
            cr = ColumnReporter(_df[col], self.config)
            self.assertTrue(str(cr.conclude_data_type()) == expexted["dtype"])

    def test_unique(self):
        _df = self.df
        cr = ColumnReporter(_df["class"], self.config)
        self.assertTrue(cr.unique() == str(", ".join(sorted(self.iris_classes))), "iris_classes")


        # def test_statistics(self):
        #     pass
