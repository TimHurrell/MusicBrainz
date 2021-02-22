import requests
import json
brainstring1 = 'http://musicbrainz.org/ws/2/release/?query=artist:'

artist = input("Enter artist/ band name....   ")
print("You have entered " + artist)
#artist = 'Love'
brainstring2 = ';fmt=json;limit=100'
brainstring = brainstring1 + artist + brainstring2
response = requests.get(brainstring)
albumstring = ''
yearstring = ''
for data in response.json()['releases']:
      try:
           if data['release-group']['primary-type'] == "Album" and data['status'] == "Official":
                 albumstring = albumstring + data['title'] + "--"
                 yearstring = yearstring + data['date'][0:4] + "--"
#                 break
      except Exception as e:
            a = 1

#      if data['release-group']['primary-type'] == "Album" and data['status'] == "Official":
#            albumstring = albumstring + data['title'] + "--"
#            yearstring = yearstring + data['date'][0:4] + "--"     

yearstring = yearstring[0:-2]
albumstring = albumstring[0:-2]
yearlist = list(yearstring.split('--'))
albumlist = list(albumstring.split('--'))
zipped_list = (sorted(list(zip(albumlist, yearlist)), key=lambda x: x[1], reverse = True))
#for data, count in enumerate(zipped_list):
#      if count <= 10:
#           print (data[0] + ' ' + data[1])
#print (albumstring)
for data in (zipped_list[0:10]):
           print (data[0] + ' ' + data[1])



