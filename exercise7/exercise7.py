import csv


def read_file():
    with open('exo7.csv', newline='') as f:
        data = csv.DictReader(f)
        for row in data:
            print(row['department_id'], row['department_name'])
    f.close()


read_file()
