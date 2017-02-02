import sys
import json
import operator



htags = {}


def lines(fp):
    print str(len(fp.readlines()))



def get_tweets(tfile):
	count = 0
	for line in tfile:
		a = json.loads(line.encode('utf-8'))
		#print a.items()
		val = 0
		key = 'entities'
		if key in a:
			t = a[key]['hashtags'] # i is a "hashtags"  array consist of text , indices
			if len(t) is not 0:
				for i in t:
					x = i['text'].encode('utf-8')
					if x not in htags:
						htags[x] = 1
					else:
						htags[x] = htags[x] + 1

		# count = count + 1
		# if count > 100:
		# 	break


def main():
    tweet_file = open(sys.argv[1])
    #lines(tweet_file)
    get_tweets(tweet_file)

    sorted_tags = sorted(htags.items(), key=operator.itemgetter(1))
    sorted_tags.reverse()
    count =0
    for i,j in sorted_tags:
    	print i + ' ' + str(j)
    	count = count + 1
    	if count == 10:
    		break

if __name__ == '__main__':
    main()
