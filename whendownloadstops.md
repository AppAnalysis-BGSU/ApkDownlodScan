# What to do when download stops: 

[0] Login as root and Go to /media/seagate/Androzoo. 

[1] Look at the email from appdownloadupdates@gmail.com and get the count of the apps downloaded when the process started running. 

Example: 150859 APKs downloaded.

[2] Get the count of the apps when the process stopped. 

wc -l foundList.csv 

Example, 160820

[3] Find the difference: 
160820 - 150859 = 9961

[4] Get the total count in the APKlist (to-be-downloaded). List has been kept with date information. 
wc -l list_5312018.csv 

Say, (N)

I would calculate (N-9961), say we get M. 
and do: 

```
tail -M list_5312018.csv > list_6022018.csv
```
Note that list_6022018.csv has 9961 fewer apps than list_5312018.csv.

[5] Now we have the updated list. And we may want to start the process. 
```
python getVirusTotal.py list_6022018.csv report4 
```

First argument is the list of files (to-be-downloaded), second argument is the folder where you want to keep your downloaded .json files. 

There are four folders : report, report2, report3, report4 
and corresponding folders downloads, downloads2, downloads3, downloads4. This will help us copy some portion for research / testing. 
But, we may want to merge everything together at the end. 

If you are keeping results in a new folders, say report5,and downloads5,  

Make sure you make necessary updates in the script as well, 

```python
if sha256 not in downLoadedApks: # If the file has not been downloaded, download it. # Get the API key from Androzoo. 
        os.system('curl -G -d apikey=$key_androZoo -d sha256='+sha256+' https://androzoo.uni.lu/api/download -o downloads/'+sha256+'.apk') #Modify this line. 
```

[6] Once you run the script, next step is to run the email script to track the progress. 

```
python sendEmail.py
```

Note ( Optional):  During this transition, we may miss 0-30 files from the list. Also, there may be 0-30 redundant APK names in the foundList.csv. But, this should be fine. This can be prevented by strictly matching the sha256, which is hectic thing to do because of  missing / redundant files during our transitions in the past.  

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






