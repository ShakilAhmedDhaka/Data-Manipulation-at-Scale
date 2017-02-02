import sys
import json
import re



coor  = [['Alabama', 32.806671, -86.79113, ''], ['Alaska', 61.370716, -152.404419, ''], ['Arizona', 33.729759, -111.431221, ''], ['Arkansas', 34.969704, -92.373123, ''], ['California', 36.116203, -119.681564, ''], ['Colorado', 39.059811, -105.311104, ''], ['Connecticut', 41.597782, -72.755371, ''], ['Delaware', 39.318523, -75.507141, ''], ['District of Columbia', 38.897438, -77.026817, ''], ['Florida', 27.766279, -81.686783, ''], ['Georgia', 33.040619, -83.643074, ''], ['Hawaii', 21.094318, -157.498337, ''], ['Idaho', 44.240459, -114.478828, ''], ['Illinois', 40.349457, -88.986137, ''], ['Indiana', 39.849426, -86.258278, ''], ['Iowa', 42.011539, -93.210526, ''], ['Kansas', 38.5266, -96.726486, ''], ['Kentucky', 37.66814, -84.670067, ''], ['Louisiana', 31.169546, -91.867805, ''], ['Maine', 44.693947, -69.381927, ''], ['Maryland', 39.063946, -76.802101, ''], ['Massachusetts', 42.230171, -71.530106, ''], ['Michigan', 43.326618, -84.536095, ''], ['Minnesota', 45.694454, -93.900192, ''], ['Mississippi', 32.741646, -89.678696, ''], ['Missouri', 38.456085, -92.288368, ''], ['Montana', 46.921925, -110.454353, ''], ['Nebraska', 41.12537, -98.268082, ''], ['Nevada', 38.313515, -117.055374, ''], ['New Hampshire', 43.452492, -71.563896, ''], ['New Jersey', 40.298904, -74.521011, ''], ['New Mexico', 34.840515, -106.248482, ''], ['New York', 42.165726, -74.948051, ''], ['North Carolina', 35.630066, -79.806419, ''], ['North Dakota', 47.528912, -99.784012, ''], ['Ohio', 40.388783, -82.764915, ''], ['Oklahoma', 35.565342, -96.928917, ''], ['Oregon', 44.572021, -122.070938, ''], ['Pennsylvania', 40.590752, -77.209755, ''], ['Rhode Island', 41.680893, -71.51178, ''], ['South Carolina', 33.856892, -80.945007, ''], ['South Dakota', 44.299782, -99.438828, ''], ['Tennessee', 35.747845, -86.692345, ''], ['Texas', 31.054487, -97.563461, ''], ['Utah', 40.150032, -111.862434, ''], ['Vermont', 44.045876, -72.710686, ''], ['Virginia', 37.769337, -78.169968, ''], ['Washington', 47.400902, -121.490494, ''], ['West Virginia', 38.491226, -80.954453, ''], ['Wisconsin', 44.268543, -89.616508, ''], ['Wyoming', 42.755966, -107.30249, '']]

happy_scores = {'Mississippi': 0.0, 'Oklahoma': 0.0, 'Delaware': 0.0, 'Minnesota': 0.0, 'Illinois': 0.0, 'Arkansas': 0.0, 'New Mexico': 0.0, 'Indiana': 0.0, 'Maryland': 0.0, 'Louisiana': 0.0, 'Idaho': 0.0, 'Wyoming': 0.0, 'Tennessee': 0.0, 'Arizona': 0.0, 'Iowa': 0.0, 'Michigan': 0.0, 'Kansas': 0.0, 'Utah': 0.0, 'Virginia': 0.0, 'Oregon': 0.0, 'Connecticut': 0.0, 'Montana': 0.0, 'California': 0.0, 'Massachusetts': 0.0, 'West Virginia': 0.0, 'South Carolina': 0.0, 'New Hampshire': 0.0, 'Wisconsin': 0.0, 'Vermont': 0.0, 'Georgia': 0.0, 'North Dakota': 0.0, 'Pennsylvania': 0.0, 'Florida': 0.0, 'Alaska': 0.0, 'Kentucky': 0.0, 'Hawaii': 0.0, 'Nebraska': 0.0, 'Missouri': 0.0, 'Ohio': 0.0, 'Alabama': 0.0, 'New York': 0.0, 'South Dakota': 0.0, 'Colorado': 0.0, 'New Jersey': 0.0, 'Washington': 0.0, 'North Carolina': 0.0, 'District of Columbia': 0.0, 'Texas': 0.0, 'Nevada': 0.0, 'Maine': 0.0, 'Rhode Island': 0.0}

states = {
        'AK': 'Alaska','AL': 'Alabama','AR': 'Arkansas','AS': 'American Samoa','AZ': 'Arizona','CA': 'California','CO': 'Colorado',
        'CT': 'Connecticut','DC': 'District of Columbia','DE': 'Delaware','FL': 'Florida','GA': 'Georgia','GU': 'Guam','HI': 'Hawaii','IA': 'Iowa','ID': 'Idaho','IL': 'Illinois',
        'IN': 'Indiana','KS': 'Kansas','KY': 'Kentucky','LA': 'Louisiana','MA': 'Massachusetts','MD': 'Maryland','ME': 'Maine','MI': 'Michigan','MN': 'Minnesota','MO': 'Missouri',
        'MP': 'Northern Mariana Islands','MS': 'Mississippi','MT': 'Montana','NA': 'National','NC': 'North Carolina','ND': 'North Dakota','NE': 'Nebraska','NH': 'New Hampshire','NJ': 'New Jersey','NM': 'New Mexico',
        'NV': 'Nevada','NY': 'New York','OH': 'Ohio','OK': 'Oklahoma','OR': 'Oregon','PA': 'Pennsylvania','PR': 'Puerto Rico','RI': 'Rhode Island','SC': 'South Carolina','SD': 'South Dakota',
        'TN': 'Tennessee','TX': 'Texas','UT': 'Utah','VA': 'Virginia','VI': 'Virgin Islands','VT': 'Vermont','WA': 'Washington','WI': 'Wisconsin','WV': 'West Virginia','WY': 'Wyoming'}



scores = {}




def lines(fp):
    print str(len(fp.readlines()))

def get_coordinates():
	for x,y,z,w in coor:
		print x 


def get_closest(a,b):
	state = None
	mn_dist = 10000000000
	for i in coor:
		dist = ((a - i[1])**2+(b - i[2])**2)**.5
		if dist < mn_dist:
			mn_dist = dist
			state = i[0]
	return state 



def find_state(a):
	cord = 'coordinates'
	place = 'place'
	user = 'user'
	state = None

	if cord in a and a[cord] is not None:
		loc = a[cord]['coordinates']
		#print loc
		#print loc[0],loc[1]
		state = get_closest(loc[0],loc[1])
		if state is not None:
			return state

	if place in a and a[place] is not None:
		if a[place]["country"].encode('utf-8') is "United States":
			if a[place]["name"] is not None:
				return a[place]["name"].encode('utf-8')

	if user in a and a[user] is not None:
		if a[user]["location"] is not None:
			return a[user]["location"].encode('utf-8')
	return state




def get_tweets(tfile):
	count = 0
	for line in tfile:
		a = json.loads(line.encode('utf-8'))
		#print a.items()
		val = 0.0
		key = 'text'
		if key in a:
			t = re.findall(r"[\w']+", a[key].encode('utf-8'))
			for i in t:
				if i in scores:
					#print i
					val = val + scores[i]

			#print a[key].encode('utf-8') + ' '+ str(val)
		state = find_state(a)
		#print state
		if state is not None:
			state_strings = re.findall(r"[\w']+", state)
			if len(state_strings) is not 0:
				#print state_strings
				for cd,nm in states.items():
					for j in nm.split(' '):
						for i in state_strings:
							if cd == i or j == i:
								if cd not in happy_scores:
									happy_scores[cd] = 0.0
								#print nm
								happy_scores[cd] = happy_scores[cd] + val

		# count = count + 1
		# if count > 1000:
		# 	break


def get_scores(afinnfile):
	#afinnfile = open("AFINN-111.txt")
	#scores = {} # initialize an empty dictionary
	for line in afinnfile:
		#print "ok"
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	  	scores[term] = int(score)  # Convert the score to an integer.

	#print scores.items() # Print every (term, score) pair in the dictionary   






def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    get_scores(sent_file)
    #get_coordinates()
    get_tweets(tweet_file)


    name = ''
    s = -100000000000
    for nm,scr in happy_scores.items():
    	if scr > s:
    		s = scr
    		name = nm
    print name

if __name__ == '__main__':
    main()
