from datetime import datetime

teams = {
	'Rocket City Trash Pandas': {
		'color': 'blue',
		'pizza': 'anything',
		'animal': 'red panda',
		'subject': 'lunch',
		'book': 'mystery',
		'pic' : 'TrashPandas.png',
		'site' : 'https://www.milb.com/rocket-city'
		
	},
	'Savannah Bananas': {
		'color': 'yellow',
		'pizza': 'banana peppers',
		'animal': 'giraffe',
		'subject': 'language arts',
		'book': 'satire',
		'pic' : 'SavannahBananas.png',
		'site' : 'https://thesavannahbananas.com/'
	},
	'Albuquerque Isotopes': {
		'color': 'silver',
		'pizza': 'pineapple',
		'animal': 'shark',
		'subject': 'science',
		'book': 'non-fiction',
		'pic': 'AlbuquerqueIsotopes.png',
		'site' : 'https://www.milb.com/albuquerque'
	},
	'Utica Unicorns': {
		'color': 'purple',
		'pizza': 'pepperoni',
		'animal': 'narwhal',
		'subject': 'theatre',
		'book': 'fantasy',
		'pic': 'UticaUnicorns.png',
		'site': 'https://uspbl.com/teams/utica-unicorns/'
	}
}

points = {
	'Rocket City Trash Pandas': 0,
	'Savannah Bananas' : 0,
	'Albuquerque Isotopes' : 0,
	'Utica Unicorns' : 0
}

def tallyPoints(color, pizza, animal, subject, book):
	for key in teams:
		# print(teams[key]['color'])
		currentTeam = key
		# print(currentTeam)
		if color == teams[key]['color']:
			points[currentTeam] += 1
		if pizza == teams[key]['pizza']:
			points[currentTeam] += 1
		if animal == teams[key]['animal']:
			points[currentTeam] += 1
		if subject == teams[key]['subject']:
			points[currentTeam] += 1
		if book == teams[key]['book']:
			points[currentTeam] += 1

	highest = 0
	winner = ''
	for key in points:
		if points[key] > highest:
			highest = points[key]
			winner = key
	return winner
			
def getImage(winner):
	for key in teams:
		if winner == key:
			return teams[key]['pic']


def getUrl(winner):
	for key in teams:
		if winner == key:
			return teams[key]['site']


def getDateString(date):
	dateStr = date.strftime('%A') + ' ' + date.strftime('%B') + ' ' + str(date.day) + ', ' + str(date.year)
	return dateStr

# print(tallyPoints('blue', 'anything', 'giraffe'))
# print(getDateString(datetime.now()))
		