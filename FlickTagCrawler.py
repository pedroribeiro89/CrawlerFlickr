import flickrapi
import UserCrawler
import TagCrawler

class FlickrTagCrawler:
	
	API_KEY = 'e63fa0acb8e1fd21c8a4123c0233bcc0'
	USER_LIST_SIZE = 300
	USER_LIST_FILE_PATH = '/Users/pedroribeiro/Desktop/CrawlerFlickr/Result/UserList.txt'
	MINAS_GERAIS_ID = '7Mf2alBTUb7b7xzl'
	TAGS_DIR = '/Users/pedroribeiro/Desktop/CrawlerFlickr/Result/Tags/'
	
	userList = []

	def __init__(self):
		print "------------begin------------"
		flickr = flickrapi.FlickrAPI(self.API_KEY)
		#self.searchUsers(flickr)
		self.readUsers()
		self.searchTags(flickr)
		print "------------end!------------"
	
	def searchUsers(self, flickr):
		userCrawler = UserCrawler.UserCrawler(flickr, self.USER_LIST_SIZE, self.MINAS_GERAIS_ID)
		self.userList = userCrawler.buildUserList()
		self.writeUserList()
		print "users collected: " + str(len(userList))
		
	def searchTags(self, flickr):
		tagCrawler = TagCrawler.TagCrawler(flickr, self.userList, self.TAGS_DIR)
 		tagCrawler.execute()

 	def writeUserList(self):
 		file = open(self.USER_LIST_FILE_PATH, 'w+')
 		
 		for userIndex in range(0, self.USER_LIST_SIZE):
 			file.write(self.userList[userIndex] + '\n')
 		
 		file.close()
 	
 	def readUsers(self):
 		file = open(self.USER_LIST_FILE_PATH, 'r')
 		userIndex = 0
 		
 		for line in file:
 			if userIndex >= 244:
 				self.userList.append(line.replace('\n', ''))
 			userIndex += 1
 		file.close
 
 
if __name__ == '__main__':
	parser_exec = FlickrTagCrawler()