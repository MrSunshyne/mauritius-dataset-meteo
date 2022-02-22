from meteomoris import *
import sys

result = get_weekforecast()
# print(result)

output = 'latest.json'
sys.stdout = open(output, "w")
print(result)
