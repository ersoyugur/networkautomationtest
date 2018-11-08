#!/usr/bin/env python

import requests
import json

def get_token(url, data, headers):
	response = requests.post(url, json.dumps(data), headers = headers)
	resp_json = response.json()
	#print response
	#print "===================="
	#print response.json()
	#print "===================="
	#print "Status Code: {}".format(response.status_code)
	#print "===================="
	#print "Raw Response: {}".format(response.text)
	#print "===================="
	#print "Fancy Output: {}".format(json.dumps(response.json()))
	#print "===================="
	#print "Fancy Output: {}".format(json.dumps(response.json()), indent=4)
	return resp_json["response"]["serviceTicket"]
#if resp.status_code != 200:
#	raise ApiError('GET /api/v1/topology/vrf/vrf-name/ {}'.format(resp.status_code))
#for todo_item in resp.json():
#	print('{} {}'.format(todo_item['id'], todo_item['summary']))

def get_ipmac(url, token, data, headers):
	headers['X-Auth-Token'] = token
	response = requests.get(url, json.dumps(data), headers = headers)
	resp_json = response.json()
	for item in resp_json["response"]:
		print "IP Address: {0} MAC Address: {1}".format(item["hostIp"], item["hostMac"])
	

def get_run(url, token, data, headers):
	file = "_Configuration.txt"
	headers['X-Auth-Token'] = token
        response = requests.get(url, json.dumps(data), headers = headers)
        resp_json = response.json()
	i = 0
	#for lines in resp_json["response"]:
	#	i = i + 1
	#	print "Router#{0} + ID: {1}".format(i, lines["id"])
	
	for lines in resp_json["response"]:
		filename = lines["id"] + file
		with open(filename, 'w+') as f:
			print >> f, lines["runningConfig"]
	#print json.dumps(resp_json["response"][0]["runningConfig"])

mainurl = 'https://devnetapi.cisco.com/sandbox/apic_em/'
config_url1 = mainurl + 'api/v1/host?limit=1&offset=1'
config_url = mainurl + 'api/v1/host'
run_url = mainurl + 'api/v1/network-device/config'



token_url = 'https://devnetapi.cisco.com/sandbox/apic_em/api/v1/ticket'
payload = {'username':'devnetuser',
	   'password':'Cisco123!'}
headers = {'Content-type':'application/json'}

if __name__ == '__main__':
	token = get_token(token_url, payload, headers)	
    	get_ipmac(config_url, token, payload, headers)
	get_run(run_url, token, payload, headers)
