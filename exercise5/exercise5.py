import csv


def read_file():
    with open('exo5.csv', 'r') as f:
        data = csv.reader(f, skipinitialspace=False)
        for row in data:
            print(', '.join(row))
    with open('exo5.csv', 'r') as f:
        data = csv.reader(f, skipinitialspace=True)
        for row in data:
            print(','.join(row))
    f.close()


read_file()
