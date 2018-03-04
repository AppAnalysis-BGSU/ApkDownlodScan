''' Original Author: Yuping Li, University of South Florida

Modified/ Adpated By: Shiva Bhusal, BGSU
'''
 
import os
import sys
import time
import requests

md5lists = []
targetdir = sys.argv[2]

with open(sys.argv[1]) as f:
    for line in f:
        #md5 = line.strip().split()[1]
        md5lists.append(line.strip().split(".")[0])

apikey = 'apikey string' 

headers = {
          "Accept-Encoding": "gzip, deflate",
          "User-Agent" : "gzip,  My Python requests library example client or username"
          }
uri = 'https://www.virustotal.com/vtapi/v2/file/report'

count = 0
for md5 in md5lists:	
    path = os.path.join(targetdir, md5+".json")
    if os.path.exists(path):
        continue
    params = {'apikey': apikey, 'resource': md5}
    response = requests.get(uri, params=params, headers=headers)
    if response.status_code != 200 or not response.text:
        if count >= 3:
            break
        count += 1
        print response.status_code, len(response.text)
        continue
    with open(path, "w") as f:
        f.write(response.content)
    print "Processed md5:", md5
    time.sleep(15)
