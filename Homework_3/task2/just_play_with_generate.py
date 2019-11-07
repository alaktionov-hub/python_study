#!/usr/bin/env python3

import sys
import numpy as np
filename = sys.argv[1]  # What File we need use. Argument 1
where_write_file = open(filename, "w")


data_fizz_buzz_to_write = str(np.random.randint(1, 99, size=(20, 3)))

print(data_fizz_buzz_to_write)
where_write_file.write(data_fizz_buzz_to_write)
