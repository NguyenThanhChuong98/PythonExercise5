import csv


def tab_delimiter():
    with open('exo2.csv', newline='') as f:
        data = csv.reader(f, delimiter='\t')
        for row in data:
            print(', '.join(row))
    f.close()

tab_delimiter()