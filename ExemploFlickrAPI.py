import flickrapi

class FlickTagCrawler:
	def __init__(self):
		api_key = 'e63fa0acb8e1fd21c8a4123c0233bcc0'
		flickr = flickrapi.FlickrAPI(api_key)
		idMinasGerais = '7Mf2alBTUb7b7xzl'
		photos = flickr.photos_search(place_id=idMinasGerais, per_page='10', has_geo='1', tags='')
		
		index = 1;
		for root in photos:
			for photo in root:
				print 'photo' + str(index)
				print 'title: ' + photo.get('title')
				print 'owner' + photo.get('owner')
				print 'tag:' + photo.tag
				print 'attrib:' + str(photo.attrib)
				#print '\n\n'
				index += 1
		
		
		print '\n\n\n\n'
		tags = flickr.tags_getListPhoto(photo_id='15220391102')
		index = 1;
		for root2 in tags:
			for root3 in root2:
				for tag in root3:
					print 'tag' + str(index)
					print 'tag:' + tag.tag
					print 'attrib:' + str(tag.attrib)
					print '\n\n'
					index += 1
		
		#for photo in photos:
			#for child in photo.getchildren():
				#print child.get('tag')
				#print child.attrib
				
				
		#test = 0;
		#for photo in flickr.walk(place_id=idMinasGerais, per_page='10', has_geo='1'):
		#	if photo.tag == 'tag':
		#		print photo.items()
		#		print photo.tag
		#		#print photo.attrib
		#		break
		#	test += 1
		
		#for photo in flickr.walk(tag_mode='all', tags='sybren,365,threesixtyfive', min_taken_date='2008-08-20',max_taken_date='2008-08-30'):
		#	print photo.get('title')
		x = flickr.people_getInfo(user_id="9438939@N07")
		print str(x)
		for root in x:
			print root.attrib
			print root.find('location').text
			#for tag in root:
				#print tag.get('label')
				#tag.get('location')
		print "------------success!------------"
 
 
 
 
if __name__ == '__main__':
	parser_exec = FlickTagCrawler()