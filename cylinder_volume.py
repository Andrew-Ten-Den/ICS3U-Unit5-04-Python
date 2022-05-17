#!/usr/bin/env python3

# Created by : Andrew-Ten-Den
# Created on : May 2022
# This program calculates the volume of a cylinder

import math


def calculate_volume(radius, height):
    # This function calculates the volume of a cylinder
    answer = (math.pi) * radius**2 * height

    return answer


def main():
    # This function calculates the volume of a cylinder

    # input
    radius = input("Enter radius (in cm): ")
    height = input("Enter height (in cm): ")
    print("")

    # process
    try:
        radius_value_as_int = int(radius)
        height_value_as_int = int(height)
        solution = calculate_volume(radius_value_as_int, height_value_as_int)
        print("The volume is {:.2f} cm³".format(solution))
    except Exception:
        print("These are not integers")


if __name__ == "__main__":
    main()
