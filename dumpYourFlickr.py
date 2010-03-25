#!/usr/bin/python
import urllib, os, flickrapi
api_key = '9ef09d14ab74f2c204b5c4ceea060b4a'
secret = 'f1f0391de2f712a7'
flickr = flickrapi.FlickrAPI(api_key, secret)
publicPhotos = flickr.people_getPublicPhotos(api_key=api_key, user_id = '49649657@N00')
photos = []
for photo in publicPhotos.getiterator('photo'):
	photos.append(photo.attrib['id'])

for photo in photos:
	photoInfo = flickr.photos_getInfo(photo_id=photo)
	photoTag = photoInfo.find('photo')
	photoTitle = photoTag.find('title').text
	photoDownload = "http://farm%s.static.flickr.com/%s/%s_%s_b.jpg" % (photoTag.attrib['farm'], photoTag.attrib['server'], photoTag.attrib['id'], photoTag.attrib['secret'])
	print "Downloading: " + photoTitle
	urllib.urlretrieve(photoDownload, os.path.join(os.getcwd(), photoTitle+'.jpg'))