class DataInfo:
    """
    return dict of info about data frame
    """

    def __init__(self, df, config):
        self.config = config
        self.df = df
        self.Number_of_columns = len(list(df))
        self.Number_of_Records = len(df)
        self.number_of_empty = df.isnull().sum().sum()
        self.info_dict = {
            "Number of Records": self.Number_of_Records,
            "Number of columns": self.Number_of_columns,
            "Empty values": "{:.3f}%".format(
                self.number_of_empty / float(self.Number_of_Records * self.Number_of_columns)),
            "Columns Names": list(df),

        }
