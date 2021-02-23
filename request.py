import requests
import json
import sys

def GetInputData():
     artist = input("Enter artist/ band name....   ")
     print("You have entered " + artist)
     return artist


def GetUrlForWebsite(artist):
     brainstring = (f'http://musicbrainz.org/ws/2/release/?query=artist:{artist};fmt=json;limit=100')
     return brainstring


def GetResponseDataFromWebSite(brainstring):
     response = requests.get(brainstring)
     return response

def RemoveFinalNCharactersFromStringEnd(TextString,n):
    TextString = TextString[0:-n]
    return TextString


def GetYearFromDate(date):
    Year = date[0:4]
    return Year


def GetAlbumDataAsString(response): 
      albumstring = ''
      yearstring = ''
      a = 0
      for data in response.json()['releases']:
            a = a + 1
            try:
                 if data['release-group']['primary-type'] == "Album" and data['status'] == "Official":
                        albumstring = albumstring + data['title'] + "--"
                        yearstring = yearstring + GetYearFromDate(data['date']) + "--"
            except KeyError:       
                 print ("record number", a, "keyerror in returned data")

      return yearstring, albumstring


def GetListFromTextString(Textstring,delimiter):
    newlist = list(Textstring.split(delimiter))
    return newlist


def ZipListsAndSortOnColumn(List1,List2,n,sorttype):
    zipped_list = (sorted(list(zip(List1, List2)), key=lambda x: x[n], reverse = sorttype))
    return zipped_list


artist = GetInputData() 
brainstring = GetUrlForWebsite(artist) 
response = GetResponseDataFromWebSite(brainstring)
yearstring, albumstring = GetAlbumDataAsString(response)

yearstring = RemoveFinalNCharactersFromStringEnd(yearstring,2)
albumstring = RemoveFinalNCharactersFromStringEnd(albumstring,2)

yearlist = GetListFromTextString(yearstring,'--')
albumlist = GetListFromTextString(albumstring,'--')
zipped_list = ZipListsAndSortOnColumn(albumlist, yearlist,1,True)


ITERATION_LIMIT = 10
for data in (zipped_list[0:ITERATION_LIMIT]):
           print (data[0] + ' ' + data[1])



