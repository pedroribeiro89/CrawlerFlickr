import os
#import codecs

class TagCrawler:

	flickr = None
	userList = []
	resultDir = None

	def __init__(self, flickr, userList, resultDir):
		self.flickr = flickr
		self.userList = userList
		self.resultDir = resultDir
		

	def execute(self):
		userIndex = 0
		photoIDList = []
		
		for userID in self.userList:
			os.makedirs(self.resultDir + userID)
		 	photoIDList = self.listUserPhotos(userID)
		 	for photoID in photoIDList:
		 		self.writePhotoFile(self.listPhotoTags(photoID), photoID, userID)
		 		
	def listUserPhotos(self, userID):
		photoIDList = []
		userPhotosResult = self.flickr.people_getPublicPhotos(user_id=userID)
		
		for root in userPhotosResult:
			for photo in root:
				if len(photoIDList) < 30:
					photoIDList.append(photo.get('id'))
				else:
					break
				
		#print photoIDList
		return photoIDList
		
	def listPhotoTags(self, photoID):
		tagList = []
		tagSearchResult = self.flickr.tags_getListPhoto(photo_id=photoID)
		
		for photoRoot in tagSearchResult:
			for tagRoot in photoRoot:
				for tag in tagRoot:
					tagList.append(tag.get('raw'))
		
		#print tagList
		return tagList
		
	def writePhotoFile(self, tagList, photoID, userID):
		file = open(self.resultDir + userID + '/' + photoID + '.txt', 'w+')
		tagUTF8 = ''
		for tag in tagList:
			#tagUTF8 = unicode(tag.content.strip(codecs.BOM_UTF8), 'utf-8')
			file.write(tag.encode('utf-8') + '\n')
		#file.writelines(tagList)
		file.close()
