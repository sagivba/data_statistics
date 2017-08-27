from  DataUtils.Reporter.ColumnReporter import ColumnReporter
from  DataUtils.Reporter.DataInfo import DataInfo
from MachineLearningUtils.UsefulPlots import DataPlots
import json

class Report():
    """creates html or text report from report_data_lst """

    def __init__(self, report_name, df, config):
        self.df = df
        self.config = config
        self.report = ""
        self.report_name = report_name

    def verbose(self, text):
        if self.config.is_verbose: print(text)

    def run(self, target=None):

        _df = self.df
        _data_info_dict = DataInfo(_df, self.config).info_dict

        self.report_lst = []
        self.report_lst.append({"report_header": self.report_name})
        self.report_lst.append({"report_data_info": _data_info_dict})

        self.report = self.report_header(self.report_name) + "\n"

        self.scatter_matrix_abs_path = None
        self.scatter_matrix_rel_path = None
        if target:
            self.plot_scatter_matrix(target=target, save=True)
        rdinf = self.report_data_info(_data_info_dict, self.scatter_matrix_rel_path)
        self.report += rdinf
        self.report_lst.append({"scatter_matrix": self.scatter_matrix_rel_path})

        columns_report_lst = []
        for col_name in _df:
            col_report = ColumnReporter(_df[col_name], self.config)
            col_report_dict = col_report.report()
            columns_report_lst.append(col_report_dict)
            self.report += self.format(col_report_dict)
        self.report_lst.append({"columns_report": columns_report_lst})


        return self.report

    def format_data_info_line(self, lbl, data_info_dict):
        return "{}:{}\n".format(lbl, data_info_dict[lbl])

    def report_data_info(self, data_info_dict, scatter_matrix_fig_path=None):
        text = ""
        data_info_lines = []
        for lbl in ["Number of Records", "Number of columns", "Empty values", "Columns Names"]:
            data_info_lines.append({lbl: data_info_dict})
            line = self.format_data_info_line(lbl, data_info_dict)
            text += line
        self.report_lst.append({"data_info": data_info_lines})
        if scatter_matrix_fig_path is not None:
            text += self.showimg(scatter_matrix_fig_path, None)
        return self.container(self.ul(text))

    def report_header(self, text):
        return str(text)

    def container(self, text):
        return str(text)

    def info(self, text):
        return str(text)

    def show_plot(self, img):
        return img

    def ul(self, text):
        return str(text)

    def h_i(self, chr, text):
        return "\n{}{}{} {} {}{}{}\n".format(chr, chr, chr, text, chr, chr, chr)

    def h1(self, text):
        return self.h_i('=', text)

    def h2(self, text):
        return self.h_i('=', text)

    def h3(self, text):
        return self.h_i('=', text)

    def h4(self, text):
        return self.h_i('=', text)

    def h5(self, text):
        return self.h_i('=', text)

    def h6(self, text):
        return self.h_i('=', text)

    def div(self, text):
        return "{}\n".format(text)

    def new_line(self):
        return "\n"

    def showimg(self, img_path):
        return "image: '{}'\n".format(img_path)

    def format(self, col_report_dict):
        _crd = col_report_dict

        def str_statistic_info(si):
            si_text = ""
            for k in sorted(si):
                si_text += "\n\t{:<10} : {}{}".format(k, si[k], self.new_line())
            return si_text + "\n"

        info = ""
        plot = ""
        text = ""

        h1 = self.h1("{}".format(_crd["name"]))
        info += self.h3("data_type: {}".format(_crd["data_type"]))
        info += self.h3("uniq:")
        info += self.div(_crd["unique_values"])
        info += self.div(self.h3("statistic_info:") + str_statistic_info(_crd["statistic_info"]))
        text += self.info(info)
        if _crd["plot_object"]:
            plot += self.showimg(_crd["plot_object"], None)
            text += self.show_plot(plot)
        text = self.container(h1 + text)
        return text

    def plot_scatter_matrix(self, target, save=True):
        plotter = DataPlots(df=self.df)
        fig = plotter.colored_scatter_matrix(df=self.df, colored_column_name=target)
        fig_file_name = "scatter_matrix-{}.png".format(target)
        self.scatter_matrix_abs_path = self.config.fig_path(fig_file_name, is_absolute=True)
        self.scatter_matrix_rel_path = self.config.fig_path(fig_file_name, is_absolute=False)
        self.verbose("plot path:  '{}'".format(self.scatter_matrix_abs_path))
        if save:
            fig.savefig(self.scatter_matrix_abs_path)
        return fig


class JSONReport(Report):
    def run(self, target=None):
        Report.run(self, target=target)
        jsnencdr = json.JSONEncoder()

        json_report = jsnencdr.encode(o=self.report_lst)
        return json_report

class HTMLReport(Report):
    def format_data_info_line(self, lbl, data_info_dict):
        return "<li>{}:{}</li>\n".format(lbl, data_info_dict[lbl])

    def report_header(self, text):
        header = '<!DOCTYPE html>\n'
        header += '<html lang="en">\n'
        header += '<head>\n'
        header += '  <title>data statistics</title>\n'
        header += '  <meta charset="utf-8">\n'
        header += '  <meta name="viewport" content="width=device-width, initial-scale=1">\n'
        header += '  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">\n'
        header += '  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\n'
        header += '  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>\n'
        header += '</head>\n'
        header += '<body>\n'
        header += '<div class="jumbotron text-center">\n'
        header += '  <h1>{}</h1>\n'.format(self.report_name)
        header += '  \n'
        header += '</div>'
        return header

    def container(self, text):
        return '<div class="container-fluid">\n{}\n</div>\n\n'.format(text)

    def info(self, text):
        return '<div class="col-sm-6">\n{}</div>\n'.format(text)

    def show_plot(self, img):
        return '<div class="col-sm-6">\n{}</div>\n'.format(img)

    def ul(self, text):
        return "<ul>\n{}\n</ul>".format(text)
    def h_i(self, i, text):
        return "<h{}>{}</h{}>\n".format(i, text, i)

    def h1(self, text):
        return self.h_i(1, text)

    def h2(self, text):
        return self.h_i(2, text)

    def h3(self, text):
        return self.h_i(3, text)

    def h4(self, text):
        return self.h_i(4, text)

    def h5(self, text):
        return self.h_i(5, text)

    def h6(self, text):
        return self.h_i(6, text)

    def div(self, text):
        return "<div>\n\t{}\n</div>\n".format(text)

    def showimg(self, img_path):
        return "<img src='{}' alt='plot:{}' width='100%%' >\n".format(img_path, img_path)

    def new_line(self):
        return "<br/>\n"


class TEXTReport(Report):
    def report_header(self, text):
        return "***\n{}\n***\n".format(text)

    def format_data_info_line(self, lbl, data_info_dict):
        return "- {}:{}\n".format(lbl, data_info_dict[lbl])

    def h_i(self, n, text):
        return "{} {}\n".format('#' * n, text)

    def h1(self, text):
        return self.h_i(1, text)

    def h2(self, text):
        return self.h_i(2, text)

    def h3(self, text):
        return self.h_i(3, text)

    def h4(self, text):
        return self.h_i(4, text)

    def h5(self, text):
        return self.h_i(5, text)

    def h6(self, text):
        return self.h_i(6, text)

    def showimg(self, img_path, alt):
        _alt = alt
        if not _alt:
            _alt = img_path
        return "![{}]({})\n".format(_alt, img_path)
