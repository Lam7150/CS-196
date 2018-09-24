#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np


def histogram_times(filename):
    # initializing list to track plane crash times
    plane_crash_times = [0] * 24

    # opening and loading plane crash history
    with open(filename, "r") as csvfile:
        airplanes = csv.DictReader(csvfile)

        # iterating through planes in plane crash history
        for row in airplanes:
            
            # sanitizing input
            if row['Time'] != "":
                row['Time'] = row['Time'].lstrip("c: ")

                # cleaning and recording plane crash times
                if (row['Time'][:2] == "00"):
                    plane_crash_hour = 0
                else:
                    plane_crash_hour = int(row['Time'][:2].lstrip('0').rstrip(".:'")) % 24
                plane_crash_times[plane_crash_hour] += 1

    return plane_crash_times


def weigh_pokemons(filename, weight):
    # initializing pokemon list
    matched_pokemon = []

    # opening and loading pokedex
    with open(filename, "r") as file:
        pokedex = json.load(file)

        # iterating through pokedex and recording pokemon with matching weights into pokemon list
        for pokemon in pokedex["pokemon"]:
            if float(pokemon["weight"].rstrip(" kg")) == weight:
                matched_pokemon.append(pokemon["name"])

    return matched_pokemon


def single_type_candy_count(filename):
    # initializing candy sum
    candy_sum = 0

    # opening and loading pokedex
    with open(filename, "r") as file:
        pokedex = json.load(file)

        # iterating through pokemon and summing candy count for single-type pokemon
        for pokemon in pokedex["pokemon"]:
            if (len(pokemon["type"]) == 1):
                candy_sum += int(pokemon.get("candy_count", 0))

    return candy_sum


def reflections_and_projections(points):
    # reflecting point across y = 1
    points[1] = (2 - points[1])

    # rotating point 90 degrees about origin
    temp = np.array(points[0])
    points[0] = points[1]
    points[1] = temp

    # projecting point onto line y = 3x
    points = np.matmul(points, [[1,3], [3,9]])
    points = np.multiply(points, 0.1)

    return points


def normalize(image):
    # declaring and initializing image max and mins
    min = image.min()
    max = image.max()

    # normalizing image
    image = np.subtract(image, min)
    image = np.multiply(image, 255 / (max - min))

    return image


def sigmoid_normalize(image):
    pass