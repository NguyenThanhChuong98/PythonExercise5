import csv


def read_file():
    with open('exo4.csv', newline='') as f:
        data = csv.DictReader(f)
        for row in data:
            print(row)
    f.close()


read_file()
