import os
import logging
# from time import time
import pandas as pd


class Config:
    """
    this class is the configuration
    see comments below
    """
    __version__ = '0.0.2'

    def __init__(self, is_verbose=False):
        pd.set_option('expand_frame_repr', False)
        self.is_verbose = is_verbose
        get_path_list = lambda path, file: path[:] + [file]
        get_path = lambda path, file: os.path.join(*get_path_list(path, file))
        self.FIG_PATH_LIST = []
        self.LOG_FORMAT = '{:10} {}: {} '.format(
            "[%(levelname)s]", "%(module)20s.%(funcName)-20s", "%(message)s")

        self.LOG_LEVEL = logging.INFO

    def fig_path(self, fig_name):
        """
        return fig path for the exploration
        all figures will be kept in one dir
        :param fig_name: figure name
        :return:
        """
        fig_dir = os.path.join(*self.FIG_PATH_LIST)
        if not os.path.exists(fig_dir):
            os.makedirs(fig_dir)
        fpl = list(self.FIG_PATH_LIST)
        fpl.append(fig_name)
        return os.path.join(*fpl)
