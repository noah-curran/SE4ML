#!/usr/bin/python3
# baditeration.py


def printtable(table):

    for i in range(0, len(table) - 1):
        for j in range(0, len(table[i]) - 1):
            print(table[j][i], '\t', end=' ')
        print('')

if __name__ == "__main__":

    table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    printtable(table)
