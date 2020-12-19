import re
import os.path
import urllib2
import base64
import gzip
import zlib
from StringIO import StringIO
from io import BytesIO

import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
	ssl._create_default_https_context = ssl._create_unverified_context

def make_requests():
	"""Calls request functions sequentially."""
	response = [None]
	responseText = None

	if(request_www_facebook_com(response)):
		# Success, possibly use response.
		responseText = read_response(response[0])

		response[0].close()
	else:
		# Failure, cannot use response.
		pass


def read_response(response):
	""" Returns the text contained in the response.  For example, the page HTML.  Only handles the most common HTTP encodings."""
	if response.info().get('Content-Encoding') == 'gzip':
		buf = StringIO(response.read())
		return gzip.GzipFile(fileobj=buf).read()

	elif response.info().get('Content-Encoding') == 'deflate':
		decompress = zlib.decompressobj(-zlib.MAX_WBITS)
		inflated = decompress.decompress(response.read())
		inflated += decompress.flush()
		return inflated

	return response.read()


def request_www_facebook_com(response):
	"""Tries to request the URL. Returns True if the request was successful; false otherwise.
	https://www.facebook.com/login.php?skip_api_login=1&amp;api_key=177684156000502&amp;kid_directed_site=0&amp;app_id=177684156000502&amp;signed_next=1&amp;next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D177684156000502%26redirect_uri%3Dhttps%253A%252F%252Fbetsapi.com%252Fauth%252F%26scope%3Demail%26state%3DHA-IBN9E12WLK6RDCOQG08TZFMAYHU3J74XP5VS%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddc42a404-6ac7-4fe0-bd00-fab6bb392ff9%26tp%3Dunspecified&amp;cancel_url=https%3A%2F%2Fbetsapi.com%2Fauth%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DHA-IBN9E12WLK6RDCOQG08TZFMAYHU3J74XP5VS%23_%3D_&amp;display=page&amp;locale=en_US&amp;pl_dbl=0
	
	response -- After the function has finished, will possibly contain the response to the request.
	
	"""
	response[0] = None

	try:
		# Create request to URL.
		req = urllib2.Request("https://www.facebook.com/login.php?skip_api_login=1&api_key=177684156000502&kid_directed_site=0&app_id=177684156000502&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D177684156000502%26redirect_uri%3Dhttps%253A%252F%252Fbetsapi.com%252Fauth%252F%26scope%3Demail%26state%3DHA-IBN9E12WLK6RDCOQG08TZFMAYHU3J74XP5VS%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddc42a404-6ac7-4fe0-bd00-fab6bb392ff9%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fbetsapi.com%2Fauth%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DHA-IBN9E12WLK6RDCOQG08TZFMAYHU3J74XP5VS%23_%3D_&display=page&locale=en_US&pl_dbl=0")

		# Set request headers.
		req.add_header("Connection", "keep-alive")
		req.add_header("Upgrade-Insecure-Requests", "1")
		req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36")
		req.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
		req.add_header("Sec-Fetch-Site", "cross-site")
		req.add_header("Sec-Fetch-Mode", "navigate")
		req.add_header("Sec-Fetch-User", "?1")
		req.add_header("Sec-Fetch-Dest", "document")
		req.add_header("Referer", "http://pt.betsapi.com/")
		req.add_header("Accept-Encoding", "gzip, deflate, br")
		req.add_header("Accept-Language", "en-US,en;q=0.9,pt;q=0.8")
		req.add_header("Cookie", "sb=fjFIXr3GPt9MVrxLrJ0zNhdc; datr=fjFIXq7QG0mUtZnuqeuFik1J; wd=1920x932; fr=0sXI4bo16sUjwgPs1.AWWH0BTndaANqJTAR3OoR-zXGJA.BffpXG.Tq.AAA.0.0.Bfx8Lq.AWVvVxxeazs")

		# Get response to request.
		response[0] = urllib2.urlopen(req)

	except urllib2.URLError, e:
		# URLError.code existing indicates a valid HTTP response, but with a non-200 status code (e.g. 304 Not Modified, 404 Not Found)
		if not hasattr(e, "code"):
			return False
		response[0] = e
	except:
		return False

	return True
