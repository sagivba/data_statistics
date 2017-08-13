from DataReporter.Config import Config
# from DataReporter.ColumnReporter import ColumnReporter
from DataReporter.Report import *
from DataReporter.FileReader import FileReader
# import matplotlib.pyplot as plt
import click
from time import time
def verbose (text):
    print(text)
@click.command()
@click.option('--input_file' ,   '-i',
              help='input file (with suffixes: csv,xlsx)',
              )

@click.option('--output_format', '-f' ,
              help='otuput format (HTML|H|TEXT|T) - default is html)',
              type=click.Choice(['HTML','H','TEXT','T']),
              default="HTML")
@click.option('--output_dir',    '-D',
               help='DIR_NAME output dirctory name)',
               default="out{}".format(time()))
def main(input_file,output_format,output_dir):
    config=Config()
    config.FIG_PATH_LIST=[output_dir,'Fig']
    verbose ("input_file: '{}'".format(input_file))
    verbose ("fig dir   : '{}'".format(config.fig_path("")))
    fr=FileReader(file_name=input_file,file_type='csv',config=config)
    df=fr.read_data()
    if str(output_format).upper() in ['TEXT','T']:
        reporter=TEXTReport(input_file,df,config)
        out_file="{}\\report.text".format(output_dir)
    elif str(output_format).upper() in ['HTML','H']:
        reporter = HTMLReport(input_file, df, config)
        out_file="{}\\report.html".format(output_dir)
    else:
        raise ValueError("not valid {}".format(output_format))
    verbose("out_file   : '{}'".format(out_file))
    text= reporter.run()
    print(text)
    with open(out_file, 'w') as out_file:
        out_file.write(text)


if __name__ == '__main__':
    main()