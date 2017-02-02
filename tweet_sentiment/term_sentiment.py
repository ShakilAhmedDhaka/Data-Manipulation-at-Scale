import sys
import json


scores = {} 
new_scores = {}

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))



def get_tweets(tfile):
	#count = 0
	for line in tfile:
		a = json.loads(line.encode('utf-8'))
		#print a.items()
		val = 0
		key = 'text'
		if key in a:
			t = a[key].encode('utf-8').split(' ')
			for i in t:
				if i in scores:
					val = val + scores[i]
			n = len(t)
			for i in t:
				if i not in scores:
					if i not in new_scores:
						new_scores[i] = 0.0
					new_scores[i] = new_scores[i] + float(val)/n
					#print new_scores[i]
		#print val

		# count = count + 1
		# if count > 20:
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
    get_tweets(tweet_file)
    for key,val in new_scores.items():
    	print key+' '+ str(val)

if __name__ == '__main__':
    main()
