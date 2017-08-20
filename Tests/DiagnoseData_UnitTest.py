import unittest

from DataReporter.ColumnReporter import DiagnoseData


class TestDiagnoseData(unittest.TestCase):
    def setUp(self):
        self.mostly_int_set1 = (1, 2, 3, 4, 5, 6, 7, 2.1, 0, -1)
        self.mostly_int_set2 = (1, 2, 3, 4, 5, 6, 7, None, 0, -1)
        self.mostly_int_set3 = (1, 2, 3, 4, 5, 6, 7, "one", 0, -1)
        self.mostly_float_set = (1.1, 2.3, 3.3, 4.0, 5, 2.1, "6.0", "two")

    def test_DiagnoseDataInt1(self):
        diagnoser = DiagnoseData("integers", self.mostly_int_set1)
        diagnoser.diagnose()
        self.assertTrue(type(diagnoser) is DiagnoseData, "type test")
        self.assertTrue(diagnoser.is_mostly_integer(), str(self.mostly_int_set1) + " is_mostly_integer")
        self.assertEqual(diagnoser.exceptions_values, {2.1}, "exceptions_values")
        self.assertEqual((diagnoser.get_min(), diagnoser.get_max()), (-1, 7), "min max")

    def test_DiagnoseDataInt2(self):
        diagnoser = DiagnoseData("integers", self.mostly_int_set2)
        diagnoser.diagnose()
        self.assertTrue(type(diagnoser) is DiagnoseData, "type test")
        self.assertTrue(diagnoser.is_mostly_integer(), str(self.mostly_int_set1) + " is_mostly_integer")
        self.assertEqual(diagnoser.exceptions_values, {None}, "exceptions_values")
        self.assertEqual((diagnoser.get_min(), diagnoser.get_max()), (-1, 7), "min max")

    def test_DiagnoseDataInt3(self):
        diagnoser = DiagnoseData("integers", self.mostly_int_set3)
        diagnoser.diagnose()
        self.assertTrue(type(diagnoser) is DiagnoseData, "type test")
        self.assertTrue(diagnoser.is_mostly_integer(), str(self.mostly_int_set1) + " is_mostly_integer")
        self.assertEqual(diagnoser.exceptions_values, {"one"}, "exceptions_values")
        self.assertEqual((diagnoser.get_min(), diagnoser.get_max()), (-1, 7), "min max")

    def test_DiagnoseDataFloat(self):
        diagnoser = DiagnoseData("floats", self.mostly_float_set)
        self.assertTrue(diagnoser.is_mostly_float(), str(self.mostly_float_set) + " is_mostly_float")
        self.assertEqual(set(diagnoser.exceptions_values), set({'two'}), "exceptions_values")
        clean_data = set(diagnoser.clean_data)
        self.assertEqual(clean_data, set([1.1, 2.3, 3.3, 4.0, 5, 2.1, 6.0]), "clean_data")

    def test_diagnose(self):
        diagnoser = DiagnoseData("integers", self.mostly_int_set1)
        diagnose = diagnoser.diagnose()
        self.assertEqual(diagnose['Accuracy'], 0.9, "diagnose Aurracy")
        self.assertEqual(diagnose["Type"], 'Mostly Integer', "diagnose Type")
