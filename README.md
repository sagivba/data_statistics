# data_statistics
A lean tool for obtaining statistics on flat data files

## Usage Examples:
### get help
```
 [prompt]$ python data_statistics.py --help
Usage: data_statistics.py [OPTIONS]

  A lean tool for obtaining statistics on flat data files output can be text
  or html

Options:
  -i, --input_file TEXT           input file (with suffixes: csv,xlsx)
  -f, --output_format [HTML|H|TEXT|T]
                                  otuput format (HTML|H|TEXT|T) - default is
                                  html)
  -D, --output_dir TEXT           DIR_NAME output dirctory name)
  -v, --verbose                   verbose mode
  --help                          Show this message and exit.
```


### html output
## [example](output_example-iris_dataset\report.html)
```
prompt> python data_statistics.py -i "TestData\iris.data.csv" -D "d:\tmp\dout" -v
data was loaded from TestData\iris.data.csv
report_name: iris.data.csv
input_file: 'H:\DataMining\TestData\iris.data.csv'
fig dir   : 'd:\tmp\dout\Fig\'
out_file  : 'd:\tmp\dout\report.html'
plot path:  'd:\tmp\dout\Fig\scatter_matrix-class.png'
plot path:  'd:\tmp\dout\Fig\sepal length.png'
plot path:  'd:\tmp\dout\Fig\sepal width.png'
plot path:  'd:\tmp\dout\Fig\petal length.png'
plot path:  'd:\tmp\dout\Fig\petal width.png'
plot path:  'd:\tmp\dout\Fig\class.png'


out file: 'd:\tmp\dout\report.html'
```




