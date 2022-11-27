import numpy
import matplotlib.pyplot as plt
import csv
from rich import print

if __name__ == "__main__":

    y = {}
    for x in range(0, 46, 1):
        y[x] = []

    with open("fireSolution.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        x = []

        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue

            x.append(float(row[0]))
            i = 0
            for v in row[1:]:
                y[i].append(float(v))
                i += 1
    print(x)

    mymodel = numpy.poly1d(numpy.polyfit(x, y[0], 2))
    myline = numpy.linspace(500, 1250, 100)

    plt.scatter(x, y[0])
    plt.plot(myline, mymodel(myline))

    plt.show()
