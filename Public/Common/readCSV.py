import csv
import os.path
from Config.global_config import data_path


def readcsv(filename):
    datafile = os.path.join(data_path, filename)
    stream = open(datafile, "r")
    data = csv.reader(stream)
    list = []
    i = 0
    for row in data:
        if i != 0:
            list.append(row)
        i += 1
    return list


# if __name__ == '__main__':
#     data = readcsv()
#     for row in data:
#         print(row)
