import re
import os.path
import base64
import gzip
import zlib
from io import BytesIO

import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

def make_requests(url):
	response = [None]
	responseText = None

	if(request_pt_betsapi_com(url, response)):
		responseText = read_response(response[0])

		response[0].close()
		return responseText


def read_response(response):
	if response.info().get('Content-Encoding') == 'gzip':
		buf = BytesIO(response.read())
		return gzip.GzipFile(fileobj=buf).read()

	elif response.info().get('Content-Encoding') == 'deflate':
		decompress = zlib.decompressobj(-zlib.MAX_WBITS)
		inflated = decompress.decompress(response.read())
		inflated += decompress.flush()
		return inflated

	return response.read()


def request_pt_betsapi_com(url, response):
	response[0] = None

	try:
		req = urllib2.Request(url)

		req.add_header("Accept-Language", "pt-BR")
		req.add_header("Accept-Encoding", "gzip, deflate")
		req.add_header("Connection", "close")
		req.add_header("Accept", "text/html, application/xhtml+xml, */*")
		req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
		req.add_header("Cookie", "__cfduid=d493479cf88f039d7820dd177635d0c781601389060; _ga=GA1.2.373783472.1601389060; _gid=GA1.2.1058110219.1601389060; _gat=1; sid=7r8u78qgphk87hn5p1iqfvl8fp; hstpconfig=eyJJRCI6IjU5Mjk0NTk5dWk1ZjczNTZmOWJjMzYwIiwiQ1RSIjoiQlIiLCJSZWdpb24iOm51bGwsIkJyb3dzZXIiOiJJRSIsIlBsYXRmb3JtIjoiV2luNyIsIk1vYmlsZSI6MCwiQm90IjowLCJyZW1vdGVfYWRkciI6NzcwMTg1MTA0LCJMYXN0VXBkYXRlIjoxNjAxMzk0NDI1LCJub2NhY2hlIjp0cnVlLCJlcnJvciI6ZmFsc2UsImxhc3RUcmFja2VyIjoxfQ%3D%3D; lasttrack45424=1; hstpcount45424=eyJDbGljayI6MCwiQ291bnRlciI6MX0%3D; tz=America%2FSao_Paulo")

		response[0] = urllib2.urlopen(req)

	except urllib2.URLError, e:
		if not hasattr(e, "code"):
			return False
		response[0] = e
	except:
		return False

	return True
