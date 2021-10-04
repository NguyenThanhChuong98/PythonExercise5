import csv


def read_file():
    with open('exo3.csv', newline='') as f:
        reader = csv.reader(f)
        data_list = list(reader)
        print(data_list)
    f.close()

read_file()
