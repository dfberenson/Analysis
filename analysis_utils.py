# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 14:15:30 2017

@author: dfberenson@gmail.com
"""

def Cell_dictreader(filename):
    import csv, json
    with open(filename) as f:
        cell_dict = {}
        reader = csv.DictReader(f)
        for row in reader:
            if row['cellnum'] != 'cellnum':
                cellnum = int(row['cellnum'])
                celldata = json.loads(row['celldata'])
                cell_dict[cellnum] = celldata
                     
    return cell_dict


def TracePlot (timepoints , values):
    import matplotlib.pyplot as plt
    plt.plot(timepoints , values)
    return