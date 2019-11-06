#!/usr/bin/env python3
# Find Floor
flats_per_floor = 8
floors = 24

flat_needed = int(input("what flat do you need?: "))
current_floor = 1


while current_floor <= floors:
    if flat_needed <= current_floor * flats_per_floor:
        print("Flor  {}, apartment found!".format(current_floor))
        # Read more about format
        break
    current_floor += 1
