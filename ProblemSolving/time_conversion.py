import math
import os
import random
import re
import sys
def timeConversion(s):
        
        check_day_night= s[-2:]
        time_with_out_meridian = s[:-2]
        hour = int(s[:2])
        if check_day_night == "AM":
            hour = (hour+1) %12 -1
            return f"{hour:02d}" + time_with_out_meridian[2:]
        elif check_day_night == "PM":
            hour = hour % 12 + 12
            return str(hour)+time_with_out_meridian[2:]
            
    # else:
        # print("Invalid value")




s = input()

result = timeConversion(s)

print(result)