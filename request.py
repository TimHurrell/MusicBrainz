import requests
import json
import sys

#def GetInputData():
 #    artist = input("Enter artist/ band name....   ")
  #   print("You have entered " + artist)
   #  return artist


#def GetUrlForWebsite(artist):
 #    brainstring = (f'http://musicbrainz.org/ws/2/release/?query=artist:{artist};fmt=json;limit=100')
  #   return brainstring


def GetResponseDataFromWebSite(brainstring):

     response = requests.get(brainstring)
     return response

def GetAlbumDataAsString(response): 
      albumlist2 = []
      for data in response.json()['releases']:
            release_status = data.get('status')
            release_title = data.get('title')
            release_date = data.get('date')
            release_type = data['release-group'].get('primary-type')
            if release_title is None:
                 release_title = 'Nonetype'
            if release_date is None or not release_date:
                 release_date = 'Nonetype'

            try:
                if release_type == "Album" and release_status == "Official":
                    album = myAlbum()
                    album.artist = artist
                    album.albumname = release_title
                    album.yearofrelease = release_date[0:4]
                    if not release_date == 'Nonetype':
                         albumlist2.append(album)                  
            except Exception as e:       
                 print (f'exception error {e} ')
      

      sort_list = SortAlbumArray(albumlist2, False)
      removed_releases = RemoveRereleases(sort_list)
      resort_list = SortAlbumArray(removed_releases, True)

      ITERATION_LIMIT = 10
      resort_list2 = resort_list[0:ITERATION_LIMIT]
      return resort_list2

def SortAlbumArray(albumlist,sorttype):
    return sorted((albumlist), key=lambda x: x.yearofrelease, reverse = sorttype)


def RemoveRereleases(albumlist):
    for release in albumlist:
         testalbum = release.albumname
         count = 0
         for release2 in albumlist:
              testalbum2 = release2.albumname
              if testalbum == testalbum2:
                   count = count + 1
                   if count == 2:
                        print ("removed ", release2.albumname, release2.yearofrelease)
                        albumlist.remove(release2)
                        count = 1
    return albumlist


def GetListFromTextString(Textstring,delimiter):
    newlist = list(Textstring.split(delimiter))
    return newlist




class myEntry:
    def __init__(self):
         self.artist = input('Enter name of artist/ band:  ')

    def description(self):
         print (f'/n/n You have selected {self.artist}')



class myCreateUrl:
    def __init__(self,artist):
         self.url = (f'http://musicbrainz.org/ws/2/release/?query=artist:{artist};fmt=json;limit=100')


    def description(self):
         print (f'URL is {self.url}')


class myResponse:
    def __init__(self,url):
         self.response = requests.get(url)


    def description(self):
         print (f'{self.response}')


class myAlbum:

    artist = "artist"
    albumname = "album"
    yearofrelease = 1800

    def description(self):
         print (f'{self.artist} released {self.albumname} in {self.yearofrelease}')



bandname = myEntry()
bandname.description()

bandurl = myCreateUrl(bandname.artist)
bandurl.description()

response = myResponse(bandurl.url)
response.description()

#artist = GetInputData() 
#brainstring = GetUrlForWebsite(artist) 
#response = GetResponseDataFromWebSite(brainstring)
#album_list = GetAlbumDataAsString(response)


#print('\n\n\nTen most recent album releases are ....')
#for obj in album_list:
#     obj.description()




