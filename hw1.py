#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np

def main():
    histogram_times("airplane_crashes.csv")

def histogram_times(filename):
    planeCrashTimes = [0] * 24

    with open(filename, "r") as csvfile:
        airplanes = csv.DictReader(csvfile)
        for row in airplanes:
            if row['Time'] != "":
                row['Time'] = row['Time'].lstrip("c: ")

                if (row['Time'][:2] == "00"):
                    planeCrashHour = 0
                else:
                    planeCrashHour = int(row['Time'][:2].lstrip('0').rstrip(".:'")) % 24
                planeCrashTimes[planeCrashHour] += 1

    return planeCrashTimes

def weigh_pokemons(filename, weight):
    pass

def single_type_candy_count(filename):
    pass

def reflections_and_projections(points):
    pass

def normalize(image):
    pass

def sigmoid_normalize(image):
    pass

if __name__ == "__main__":
    main()