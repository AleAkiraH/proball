import re
import os.path
import urllib.request
import base64
import gzip
import zlib
from io import StringIO
from io import BytesIO

import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

def make_requests():
	"""Calls request functions sequentially."""
	response = [None]
	responseText = None

	if(request_betsapi_com(response)):
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


def request_betsapi_com(response):
	"""Tries to request the URL. Returns True if the request was successful; false otherwise.
	http://betsapi.com/login
	
	response -- After the function has finished, will possibly contain the response to the request.
	
	"""
	response[0] = None

	try:
		# Create request to URL.
		req = urllib.request.Request("http://betsapi.com/login")

		# Set request headers.
		req.add_header("Connection", "keep-alive")
		req.add_header("Upgrade-Insecure-Requests", "1")
		req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36")
		req.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
		req.add_header("Referer", "http://betsapi.com/")
		req.add_header("Accept-Encoding", "gzip, deflate")
		req.add_header("Accept-Language", "en-US,en;q=0.9,pt;q=0.8")
		req.add_header("Cookie", "_ga=GA1.2.1777462985.1596768026; __gads=ID=db13eec9197acded-22bc78cd46b800c6:T=1603903411:RT=1603903411:S=ALNI_MZ0OX-ieeYQiTQdZT1FhL30Lnd6WA; __cfduid=d6b1f0377f0be126d9dc2705e52c2e6b41605193338; sid=qc2av3ci6a0dj7oa4iuhu7ni64; tz=America%2FSao_Paulo; _gid=GA1.2.1806760520.1606923956; SL_GWPT_Show_Hide_tmp=1")

		# Get response to request.
		response[0] = urllib.request.urlopen(req)

	except:
		return False

	return True
