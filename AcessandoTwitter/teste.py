import oauth2 as oauth
import urllib2 as urllib

access_token_key = "444577132-55V5jT7fSkIS07ayF8WsGOmGV2iZmXp443eXyVnf"
access_token_secret = "KDEx4eYW5oamAxexL8zwfDS6M90jn4sEa5tQJohDi9Otj"
consumer_key = "h1GX0FfEcWE3ImWDTY71QLY4P"
consumer_secret = "2l3dLUU1hjcID6XiKUkV5dCpTsDFN3pHl4JVx3F9go2C7NiM6s"

_debug = 0
oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()
http_method = "GET"
http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)
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

def fetchsamples():
  url = "https://stream.twitter.com/1/statuses/sample.json"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  for line in response:
    print line.strip()
  
if __name__ == '__main__':
  fetchsamples()
      
