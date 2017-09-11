# -*- coding: utf-8 -*-

import sys
import vpython as vs
import numpy as np


# CSVファイルを読み込み、リスト化

def open_with_numpy_loadtxt_2(filename):
    with open(filename, 'r') as file:
        line = file.readline()
        header = line.strip().split(',')
        data = np.genfromtxt( filename, delimiter=",",skip_header=1, filling_values=(0, 0, 0) )
    return map(int,header), data

header, data = open_with_numpy_loadtxt_2('copy.csv')
#header, data = open_with_numpy_loadtxt_2(input("File Name = "))

x, z, y = header
print("x,z,y = ",x,z,y)

List = data.tolist()

#PList = [[[[0 for n in range(2)] for i in range(x)] for j in range(z)] for k in range(y)]


m = 0
for k in range(y):
    for j in range(z):
        for i in range(x):
            #PList[k][j][i] = [List[m][0], List[m][1]]

            if List[m][0] != 0:

                vs.box(pos=vs.vector(i - 0.5 - x / 2, k - 0.5 - y / 2, j - 0.5 - z / 2),length=1, width=1, height=1,color=vs.color.green)

            print([List[m][0], List[m][1]],end = "")
            m += 1
    #        print(PList[k][j][i],end = "")
        print()
    print()
