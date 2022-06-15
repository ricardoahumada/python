#!/usr/bin/env python3

import os
from sys import argv

script, from_file, to_file = argv

open(to_file, 'w').write(open(from_file).read())

target = open(to_file)
contents = target.read()
print(contents)
target.close()

os.remove("new.txt")
