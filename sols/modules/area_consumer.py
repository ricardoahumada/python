#!/usr/bin/env python3

from area_calculator import calc_area

res1 = calc_area('square', {'side': 2})
print('square area: ', res1)

res2 = calc_area('rectangle', {'width': 4, 'length': 6})
print('rectangle area: ', res2)

res3 = calc_area('triangle', {'base': 4, 'height': 10})
print('triangle area: ', res3)
