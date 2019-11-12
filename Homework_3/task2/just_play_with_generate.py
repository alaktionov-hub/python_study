#!/usr/bin/env python3

import sys
import numpy as np
filename = sys.argv[1]  # What File we need use. Argument 1
where_write_file = open(filename, "w")

np.savetxt(where_write_file, np.random.randint(1, 99, size=(20, 3)), fmt="%s")

# np.savetxt - use to save

