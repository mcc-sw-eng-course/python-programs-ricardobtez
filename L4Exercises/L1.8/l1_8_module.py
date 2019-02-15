"""
Matricula: AA00354798
Nombre: Samuel Solorzano Ramirez
Maestro: Dr. Gerardo Padilla
Materia: Analysis, Design, and Construction of Software Systems

L1 - 8
Write a module containing different function that computes the:
- Sample Mean
- Sample standard deviation
- Median
- A function that returns the n-quartil
- A function that returns the n-percentil
"""
def get_sample_mean(sample):
    mean = 0
    if isinstance(sample, list):
        if len(sample) > 0:
            for x in sample:
                number = float(x)
                mean = mean + number
            mean = mean / len(sample)
    return mean

import math
def get_sample_standard_dev(sample):
    sdev = 0
    if isinstance(sample, list):
        if len(sample) > 0:
            mean = get_sample_mean(sample)
            variance = 0
            for x in sample:
                number = mean - float(x)
                variance = variance + (number*number)
            variance = variance / len(sample)
            sdev = math.sqrt(variance)
    return sdev

def get_sample_median(sample):
    median = 0
    if isinstance(sample, list):
        if len(sample) > 0:
            sample_sorted = sorted(sample)
            length = len(sample_sorted)
            if length % 2 == 0 :
                middle = int(length/2)
                median = ( float(sample_sorted[middle-1]) + float(sample_sorted[middle])) / 2.0
            else:
                middle = int((length)/2)
                median = sample_sorted[middle]
    return median

class Quartil:
    LOW, MID, HIGH = range(0, 3)

def get_n_quartil(quart, sample):
    lowQ = 0
    highQ = 0
    midQ = 0
    if isinstance(sample, list):
        if len(sample) > 0:
            sample_sorted = sorted(sample)
            length = len(sample_sorted)
            middle = int(length/2)
            if (length % 2 == 0):
                lowQ = get_sample_median(sample_sorted[:middle])
                highQ = get_sample_median(sample_sorted[middle:])
            else:
                lowQ = get_sample_median(sample_sorted[:middle])
                highQ = get_sample_median(sample_sorted[middle+1:])
            midQ = get_sample_median(sample_sorted)
    if quart == Quartil.LOW:
        return lowQ
    elif quart == Quartil.MID:
        return midQ
    elif quart == Quartil.HIGH:
        return highQ
    else:
        return None

def get_n_percentil(per, sample):
    perc = 0
    if isinstance(sample, list):
        if len(sample) > 0:
            sample_sorted = sorted(sample)
            length = len(sample_sorted)
            index = per * length # get the % index in the array
            index = int(index + 1) # round it up
            perc = sample_sorted[index-1]
    return perc
