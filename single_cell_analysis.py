# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 14:09:07 2017

@author: dfberenson@gmail.com
"""

import numpy as np
import matplotlib.pyplot as plt


csv_filename = r'E:\DFB imaging experiments\DFB_170203_HMEC_1G_Fucci_4\DFB_170203_HMEC_1G_Fucci_4 cell_dict.csv'
analysis_dict = Cell_dictreader(csv_filename)

analysis_array_dict = {}
for cell in analysis_dict:
    analysis_array_dict[cell] = np.asarray(analysis_dict[cell])
    
aad = analysis_array_dict
#Each cell in aad is keyed to a numpy array with dimensions T x 9:
    #Each row is one timepoint
    #The columns are: Frame , X , Y , RedIntens , RedArea , RedMean , GreenIntens , GreenArea , GreenMean


good_cells = []
birth_sizes = []
G1_lengths = []

plt.ion()
for cell in aad:
    plt.plot(aad[cell][:,0] , aad[cell][:,6] , label = cell)
    plt.legend()
    plt.show(block = False)
    if input("Good cell? 0/1: "):
        good_cells.append(cell)


plt.ion()
for cell in good_cells:
    plt.plot(aad[cell][:,0] , aad[cell][:,6] , label = cell)
    plt.legend()
    plt.show(block = False)
    end_G1 = input("What frame does Fucci-D begin to rise? ")
    if end_G1 != 0:
        birth_sizes.append(aad[cell][4,3])
            #Uses the size at timepoint 4, after effects of mitosis have ended
        G1_lengths.append(end_G1 - aad[cell][0,0])


for cell in aad:
    plt.plot(aad[cell][:,0] , aad[cell][:,3] , label = cell)
    plt.legend()
    
plt.scatter(birth_sizes, G1_lengths)