from meteomoris import *
import datetime
import sys
import json

result = get_weekforecast()

# get unix timestamp of now
now = datetime.datetime.now()

dated_file_name = './data/history/' + str(int(now.timestamp())) + '.json'
latest_file_name = './data/latest.json'


with open(dated_file_name, 'w+', encoding='utf8') as f:
    json.dump(result, f, ensure_ascii=False)

with open(latest_file_name, 'w+', encoding='utf8') as f:
    json.dump(result, f, ensure_ascii=False)
