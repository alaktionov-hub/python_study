#!/usr/bin/env python3


num_flat = int(input("Give number of apartment what you search: "))
num_floors = 24  # flors in 1 house
num_flats_per_floor = 8  # Flat per floor


current_floor = 1  # We need count flor
current_porch = 1  # We need cpint porch


# So add check if num flat more that num flats
# So lets check if flat what we search > more that all flats in 1 hous . So if yes, we go to second porch +1
while num_flat > num_floors*num_flats_per_floor*current_porch:
    current_porch += 1
num_flat = num_flat - num_floors*num_flats_per_floor*(current_porch-1)
while current_floor <= num_floors:  # Then check if currnet flor less than flat what we search
    # If flat what we search less than current flor we * to flat per floor
    if num_flat <= current_floor * num_flats_per_floor:
        print("So this flat at porch - ", current_porch, "on this Floor - ",
              current_floor, " You can kill em all !!")
        break
    current_floor += 1
