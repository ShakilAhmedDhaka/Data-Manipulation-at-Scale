import oauth2 as oauth
import urllib2 as urllib
import time

# See assignment1.html instructions or README for how to get these credentials

api_key = "MNp2mIr3jojRaHvmsJMF3mOtv"
api_secret = "PLjV8oBmGJuz2GZ5XfyBXspqV3oeGKO7ne35CW93o89yJEHXfW"
access_token_key = "3729400874-kjlBtZC079zhyjbypM5gR3PtmJl2F3SMu1sxL5t" 
access_token_secret = "hLGbPHYBBKHy5FIIwxaFQmDltjYMr7ZhaV4JcoSTs7rR6"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples(timeout=60):
  url = "https://stream.twitter.com/1.1/statuses/sample.json"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  start_interval = time.time()
  end_time = start_interval + timeout
  with open('output2.txt', 'w') as writer:
    for line in response:
      writer.write(line)
      now = time.time()
      if now > end_time:
        break
  return

if __name__ == '__main__':
  fetchsamples()
  with open('output2.txt') as lines:
    with open('problem_1_submission2.txt', 'w') as writer:
      for index, line in enumerate(lines):
        writer.write(line)
        if index == 19:
          break