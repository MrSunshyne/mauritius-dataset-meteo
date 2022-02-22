from meteomoris import *
import datetime
import sys

result = get_weekforecast()

# get unix timestamp of now
now = datetime.datetime.now()
dated_file_name = './data/history/' + str(int(now.timestamp())) + '.json'


latest_file_name = './data/latest.json'
sys.stdout = open(latest_file_name, "w")
print(result)

sys.stdout = open(dated_file_name, "w")
print(result)
