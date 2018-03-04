## ApkDownlodScan

### Download the latest CSV from Androzoo
```
curl https://androzoo.uni.lu/static/lists/latest.csv.gz --output latest.csv.gz
```

### Get the first column [Not necessary]

```
awk -F"," '{if ($1) print $1}' latest.csv >sha256List.csv
```

### Get the third (1/3)rd portion of the APKS
tail -1920588 sha256List.csv >finalList.csv


