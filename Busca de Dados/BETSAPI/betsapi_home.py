import re
import os.path
import base64
import gzip
import zlib
from io import BytesIO

import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

def make_requests():
	response = [None]

	if(request_pt_betsapi_com(response)):
		response[0].close()


def request_pt_betsapi_com(response):
	response[0] = None

	try:
		req = urllib2.Request("https://pt.betsapi.com/")

		req.add_header("Accept", "text/html, application/xhtml+xml, */*")
		req.add_header("Referer", "https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D177684156000502%26redirect_uri%3Dhttps%253A%252F%252Fpt.betsapi.com%252Fauth%252F%26scope%3Demail%26state%3DHA-VL7ZXHWI4638UG9ET1MOARK2JFQPS0NCBD5Y%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db1412044-ce92-442b-ab89-71fe39e2e691%26cbt%3D1601407324477&lwv=101")
		req.add_header("Accept-Language", "pt-BR")
		req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
		req.add_header("Accept-Encoding", "gzip, deflate")
		req.add_header("Connection", "Keep-Alive")
		req.add_header("Cookie", "__cfduid=d493479cf88f039d7820dd177635d0c781601389060; _ga=GA1.2.373783472.1601389060; _gid=GA1.2.1058110219.1601389060; _gat=1; sid=7r8u78qgphk87hn5p1iqfvl8fp; hstpconfig=eyJJRCI6IjU5Mjk0NTk5dWk1ZjczNTZmOWJjMzYwIiwiQ1RSIjoiQlIiLCJSZWdpb24iOm51bGwsIkJyb3dzZXIiOiJJRSIsIlBsYXRmb3JtIjoiV2luNyIsIk1vYmlsZSI6MCwiQm90IjowLCJyZW1vdGVfYWRkciI6NzcwMTg1MTA0LCJMYXN0VXBkYXRlIjoxNjAxMzk0NDI1LCJub2NhY2hlIjp0cnVlLCJlcnJvciI6ZmFsc2UsImxhc3RUcmFja2VyIjoxfQ%3D%3D; lasttrack45424=1; hstpcount45424=eyJDbGljayI6MCwiQ291bnRlciI6MX0%3D; tz=America%2FSao_Paulo")

		response[0] = urllib2.urlopen(req)

	except urllib2.URLError, e:
		if not hasattr(e, "code"):
			return False
		response[0] = e
	except:
		return False

	return True
