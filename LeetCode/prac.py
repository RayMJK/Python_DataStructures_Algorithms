#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'groupDivision' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY levels
#  2. INTEGER maxSpread
#

def groupDivision(levels, maxSpread):
    # Write your code here
    answer = 1
    stack = [levels[0]]
    levels = sorted(levels)
    if len(levels) == 0:
        return 0
    elif maxSpread == 0 and len(list(set(levels))) != 1:
        return len(list(set(levels)))
    else:
        for i in range(1, len(levels)):
            if levels[i] - stack[0] <= maxSpread:
                stack.append(levels[i])
            else:
                new = levels[i]
                stack = [new]
                answer += 1
    return answer


if __name__ == '__main__':