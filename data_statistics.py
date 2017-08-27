import os
from time import time

import click

from DataUtils.FileReader import FileReader
from DataUtils.Reporter.Config import Config
from DataUtils.Reporter.Report import *

__version__ = '0.0.4'

def verbose(text):
    print(text)


@click.command()
@click.option('--input_file', '-i',
              help='input file (with suffixes: csv,xlsx)',
              )
@click.option('--output_format', '-f',
              help='otuput format (HTML|H| TEXT|T |JSON|J) - default is html)',
              type=click.Choice(['HTML', 'H', 'TEXT', 'T', 'JSON', 'J']),
              default="HTML")
@click.option('--output_dir', '-D',
              help='DIR_NAME output dirctory name)',
              default="out{}".format(time()))
@click.option('--target', '-T',
              help='column to check vs other)'
              )
@click.option('--verbose', '-v',
              help='verbose mode',
              is_flag=True, default=False)
def main(input_file, output_format, output_dir, target, verbose):
    """
    A lean tool for obtaining statistics on flat data files
    output can be text or html
    """
    config = Config(path_list=[output_dir], is_verbose=verbose)
    fr = FileReader(file_name=input_file, file_type='csv', config=config)
    df = fr.read_data()
    report_name = os.path.basename(input_file)
    print("report_name: {}".format(report_name))
    if str(output_format).upper() in ['TEXT', 'T']:
        reporter = TEXTReport(report_name, df, config)
        out_file_name = os.path.join(output_dir, "report.md")

    elif str(output_format).upper() in ['HTML', 'H']:
        reporter = HTMLReport(report_name, df, config)
        out_file_name = os.path.join(output_dir, "report.html")

    elif str(output_format).upper() in ['JSON', 'J']:
        reporter = JSONReport(report_name, df, config)
        out_file_name = os.path.join(output_dir, "report.json")
    else:
        raise ValueError("not valid {}".format(output_format))
    reporter.verbose("input_file: '{}'".format(input_file))
    reporter.verbose("fig dir   : '{}'".format(config.fig_path("")))
    reporter.verbose("out_file  : '{}'".format(out_file_name))

    text = reporter.run(target=target)
    # print(text)
    with open(out_file_name, 'w') as out_file:
        out_file.write(text)

    print("\n\nout file: '{}'".format(out_file_name))


if __name__ == '__main__':
    main()
