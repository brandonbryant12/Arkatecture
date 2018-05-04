import requests
import zipfile
import io
from datetime import date

# Set variable for source parent URL and the download target folder
sourceURL = 'https://www5.fdic.gov/sdi/Resource/AllReps/All_Reports_'
downloadTargetFolder = 'C:\\Users\\KAnderson\\Desktop\\Bank_Files\\Testing'

# Set variables to be use for string manipulation and declare array to hold the final source URL's
quarters = ['0331', '0630', '0930', '1231']
startingYear = 2009
urlList = []

# Loop from starting year to current year and create a source URL for each quarter. Push URL's into final URL array.
def createURLArray(year):
    while year < date.today().year:
        for q in quarters:
            urlList.append(sourceURL + str(year) + q + '.zip')
        year += 1


# Declare function for downloading and unpacking the .zip files from source URL's to a specified target folder.
def GetFileFromURL(url):
    try:
        print("Downloading: " + url)
        sourceZip = requests.get(url)
        zipContent = zipfile.ZipFile(io.BytesIO(sourceZip.content))
        print("Unpacking files for: " + url)
        zipContent.extractall(downloadTargetFolder)
    except:
        print("Zip file not found at the following URL: ".format(url))

def GetBulkFiles():
    startYear = int(input("Enter a starting year for the data pull: "))
    createURLArray(startYear)
    for url in urlList:
        GetFileFromURL(url)

GetBulkFiles()