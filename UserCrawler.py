class UserCrawler:

	listSize = 0
	placeID = None
	flickr = None
	
	userList = []
	
	def __init__(self, flickr, listSize, placeID):
		self.listSize = listSize
		self.placeID = placeID
		self.flickr = flickr

	def buildUserList(self):
		""" Build the user list with the given size """
		pageNumber = 1
		searchResult = self.flickr.photos_search(place_id=self.placeID, per_page='500', has_geo='1', page=pageNumber)
		#searchResult = self.flickr.photos_getRecent()
		
		while len(self.userList) < self.listSize:
			for rootTag in searchResult:
				for photoTag in rootTag:
					userID = photoTag.get('owner')
					if not self.isDuplicatedUser(userID) and self.numberOfPhotos(userID) >= 30: #and self.isFromMinasGerais(userID):
						self.userList.append(userID)
						print "inserted user! userListSize: " + str(len(self.userList))
			print 'pageCollected: ' + str(pageNumber)
			pageNumber += 1
			searchResult = self.flickr.photos_search(place_id=self.placeID, per_page='500', has_geo='1', page=pageNumber)
		
		print 'User List build finish. number of user: ' + str(len(self.userList))
		return self.userList
		
	def isDuplicatedUser(self, userID):
		""" Check if the user is already in the list """
		for user in self.userList:
			if user == userID:
				return True
		return False
		
	def numberOfPhotos(self, userID):
		""" Check if the user have 30 or more photos """
		searchResult = self.flickr.photos_search(user_id=userID, per_page='30')
		photosNumber = 0 
		for rootTag in searchResult:
			for photoTag in rootTag:
				photosNumber += 1
		return photosNumber
					
	def isFromMinasGerais(self, userID):
		""" Check if user location is from Minas Gerais """
		userLocation = ''
	
		userInfo = self.flickr.people_getInfo(user_id=userID)
		for root in userInfo:
			userLocation = root.find('location')
			if userLocation != None:
				userLocation = root.find('location').text
				#print userLocation
			if userLocation == None:
				return False
			elif 'BELO HORIZONTE' in userLocation.upper() or \
				 'MINAS GERAIS' in userLocation.upper() or \
				 ' MG ' in userLocation.upper() or \
				 ' MG,' in userLocation.upper() or \
				 ', MG' in userLocation.upper() or \
				 ',MG ' in userLocation.upper():
				#print 'coletado: ' + userLocation
				return True