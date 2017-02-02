import sys
import json
import re


freq_scores = {}


def lines(fp):
    print str(len(fp.readlines()))



def get_freq(tfile):
	count = 0
	wc = 0
	for line in tfile:
		a = json.loads(line.encode('utf-8'))
		#print a.items()
		key = 'text'
		if key in a:
			#t = a[key].encode('utf-8').split(' ')
			t = re.findall(r"[\w']+", a[key].encode('utf-8'))
			for i in t:
				wc = wc + 1
				if i not in freq_scores:
					freq_scores[i] = 0
				else:
					freq_scores[i] = freq_scores[i] + 1
		# count = count + 1
		# if count > 100:
		# 	break 

	for key,val in freq_scores.items():
		freq_scores[key] = float(val)/wc


def main():
    tweet_file = open(sys.argv[1])
    #lines(tweet_file)
    get_freq(tweet_file)
    for key,val in freq_scores.items():
    	print key+' '+ str(val)

if __name__ == '__main__':
    main()
