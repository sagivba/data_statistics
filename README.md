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

```
 [prompt]$ python data_statistics.py -i "TestData/dessert.csv" -D "/tmp/dessert" -v
data was loaded from /home/sagivba/TestData/dessert.csv
input_file: '/home/sagivba/TestData/dessert.csv'
fig dir   : '/home/sagivba/TestData/Fig/'
out_file  : '/home/sagivba/TestData/report.html'
plot path:  '/tmp/dessert/Fig/id.png'
plot path:  '/tmp/dessert/Fig/day.of.week.png'
plot path:  '/tmp/dessert/Fig/num.of.guests.png'
plot path:  '/tmp/dessert/Fig/hour.png'
plot path:  '/tmp/dessert/Fig/table.png'
plot path:  '/tmp/dessert/Fig/dessert.png'


out file: /tmp/dessert/report.html
```



