from meteomoris import *
import sys

result = get_weekforecast()

output = './data/latest.json'
sys.stdout = open(output, "w")
print(result)
