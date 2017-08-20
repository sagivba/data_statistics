from  DataReporter.ColumnReporter import ColumnReporter
from  DataReporter.DataInfo import DataInfo


# import pprint


class Report():
    """creates html or text report from report_data_lst """

    def __init__(self, report_name, df, config):
        self.df = df
        self.config = config
        self.report = ""
        self.report_name = report_name

    def verbose(self, text):
        if self.config.is_verbose: print(text)

    def run(self):

        _df = self.df
        self.report = self.report_header("ll") + "\n"
        self.report += self.report_data_info(DataInfo(_df, self.config).info_dict)

        for col_name in _df:
            col_report = ColumnReporter(_df[col_name], self.config)
            col_report_dict = col_report.report()
            self.report += self.format(col_report_dict)

        return self.report

    def format_data_info_line(self, lbl, data_info_dict):
        return "{}:{}\n".format(lbl, data_info_dict[lbl])

    def report_data_info(self, data_info_dict):
        text = ""
        for lbl in ["Number of Records", "Number of columns", "Empty values", "Columns Names"]:
            line = self.format_data_info_line(lbl, data_info_dict)
            text += line
        return self.container(text)

    def report_header(self, text):
        return text

    def container(self, text):
        return text

    def info(self, text):
        return text

    def show_plot(self, img):
        return img

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
        info += self.h3("data_type: {}".format(_crd["data_dype"]))
        info += self.h3("uniq:")
        info += self.div(_crd["unique_values"])
        info += self.div(self.h3("statistic_info:") + str_statistic_info(_crd["statistic_info"]))
        text += self.info(info)
        if _crd["plot_object"]:
            plot += self.showimg(_crd["plot_object"])
            text += self.show_plot(plot)
        text = self.container(h1 + text)
        return text


class HTMLReport(Report):
    def format_data_info_line(self, lbl, data_info_dict):
        return "<li>{}:{}</li>\n".format(lbl, data_info_dict[lbl])

    # def report_data_info(self, data_info_dict):
    #     text = "<div class='col-sm-12' >\n<ul>"
    #     text += "<li>{}:{}</li>\n".format("Number of Records", data_info_dict["Number of Records"])
    #     text += "<li>{}:{}</li>\n".format("Number of columns", data_info_dict["Number of columns"])
    #     text += "<li>{}:{}</li>\n".format("Columns Names", data_info_dict["Columns Names"])
    #     text += "</ul>\n</div>\n"
    #
    #     return self.container(text)

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
        return '<div class="container">\n{}\n</div>\n\n'.format(text)

    def info(self, text):
        return '<div class="col-sm-6">\n{}</div>\n'.format(text)

    def show_plot(self, img):
        return '<div class="col-sm-6">\n{}</div>\n'.format(img)

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
        return "<img src='{}' alt='plot:{}' width='80%%' >\n".format(img_path, img_path)

    def new_line(self):
        return "<br/>\n"


class TEXTReport(Report):
    def h_i(self, chr, text):
        return "\n{}{}{} {} {}{}{}\n".format(chr, chr, chr, text, chr, chr, chr)

    def h1(self, text):
        return self.h_i('#', text)

    def h2(self, text):
        return self.h_i('*', text)

    def h3(self, text):
        return self.h_i('=', text)

    def h4(self, text):
        return self.h_i('-', text)

    def h5(self, text):
        return self.h_i('.', text)

    def h6(self, text):
        return self.h_i(' ', text)
