import requests
import os.path
import os, ssl

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
	ssl._create_default_https_context = ssl._create_unverified_context

def get_list_series_availables(url):
	response = [None]
	headers = {"Accept-Language": "en-US,en;q=0.9,pt;q=0.8"
	,"Sec-Fetch-Site": "none"
	,"Sec-Fetch-Mode": "navigate"
	,"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
	,"Connection": "close"
	,"Cookie": "_ga=GA1.2.1777462985.1596768026; hstpconfig=eyJJRCI6Ijk0MzQ1Nzc2d2FuNWY3MGE0M2EzNTc0NiIsIkNUUiI6IkJSIiwiUmVnaW9uIjpudWxsLCJCcm93c2VyIjoiQ2hyb21lIiwiUGxhdGZvcm0iOiJXaW5kb3dzIiwiTW9iaWxlIjowLCJCb3QiOjAsInJlbW90ZV9hZGRyIjoiNzcwMTg1MTA0IiwiTGFzdFVwZGF0ZSI6MTYwMTIxNzU5NH0%3D; __gads=ID=db13eec9197acded-22bc78cd46b800c6:T=1603903411:RT=1603903411:S=ALNI_MZ0OX-ieeYQiTQdZT1FhL30Lnd6WA; __cfduid=d6b1f0377f0be126d9dc2705e52c2e6b41605193338; sid=qc2av3ci6a0dj7oa4iuhu7ni64; tz=America%2FSao_Paulo; _gid=GA1.2.1806760520.1606923956; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; hstpcount45424=eyJDbGljayI6MCwiQ291bnRlciI6MX0%3D; _gat=1"
	,"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
	,"Upgrade-Insecure-Requests": "1"
	,"Sec-Fetch-Dest": "document"}
	
	response[0] = requests.get(url, verify=False, headers=headers).text
	return response[0]