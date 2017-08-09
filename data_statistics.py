from DataReporter.Config import Config
from DataReporter.ColumnReporter import ColumnReporter
from DataReporter.Report import *
from DataReporter.FileReader import FileReader
import matplotlib.pyplot as plt

config=Config()
in_file_name='prices.csv'
fr=FileReader(file_name=".\\data\\{}".format(in_file_name),file_type='csv',config=config)
# fr=FileReader(file_name=".\\data\\INBALTU2.xlsx",file_type='excel',config=config)
df=fr.read_data()
reporter=HTMLReport(in_file_name,df,config)
text= reporter.run()


with open('d:\\tmp\\1.html', 'w') as out_file:
    out_file.write(text)

