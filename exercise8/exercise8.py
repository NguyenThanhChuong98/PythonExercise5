import csv


def read_file():
    fields = []
    rows = []
    with open('exo8.csv', newline='') as f:
        data = csv.reader(f, delimiter=' ', quotechar=',')
        fields = next(data)
        for row in data:
            print(', '.join(row))
    print("\nTotal no. of rows: ", data.line_num)
    print('Field names are:')
    print(', '.join(field for field in fields))
    f.close()

read_file()
