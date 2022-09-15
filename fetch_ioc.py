#!/usr/bin/env python

import requests
from datetime import datetime
import json

TargetHost = "https://threatfox-api.abuse.ch/api/v1/"
payload = { "query": "get_iocs", "days": 1 }
now = datetime.now()
FileName = now.strftime('%d-%m-%Y') + ".txt"

def DownloadIOC(TargetHost):
	r = requests.post(TargetHost, json= payload)
	f = open(FileName,"w")
	f.write(r.text)
	f.close()  
DownloadIOC(TargetHost)

def NormaliseData():
	f = open(
