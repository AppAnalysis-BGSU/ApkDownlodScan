'''
Python Script to recover once the download process stops.

Running the script:


First test:
python recover.py arg1 arg2

Then create a new file:

python recover.py arg1 arg2 > download_list_date.csv

arg1 is the original fileList ( the list of files for which download process had started in the previous instance)

arg2 is the foundList.


'''

import sys

current = str(sys.argv[1])
foundFile = str(sys.argv[2])

currentList = []
foundList = []
newList = []

currentContent = open (current, 'r')

for line in currentContent:
    currentList.append(line.strip())
currentContent.close()

foundListContent = open (foundFile, 'r')
for line in foundListContent:
    foundList.append(line.strip())
foundListContent.close()

'''
Only take those files from currentList which are not in foundList.
'''
for sha256 in currentList:
    if sha256 not in foundList:
        print(sha256)




