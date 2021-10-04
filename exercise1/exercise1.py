import csv


def read_each_row():
    with open('exo1.csv', newline='') as f:
        data = csv.reader(f, delimiter=' ', quotechar='|')
        for row in data:
            print(', '.join(row))
    f.close()

read_each_row()
