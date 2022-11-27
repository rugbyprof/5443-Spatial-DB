import csv
import json


def doit(ms, deg):
    mss = [
        500,
        550,
        600,
        650,
        700,
        750,
        800,
        850,
        900,
        950,
        1000,
        1050,
        1100,
        1150,
        1200,
        1250,
    ]
    formulas = [
        0.001370 + -0.000000364 + deg + 0.0000128 + deg**2,
        0.001030 + 0.00000054 + deg + 0.000015 + deg**2,
        0.001630 + -0.000000729 + deg + 0.0000172 + deg**2,
        0.001220 + -0.0000000455 + deg + 0.0000192 + deg**2,
        0.001180 + 0.000000159 + deg + 0.000021 + deg**2,
        0.000979 + 0.00000038 + deg + 0.0000226 + deg**2,
        0.00101 + 0.000000445 + deg + 0.0000239 + deg**2,
        0.00133 + -0.000000223 + deg + 0.0000248 + deg**2,
        0.00131 + -0.0000000613 + deg + 0.0000254 + deg**2,
        0.00156 + -0.000000656 + deg + 0.0000256 + deg**2,
    ]
    return None


if __name__ == "__main__":
    with open("distance_table.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        x = []

        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue
