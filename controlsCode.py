#Importing Numpy, Matplotlib, Math, and Pandas
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd 

figure_counter = 0

#Extracting and formatting the data 
def extract_data(extension):
    path = 'Controls Lab Data/WED1 ' + extension + '.txt'
    n, m = len(open(path).readlines()), 4
    raw_data = np.empty((n - 3, m), dtype=np.dtype('U100'))
    n, m = 0, 0

    with open(path, 'r') as file:
        for line in file:
            m = 0
            if n > 1 and n < len(open(path).readlines()):
                for word in line.split():
                    if word != '[': 
                        raw_data[n - 3, m] = word
                        m += 1
            n += 1

    raw_data = np.char.strip(raw_data, ';')
    raw_data = np.char.strip(raw_data, ']')
    return raw_data
                
def processing_Datasets():
    set_names = np.array(['frequency response critically damped', 
                           'frequency response over damped',
                           'frequency response under damped',
                           'P response Kp=2X',
                           'P response Kp=X',
                           'PD response critically damped',
                           'PD response over damped',
                           'PD response under damped',
                           'PID response Ki=2X',
                           'PID response Ki=X'])