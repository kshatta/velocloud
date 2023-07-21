import requests
import json

url = "https://<company>.velocloud.net/portal/rest/enterprise/getEnterpriseEdges"

payload = "{\"enterpriseId\":1}"
headers = {
  'Authorization': 'token XXXX',
  'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)


data = response.text


#print("Type:", type(data))

json_object = json.loads(data)

#print("Type:", type(json_object))

#The following line will print the object with ID 3
print(json.dumps(json_object[3], indent=4))

#The previous code will print the whole dictionary object, if we want just the value for the key id we can type the following 
print(json_object[3]['id'])
