''' 
Original Author: Yuping Li, University of South Florida
Modified/ adapted By: Shiva Bhusal, BGSU
'''
 
import os
import sys
import time
import requests

sha256lists = [] #md5 renamed to sha256. 
downLoadedApks=[]
targetdir = sys.argv[2]

with open("newapks_already_downloaded.txt") as f: #Open the file and get its content in a list. 
    for line in f:
        temp=line.strip().split('.')[0]
        downLoadedApks.append(temp)


with open(sys.argv[1]) as f:
    for line in f:
        #sha256 = line.strip().split()[1]
        temp=line.strip()
        sha256lists.append(temp)


apikey = '$key_virusTotal' # Get the API key from the virus total website.

headers = {
          "Accept-Encoding": "gzip, deflate",
          "User-Agent" : "gzip,  My Python requests library example client or username"
          }
uri = 'https://www.virustotal.com/vtapi/v2/file/report'
foundFilePath = "foundList.csv"


count = 0
for sha256 in sha256lists:	
    path = os.path.join(targetdir, sha256+".json")
    if os.path.exists(path):
        continue
    params = {'apikey': apikey, 'resource': sha256}
    response = requests.get(uri, params=params, headers=headers)
    if response.status_code != 200 or not response.text:
        if count >= 3:
            break
        count += 1
        print response.status_code, len(response.text)
        continue
    with open(path, "w") as f:
        f.write(response.content)

    with open(foundFilePath,"a") as f:
        f.write('\n')
        f.write(sha256)

    if sha256 not in downLoadedApks: # If the file has not been downloaded, download it. # Get the API key from Androzoo. 
        os.system('curl -G -d apikey=$key_androZoo -d sha256='+sha256+' https://androzoo.uni.lu/api/download -o downloads/'+sha256+'.apk')

    print "Processed sha256:", sha256
    time.sleep(15)
