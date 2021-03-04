import requests
import json
import sys
      



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


class myResponseFromWebSite:
    def __init__(self,url):
         self.response = requests.get(url)


    def description(self):
         print (f'{self.response}')


class myGetRequiredQueryDataFromJson:

     def __init__(self,jsondata):
         self.status = jsondata.get('status')
         self.title = jsondata.get('title')
         self.date = jsondata.get('date')
         self.type = jsondata['release-group'].get('primary-type')

         if self.title is None:
             self.title = 'Nonetype'
         if self.date is None or not self.date:
             self.date = 'Nonetype'

         self.date = self.date[0:4]


     def description(self):
         print (f'{self.status} {self.title} {self.date} {type(self.date)} {self.type}')


class myRelease:

     def __init__(self,artist,release_title,release_date):
         self.artist = artist
         self.title = release_title
         self.yearofrelease = release_date

     def description(self):
         print (f'{self.artist} released {self.title} in {self.yearofrelease}')


class myRequiredData:
     def __init__(self,releasetype,releasestatus,releaseyear):
         self.filter = False
         if releasetype == "Album" and releasestatus == "Official" and not releaseyear == 'Nonetype':
             self.filter = True
     def description(self):
         print (f'{self.filter}')


class myReleaseList:
     def __init__(self,artist,response):
          self.releaselist = []
          for data in response.json()['releases']:
               releasedata = myGetRequiredQueryDataFromJson(data)
               #releasedata = myGetRequiredQueryDataFromJson.myadjustforexceptions(releasedata)
               try:
                    releasefilter = myRequiredData(releasedata.type,releasedata.status,releasedata.date)
                    if releasefilter.filter == True:
                         self.releaselist.append(myRelease(artist,releasedata.title,releasedata.date))                 
               except Exception as e:       
                    print (f'exception error {e} ')
     
     def description(self):
         #print (f'{self.releaselist}')
         for x in range(len(self.releaselist)):
             print (self.releaselist[x].yearofrelease)
     
     
     def sortarray(self):
         sorted((self.releaselist), key=lambda x: x.yearofrelease, reverse = False)
         

  


bandname = myEntry()
bandname.description()

bandurl = myCreateUrl(bandname.artist)
#bandurl.description()

webresponse = myResponseFromWebSite(bandurl.url)
#webresponse.description()

#artist = GetInputData() 
#brainstring = GetUrlForWebsite(artist) 
#response = GetResponseDataFromWebSite(brainstring)
album_list = myReleaseList(bandname.artist,webresponse.response)


def SortAlbumArray(albumlist,sorttype):
    return sorted((albumlist), key=lambda x: x.yearofrelease, reverse = sorttype)




def RemoveRereleases(albumlist):
    for release in albumlist:
         testalbum = release.title
         count = 0
         for release2 in albumlist:
              testalbum2 = release2.title
              if testalbum == testalbum2:
                   count = count + 1
                   if count == 2:
                        print ("removed ", release2.title, release2.yearofrelease)
                        albumlist.remove(release2)
                        count = 1
    return albumlist


def Rereleases(albumlist):
    for release in albumlist:
         print (release)

         

sorted_album_list = SortAlbumArray(album_list.releaselist,False)
removed_album_list = RemoveRereleases(sorted_album_list)
sorted_album_list = SortAlbumArray(removed_album_list,True)


print('\nTen most recent album releases are ....')
for obj in sorted_album_list:
    obj.description()







def GetListFromTextString(Textstring,delimiter):
    newlist = list(Textstring.split(delimiter))
    return newlist






