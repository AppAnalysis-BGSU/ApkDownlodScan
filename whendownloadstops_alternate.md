# What to do when download stops ( Alternative approach)

[1] Download Python Script from Github. 

```
curl https://raw.githubusercontent.com/AppAnalysis-BGSU/ApkDownlodScan/master/recovery/recover.py
```
[2] Run the script and test. First argument to the program is the most recent list of files ( as per date), and second argument is the foundList.

Eg. 
```
python recover.py list_july3.csv foundList.csv

```
[3] Check the no of lines of the result:

```
python recover.py list_july3.csv foundList.csv | wc - l

```
The no of lines should be roughly equal to the (X-Y)

Where, in this example,  X is the no of lines in list_july3.csv and 
Y is the no of files in the most recent downloads folder. 

X: 
```
wc -l list_july3.csv
```

Y:
```
ls downloads4 | wc -l
```

[4] If everything looks good in the above step, run the script and create a new list of files. 

```
python recover.py list_july3.csv foundList.csv > list_$today's_date.csv

```

[5] Now, use this new list and start the download process:

First argument is the new List and second argument is the folder where you want to download the VirusTotal results.

Example, 
```
python getVirusTotal.py list_$today's_date.csv report5
```

**Please note:**

There will be  N folders in the directory: report, report2, report3, report4...reportN 
and corresponding folders downloads, downloads2, downloads3, downloads4, downloadsN This will help us copy some portion for research / testing. 
But, we may want to merge everything together at the end. 

If you are keeping results in a new folders, 
Example, report5,and downloads5,  

Make sure you make necessary updates in the script as well, 

```python
if sha256 not in downLoadedApks: # If the file has not been downloaded, download it. # Get the API key from Androzoo. 
os.system('curl -G -d apikey=$key_androZoo -d sha256='+sha256+' https://androzoo.uni.lu/api/download -o downloads/'+sha256+'.apk') #Modify this line. 
```

[6] Check the counts in folders: report5, downloads5, and the increment in foundList.csv. 

[7] If everything is Ok in 5, run the email sending script to track the progress:

```
python sendEmail.py
```

# What to do When academic api access expires 
It will expire tentatively during the last week of July. In that case, 
Either:
[1] Get the new academic api and follow the above process. 
Or 
[2] Increase the delay in getVirusTotal.py to 15 s. Currently it is 1 s. 

```
time.sleep(1) #Change the delay to 15 s 
```



In case of any issues, Please email : civabhusal@gmail.com






