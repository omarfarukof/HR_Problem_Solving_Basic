import math
import os
import random
import re
import sys



#
# Complete the 'mostActive' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY customers as parameter.
#

def mostActive(customers):
    customers_id = list(set(customers))
    out = []
    total_customers = len(customers)
    for c in customers_id:
        if ((customers.count(c))/total_customers*100) >= 5:
            out.append(c)
    out.sort()
    return out

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # fptr = open('/dev/stdout', 'w')

    customers_count = int(input().strip())

    customers = []

    for _ in range(customers_count):
        customers_item = input()
        customers.append(customers_item)

    result = mostActive(customers)

    # print("->\n")

    # fptr.write('\n'.join(result))
    # fptr.write('\n')

    # fptr.close()



    print('\n'.join(result))
