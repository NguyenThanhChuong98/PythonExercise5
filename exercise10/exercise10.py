import csv


def read_file():
    data = [[10, 'a1', 1], [12, 'a2', 3], [14, 'a3', 5], [16, 'a4', 7], [18, 'a5', 9]]
    with open("exo10.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
    with open('exo10.csv', newline='') as f:
        data = csv.reader(f, delimiter=' ')
        for row in data:
            print(', '.join(row))
    f.close()


read_file()
