#!/usr/bin/env python3


# First Write without porch


flats_per_floor = 8
floors = 24

# flat_needed = int(input("what flat do you need?: "))
# current_floor = 1


def find_flat_on_floor(flats_per_floor, floors, flat_needed):

    i = 1  # Start From 1 flor
    while i <= floors:
        line = ""
        while flat_needed <= i * flats_per_floor:
            # return(str("Flor  {}, apartment found!".format(current_floor)))
            line += str(i)
            print(i)
        # print("Flor  {}, apartment found!".format(current_floor))
    #	Read more about format
            break
        i += 1
        return line


find_flat_on_floor(8, 24, 13)
