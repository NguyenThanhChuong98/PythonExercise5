import csv

csv.register_dialect('csv_dialect',
                     delimiter='|',
                     skipinitialspace=True,
                     quoting=csv.QUOTE_ALL)


def read_file():
    with open('exo6.csv', 'r') as f:
        reader = csv.reader(f, dialect='csv_dialect')
        for row in reader:
            print(row)
    f.close()


read_file()
