class DataInfo:
    """
    return dict of info about data frame
    """

    def __init__(self, df, config):
        self.config = config
        self.df = df

        self.info_dict = {
            "Number of Records": df.count(),
            "Number of columns": len(list(df)),
            "Columns Names": list(df)
        }
