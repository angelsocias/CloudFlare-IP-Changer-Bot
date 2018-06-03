import sys
if sys.version_info >= (3, 0):
	import urllib.request
	NEW_IP = urllib.request.urlopen("http://ip.42.pl/raw").read().decode('utf-8')
else:
	from urllib2 import urlopen
	NEW_IP = urlopen('http://ip.42.pl/raw').read()
import requests
import json


###############################################################################
API_ENDPOINT = "https://api.cloudflare.com/client/v4/zones/" #Don't change it!

CLOUDFLARE_API = "CloudFlareAPIKey" #Your cloudflare API Key, you can get it accesing to your account https://dash.cloudflare.com/profile and clicking in "Global API Key"
CLOUDFLARE_ZONE = "CloudFlareZoneID" #Your CloudFlare Zone ID, you can get it on the Overwiew window
CLIENT_MAIL = "example@gmail.com" #Your e-mail
SUBDOMAIN_TO_EDIT = "subdomain" #Subdomain it will change the IP

#All the other information, like the domain or the subdomain ID will get it automatically!

################################################################################



headers = { 
  "X-Auth-Email": CLIENT_MAIL ,
    "Content-Type": "application/json",
    "X-Auth-Key": CLOUDFLARE_API
}

r = requests.get(url = API_ENDPOINT+CLOUDFLARE_ZONE, headers = headers)
response = json.loads(r.text)

DOMAIN = response['result']['name']

r2 = requests.get(url=API_ENDPOINT+CLOUDFLARE_ZONE+'/dns_records', headers=headers)
response = json.loads(r2.text)['result']

for i in response:
	if i['name'] == SUBDOMAIN_TO_EDIT+"."+DOMAIN:
		ID_SUBDOMAIN = i['id']
		TYPE_SUBDOMAIN = str(i['type'])
		CURRENT_IP = i['content']

if str(CURRENT_IP) == str(NEW_IP):
	print("Same IP")
else:
	print("Different IP, changing it...")
	data = {"type":TYPE_SUBDOMAIN,"name":SUBDOMAIN_TO_EDIT+"."+DOMAIN,"content":NEW_IP}

	r3 = requests.put(url=API_ENDPOINT+CLOUDFLARE_ZONE+'/dns_records/'+ID_SUBDOMAIN, headers=headers, data=json.dumps(data))
	response = json.loads(r3.text)['result']
	print("Changed!")
