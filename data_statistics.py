from DataReporter.Config import Config
from DataReporter.ColumnReporter import ColumnReporter
from DataReporter.Report import *
from DataReporter.FileReader import FileReader
import matplotlib.pyplot as plt
import click

@click.command()
@click.option('--input_file' , '-i',  help='input file (with suffixes: csv,xlsx)')
@click.option('--output_format', '-f' , help='otuput format (htmlH|text|T) - default is html)')
@click.option('--output_dir', '-D', help='DIR_NAME output dirctory name)')
def main(input_file,output_format,output_dir):
    config=Config()
    fr=FileReader(file_name=input_file,file_type='csv',config=config)
    df=fr.read_data()

    reporter=HTMLReport(input_file,df,config)
    text= reporter.run()


    with open('d:\\tmp\\1.html', 'w') as out_file:
        out_file.write(text)


if __name__ == '__main__':
    main()