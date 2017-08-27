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

    def __init__(self, path_list=[], fig_path='Fig', is_verbose=False):
        pd.set_option('expand_frame_repr', False)
        self.is_verbose = is_verbose
        get_path_list = lambda path, file: path[:] + [file]
        get_path = lambda path, file: os.path.join(*get_path_list(path, file))
        self.PATH_LIST = path_list
        self.FIG_DIR = fig_path
        self.LOG_FORMAT = '{:10} {}: {} '.format(
            "[%(levelname)s]", "%(module)20s.%(funcName)-20s", "%(message)s")

        self.LOG_LEVEL = logging.INFO

    def fig_path(self, fig_name, is_absolute=True):
        """
        return fig path for the exploration
        all figures will be kept in one dir
        :param fig_name: figure name
        :return:
        """
        if is_absolute:
            fig_path_lst = self.PATH_LIST + [self.FIG_DIR]
        else:
            fig_path_lst = [self.FIG_DIR]

        fig_dir = os.path.join(*fig_path_lst)
        if not os.path.exists(fig_dir):
            os.makedirs(fig_dir)
        fpl = [fig_dir, fig_name]
        return os.path.join(*fpl)
