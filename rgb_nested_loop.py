#!/usr/bin/env python3
# Created by: Lia Duggan
# Created on: Nov.11th, 2022
# This program displays all the Valid RGB colors


def main():

    # Making the Variables for the Colors
    for red in range(0, 256):

        for blue in range(0, 256):

            for green in range(0, 256):

                print("{} {} {}".format(red, green, blue))
                # printing all the RGB colors in the color it correlates to
                print(
                    (
                        "{} {} {}"
                        "\033[{};{};{}m".format(red, green, blue, red, green, blue)
                    )
                )


if __name__ == "__main__":
    main()
