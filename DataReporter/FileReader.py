import pandas as pd


# import logging
class FileReader():
    """read file into DataFrame"""
    def __init__(self,file_name,file_type,config):
        self.config = config
        self.file_name=file_name
        self.rf_dict={
                "csv":pd.read_csv,
                "excel":pd.read_excel,
                "json":pd.read_json
        }
        if not file_type in self.rf_dict:
            raise ValueError("file type: {} is not valid - not in {}".
                             format(file_type,self.rf_dict.keys()))
        self.file_type=file_type

        # logging.basicConfig(filename=config.LOG_NAME, format=config.LOG_FORMAT, filemode='w', level=config.LOG_LEVEL)

        return

    def verbose(self, text):
        if self.config.is_verbose: print(text)

    def read_data(self, *args, **kwargs):
        _read_file=self.rf_dict[self.file_type]
        self.df = _read_file(
            self.file_name,
            *args, **kwargs
        )

        self.verbose("data was loaded from {}".format(self.file_name))
        return self.df