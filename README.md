# data_statistics
A lean tool for obtaining statistics on flat data files

## Usage Examples:
### get help
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


### html output
 [prompt]$ python data_statistics.py -i "h:\DataMining\TestData\dessert.csv" -D "h:\tmp\dessert" -v
data was loaded from h:\DataMining\TestData\dessert.csv
input_file: 'h:\DataMining\TestData\dessert.csv'
fig dir   : 'h:\tmp\dessert\Fig\'
out_file  : 'h:\tmp\dessert\report.html'
plot path:  'h:\tmp\dessert\Fig\id.png'
plot path:  'h:\tmp\dessert\Fig\day.of.week.png'
plot path:  'h:\tmp\dessert\Fig\num.of.guests.png'
plot path:  'h:\tmp\dessert\Fig\hour.png'
plot path:  'h:\tmp\dessert\Fig\table.png'
plot path:  'h:\tmp\dessert\Fig\dessert.png'


out file: h:\tmp\dessert\report.html


