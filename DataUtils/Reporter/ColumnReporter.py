import statistics

from  MachineLearningUtils.UsefulPlots import *

__version__ = '0.0.2'

class ColumnReporter():
    """process one column of data"""

    def __init__(self, data_column, config):
        self.data_column = data_column
        self.config = config

    def verbose(self, text):
        if self.config.is_verbose: print(text)

    def report(self):
        """
        
        :return:  report data Structure:
         { 
            name: "",
            uniq_values:[]
            data_dype: [numeric| categoricial]
            plot object
            statistic info
         
         }
        """
        _data = self.data_column
        self.plot()
        self.report_dict = {
            "name": _data.name,
            "unique_values": self.unique(),
            "data_type": str(self.conclude_data_type()),
            "plot_object": self.rel_fig_path,
            "statistic_info": self.statistics()
        }

        return self.report_dict

    def statistics(self):
        statistic_dict = {}
        _data = self.data_column[self.data_column.notnull()]

        if str(self.data_column.dtype) != 'object':
            try:
                statistic_dict["median "] = str(_data.median())
            except:
                pass
            try:
                statistic_dict["mean"] = str(_data.mean())
            except:
                pass
            try:
                statistic_dict["max"] = str(_data.max())
            except:
                pass
            try:
                statistic_dict["min"] = str(_data.min())
            except:
                pass
        try:
            statistic_dict["mode"] = ";".join(map(str, list(_data.mode())))
        except:
            pass
        self.mostly()
        statistic_dict["mostly type:"] = self.diagnose_mostly["Type"]
        statistic_dict["mostly accuracy:"] = self.diagnose_mostly["Accuracy"]

        return statistic_dict

    def plot(self, save=True):
        fig_file_name = "{}.png".format(str(self.data_column.name).replace(' ', '_'))
        self.abs_fig_path = self.config.fig_path(fig_file_name, is_absolute=True)
        self.rel_fig_path = self.config.fig_path(fig_file_name, is_absolute=False)
        plotter = DataPlots()
        fig = plotter.plot_column(self.data_column)
        self.verbose("plot path:  '{}'".format(self.abs_fig_path))
        if save:
            fig.savefig(self.abs_fig_path)
        return fig

    def unique(self):
        _data = self.data_column
        uniq_vals = _data.unique()
        uv = sorted(list(map(str, uniq_vals)))
        if len(uv) > 20:
            uv = map(str, uv[0:9] + ["..."] + uv[-9:-1])
        return ", ".join(uv)

    def conclude_data_type(self):
        return self.data_column.dtype

    def mostly(self):
        name = self.data_column.name
        diagnoser = DiagnoseData(name, self.data_column)
        self.diagnose_mostly = diagnoser.diagnose()
        return self.diagnose_mostly


class DiagnoseData():
    def __init__(self, header, data, sensitivity_level=0.75):
        self.data = data
        self.header = header
        self.suspected_rows_dict = dict()
        self.suspected_rows_tmp = dict()
        self.clean_data = []
        self.counter = 0
        self.others_type_counter = 0
        self.sensitivity_level = sensitivity_level
        self.exceptions_values = set([])
        self.accuracy_level = 0
        self.mostly_type = None
        self.statistic_info = {
            "min": None,
            "max": None,
            "median": None,
            "variance": None,
            "mean": None,
            "mode": None,
            "cardinality": None
        }

    def set_statatistics(self, keys=None):
        if keys == None:
            keys = self.statistic_info.keys()
        if "cardinality" in keys: self.statistic_info["cardinality"] = len(set(self.clean_data))
        if "min" in keys: self.statistic_info["min"] = min(self.clean_data)
        if "max" in keys: self.statistic_info["max"] = max(self.clean_data)
        if "mean" in keys: self.statistic_info["mean"] = statistics.mean(self.clean_data)
        if "median" in keys: self.statistic_info["median"] = statistics.median(self.clean_data)
        try:
            if "mode" in keys: self.statistic_info["mode"] = statistics.mode(self.clean_data)
        except statistics.StatisticsError:
            pass
        if len(self.clean_data) > 1 and "variance" in keys:
            self.statistic_info["variance"] = statistics.variance(self.clean_data)

    def is_mostly_some_function(self, function, convertor):
        self.exceptions_values = set([])
        self.counter = 0
        self.others_type_counter = 0
        for element in self.data:
            if function(element):
                try:
                    self.counter += 1
                    converted_element = convertor(element)
                    self.clean_data.append(converted_element)
                except:
                    pass
                if self.statistic_info["min"] is None or converted_element < self.statistic_info["min"]:
                    self.statistic_info["min"] = converted_element
                if self.statistic_info["max"] is None or converted_element > self.statistic_info["max"]:
                    self.statistic_info["max"] = converted_element
            else:
                self.others_type_counter += 1
                self.exceptions_values.add(element)
                tmp_set = self.suspected_rows_tmp.setdefault(self.counter - 1, set())
                tmp_set.add(self.header)
                self.suspected_rows_tmp[self.counter - 1] = tmp_set
        if len(self.clean_data) == 0:
            # this is unknown type so clean_data is the data
            self.clean_data = self.data

        return self.is_mostly(self.counter, len(self.data))

    def is_mostly_integer(self):
        return self.is_mostly_some_function(DiagnoseData.is_int, DiagnoseData.to_int)

    def is_mostly_float(self):
        return self.is_mostly_some_function(DiagnoseData.is_float, float)

    def is_mostly(self, counter, total, sensitivity_level=None):
        if not sensitivity_level: sensitivity_level = self.sensitivity_level
        self.accuracy_level = counter / total
        return self.accuracy_level >= sensitivity_level

    def diagnose(self):
        self.mostly_type = "Unknown"
        if self.is_mostly_integer():
            self.mostly_type = "Mostly Integer"
            self.suspected_rows_dict = self.suspected_rows_tmp
            if len(self.clean_data) > 0:
                self.set_statatistics()
        elif self.is_mostly_float():
            self.mostly_type = "Mostly Float"
            self.suspected_rows_dict = self.suspected_rows_tmp
            if len(self.clean_data) > 0:
                self.set_statatistics()
        if self.mostly_type == "Unknown":
            self.accuracy_level = 0
            self.set_statatistics(["cardinality", "mode"])
        return {"Type": self.mostly_type, "Accuracy": self.accuracy_level}

    def text_statistic_info(self):
        ret_val = ""
        keys = ["cardinality", "min", "max", "median", "variance", "mean", "mode"]

        for k in keys:
            v = self.statistic_info.get(k)
            if v:
                v_format = "{}"
                if self.is_int(v):
                    v_str = v_format.format(v)
                elif self.is_float(v):
                    v_format = "{:.2f}"
                    v_str = v_format.format(float(v))
                else:
                    v_str = v_format.format(v)
                ret_val += k + ": " + v_str + ";  "
        return ret_val

    def get_min(self):
        return self.statistic_info.get("min")

    def get_max(self):
        return self.statistic_info.get("max")

    @staticmethod
    def to_int(val):
        return int(float(val))

    @staticmethod
    def is_int(val):
        if val is None:
            return False
        if type(val) == int:
            return True
        if type(val) == float:
            return val.is_integer()
        try:
            DiagnoseData.to_int(val)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_float(val):
        if val is None:
            return False
        if type(val) == float:
            return True
        try:
            float(val)
            return True
        except ValueError:
            return False
